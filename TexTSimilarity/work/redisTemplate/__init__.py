import redis

HOST = '202.205.99.174'
PASSWORD = 'TongYang123'
DATABASE = 0
PORT = '6379'

similarity = redis.Redis(host=HOST, port=PORT, password=PASSWORD, db=0)


def insert_one(cmsTaskId, cmsResultINFO):
    similarity.set('cmsTaskId:' + str(cmsTaskId), cmsResultINFO)


def query(cmsTaskId):
    return bytes.decode(similarity.get('cmsTaskId:' + str(cmsTaskId)))
