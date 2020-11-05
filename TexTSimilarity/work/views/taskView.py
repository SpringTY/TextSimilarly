from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.http import require_POST, require_GET
from TexTSimilarity.work.models.models import CMSFile, CMSTask, CMSResult
from TexTSimilarity.work.similarCalc.similarCalc import similar
from TexTSimilarity.work.utils.constValues import CMSTaskStatus, CMSFileStatus
from TexTSimilarity.work.redisTemplate import insert_one, query
from TexTSimilarity.work.utils.fileUtils import del_file
import json


@require_GET
def tasks(request):
    cms_tasks = CMSTask.objects.all().order_by('cmsTaskId')
    cms_tasks_json = serializers.serialize("json", cms_tasks)
    return HttpResponse(cms_tasks_json)


@require_GET
def runTask(request):
    print('in')
    cmsTaskId = request.GET.get('cmsTaskId')
    cmsTask = CMSTask.objects.filter(cmsTaskId=cmsTaskId).first()
    if cmsTask is not None and (not cmsTask.cmsTaskStatus == CMSTaskStatus.CREATED):
        return HttpResponse('waitting')
    cmsTask.cmsTaskStatus = CMSTaskStatus.WORKING
    CMSTask.save(cmsTask)
    print(cmsTask)
    print('cmsTaskId:', cmsTaskId)
    cmsFiles = CMSFile.objects.filter(cmsTaskId=cmsTaskId).first()
    print('cmsFile', cmsFiles)
    print('cmsFilePath', cmsFiles.cmsFilePath)
    docNameList, similarity = similar(cmsFiles.cmsFilePath)

    print(docNameList)
    print(similarity)
    cmsResult = {
        'docNameList': docNameList,
        'similarity': similarity
    }
    cmsResultMYSQL = CMSResult.create(cmsTaskId=cmsTaskId, cmsResultInfo='redis')
    cmsResultMYSQL.save()
    cmsResultID = cmsResultMYSQL.cmsResultId
    cmsResultJSON = json.dumps(cmsResult)
    insert_one(cmsTaskId=cmsTaskId, cmsResultINFO=cmsResultJSON)
    cmsTask.cmsTaskStatus = CMSTaskStatus.FINISHED

    CMSTask.save(cmsTask)
    del_file(cmsFiles.cmsFilePath)
    CMSFile.objects.filter(cmsTaskId=cmsTaskId).update(cmsFileStatus=CMSFileStatus.DELETE)
    return HttpResponse('success')
