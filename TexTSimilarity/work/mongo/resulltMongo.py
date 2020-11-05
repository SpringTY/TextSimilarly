# from TexTSimilarity.work.mongo.mongoDB import getSet
#
# COLLECTION_NAME = 'similarity'
# similarity = getSet(COLLECTION_NAME)
#
#
# def insert_one(cmsResultId, cmsTaskId, cmsResultINFO):
#     cmsResult = {
#         'cmsResultId': cmsResultId,
#         'cmsTaskId': cmsTaskId,
#         'cmsResultINFO': cmsResultINFO
#     }
#     similarity.insert_one(cmsResult)
#
#
# def insert_many(cmsResults):
#     similarity.insert_many(cmsResults)
#
#
# def query(cmsTaskId):
#     cmsTaskId = str(cmsTaskId)
#     return similarity.find_one({'cmsTaskId': cmsTaskId})
#
# # if __name__ == '__main__':
# #     res = query('15')
#