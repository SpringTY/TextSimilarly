from TexTSimilarity.work.similarCalc.similarCalcWCImp import similarCalcWCImp
import sys
# sys.path.append('C:/PyCharm/TextSimilarly/TexTSimilarity/work/similarCalc/tdidf_word')
from TexTSimilarity.work.similarCalc.similarCalcTFIDFImp import tfidf_word as similarCalcTFIDFImp

similarCalc = {
    'similarCalcWCImp': similarCalcWCImp,
    'similarCalcTFIDFImp': similarCalcTFIDFImp
}

DEFAULT_METHOD = 'similarCalcTFIDFImp'


def similar(filePath, method=DEFAULT_METHOD):
    return similarCalc[method](filePath)


def getSimilarCalcMethods():
    return list(similarCalc.keys())


if __name__ == '__main__':
    print(1)
