from TexTSimilarity.work.similarCalc.similarCalcWCImp import similarCalcWCImp

similarCalc = {
    'similarCalcWCImp': similarCalcWCImp
}

DEFAULT_METHOD = 'similarCalcWCImp'


def similar(filePath, method=DEFAULT_METHOD):
    return similarCalc[method](filePath)


def getSimilarCalcMethods():
    return list(similarCalc.keys())


if __name__ == '__main__':
    print(1)
