#输入设定文档目录
#输出相似度超过阈值的文档对
import os
from math import ceil

import docx
import jieba
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

filterLength = 10#过滤文本长度值
#重命名所有报告名称为学号.文件格式

def getDocx(path:str):
    f = docx.Document(path)
    return(''.join(filterRow([p.text for p in f.paragraphs])))

def filterRow(doc:list):
    '''
    过滤文本中不需要的内容，可以添加更多规则
    '''
    for para in list(reversed(doc)):
        if '\xa0' in para:#删去代码段，有的高亮部分可以删去，有的删不去
            doc.remove(para)
        elif para in ['\n', '', ' ']:#删去没有文字的段
            doc.remove(para)
        elif len(para) < filterLength:#长度小于十，删去
            doc.remove(para)
    return doc

#从路径中读取文章
def readDocFromPath(path:str):
    docNameList, docTextList = [], []#文件名列表、文件内容列表
    failDocList = []
    for root, dirs, files in os.walk(path):
        for file in files:#对文件进行识别和分类，不同文件做不同处理
            try:
                extension = file.split('.')[-1]
                if extension == 'docx':#如果扩展名是docx
                    docTextList.append(getDocx(os.path.join(root, file)))
                    docNameList.append(file)
            except:
                failDocList.append(os.path.join(root, file))
    #print('以下文件读取失败')
    # print('\n'.join(failDocList))
    #print('文件读取完成')
    return(docNameList, docTextList)

#去标点（在求分词结果时用,加去停用词）
def remove_list():
    remove_list = ['，', '：', '。', '《', '》', '\n', '_', '“', '”', '、', ' ', ':', '（', '）', '.', '(', ')', '=']
    return remove_list

#分词结果
def jieba_result(content):
    res = jieba.lcut(content)
    for i in remove_list():
        while i in res:
            res.remove(i)
    return res

#计算相似度
def CalculateCos(gwyList, subList):
    gwyLen = 0
    for gwynum in gwyList:
        gwyLen = gwyLen + gwynum ** 2
    gwyLen = gwyLen ** 0.5
    subLen = 0
    for sub in subList:
        subLen = subLen + sub ** 2
    subLen = subLen ** 0.5
    # return subLen
    totalLen = len(gwyList)
    fenmu = 0
    for i in range(0,totalLen):
        fenmu = fenmu + subList[i] * gwyList[i]
    print(fenmu / (subLen * gwyLen))
    return fenmu / (subLen * gwyLen)

#tfidf
def tfidf_word(cmsFilePath):
    # 输入路径
    testPath = cmsFilePath
    #testPath = './test'
    docNameList, docTextList = readDocFromPath(testPath)
    top_n_res = []  # 词频结果
    for i in docTextList:
        top_n_res.append(' '.join(jieba_result(i)))
    vectorizer = CountVectorizer()  # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
    transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf权值
    tfidf = transformer.fit_transform(vectorizer.fit_transform(top_n_res))
    weight = tfidf.toarray()  # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
    similarity_tfidf = []
    section_list = []
    section = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for i in range(len(weight)):
        for j in range(i + 1, len(weight)):
            result = CalculateCos(weight[i], weight[j])
            #num = (result * 100) / 10
            num = ceil(result*10)-1
            if num in section:
                section[num] += 1
            #if int(num) in section:
                #section[int(num)] += 1
            similarity_tfidf.append({
                'from': i,
                'to': j,
                'similarity': result
            })
    #将字典类型转换成数组
    for i in section.items():
        section_list.append(i[1])
    #print(section_list)
    #print(section.items())
    return docNameList, similarity_tfidf, section_list
            #print(result)
            #if (result >= r):
                #print("result = ", result, docNameList[i], "与", docNameList[j], "相似")

if __name__ == '__main__':
    docNameList, similarity_tfidf, section_list =tfidf_word('C:/PyCharm/wf/test')





