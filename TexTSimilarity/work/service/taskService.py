import json

from TexTSimilarity.work.models.models import CMSTask, CMSFile, CMSResult
from TexTSimilarity.work.redisTemplate import insert_one
from TexTSimilarity.work.utils.constValues import CMSTaskStatus, CMSFileStatus
from TexTSimilarity.work.utils.fileUtils import del_file
from similarCalc import similar

'''
    潜在风险 对于cmsTaskStatus的操作
'''


def runTaskService(cmsTaskId):
    # 根据任务号得到任务
    cmsTask = CMSTask.objects.filter(cmsTaskId=cmsTaskId).first()
    # 检查任务是否存在 并且是否是<未运行状态>
    if cmsTask is not None and (not cmsTask.cmsTaskStatus == CMSTaskStatus.CREATED):
        return 'watting'
    # 给任务状态切换成正在工作中
    cmsTask.cmsTaskStatus = CMSTaskStatus.WORKING
    CMSTask.save(cmsTask)
    # 得到任意一个文件对象，获取相对路径前缀
    cmsFiles = CMSFile.objects.filter(cmsTaskId=cmsTaskId).first()
    # 计算得到结果
    docNameList, similarity = similar(cmsFiles.cmsFilePath)
    # 封装成字典
    cmsResult = {
        'docNameList': docNameList,
        'similarity': similarity
    }
    # 更新结果记录
    cmsResultMYSQL = CMSResult.create(cmsTaskId=cmsTaskId, cmsResultInfo='redis')
    cmsResultMYSQL.save()
    cmsResultID = cmsResultMYSQL.cmsResultId
    # Json结果
    cmsResultJSON = json.dumps(cmsResult)
    # 把Json结果放到Redis中
    insert_one(cmsTaskId=cmsTaskId, cmsResultINFO=cmsResultJSON)
    # 任务标记完成
    cmsTask.cmsTaskStatus = CMSTaskStatus.FINISHED
    CMSTask.save(cmsTask)
    # 删除本地文件
    del_file(cmsFiles.cmsFilePath)
    # 更新文件状态
    CMSFile.objects.filter(cmsTaskId=cmsTaskId).update(cmsFileStatus=CMSFileStatus.DELETE)
    return 'success'
