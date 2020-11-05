import redis

HOST = '47.98.177.164'
PASSWORD = 'MengQingQiang123'
DATABASE = 0
PORT = '6379'

similarity = redis.Redis(host=HOST, port=PORT, password=PASSWORD, db=0)


def insert_one(cmsTaskId, cmsResultINFO):
    similarity.set('cmsTaskId:' + str(cmsTaskId), cmsResultINFO)


def query(cmsTaskId):
    return bytes.decode(similarity.get('cmsTaskId:' + str(cmsTaskId)))
