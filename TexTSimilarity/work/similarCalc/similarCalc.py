from TexTSimilarity.work.similarCalc.similarCalcWCImp import similarCalcWCImp
import sys
sys.path.append('C:/PyCharm/TextSimilarly/TexTSimilarity/work/similarCalc/tdidf_word')
from tfidf_word import tfidf_word
similarCalc = {
    'similarCalcWCImp': similarCalcWCImp, 'tfidf_word': tfidf_word
}

DEFAULT_METHOD = 'similarCalcWCImp'


def similar(filePath, method=DEFAULT_METHOD):
    return similarCalc[method](filePath)


def getSimilarCalcMethods():
    return list(similarCalc.keys())


if __name__ == '__main__':
    print(1)
