import pymongo

HOST = '47.98.177.164'
USERNAME = 'spring'
PASSWORD = 'tongyang123'
DATABASE = 'similarity'
Connection = pymongo.MongoClient(host=HOST, username=USERNAME, password=PASSWORD, authSource='similarity',
                                 authMechanism='SCRAM-SHA-256')


def getSet(name):
    return Connection[DATABASE][name]


if __name__ == '__main__':
    print(1)
