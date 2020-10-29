from django.core import serializers
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.views.decorators.http import require_POST, require_GET
from TexTSimilarity.work.models.models import CMSFile, CMSTask, CMSResult
from django.core.files.storage import default_storage
from TexTSimilarity.work.utils.constValues import *


@require_GET
def textFiles(request):
    cmsFile = CMSFile.create('name', 'path', 1, 1)
    cmsFile.save()
    print(cmsFile.cmsFileId)
    return HttpResponse('ok')


@require_GET
def mysqlTest(request):
    objects_all = CMSResult.objects.all()
    print(objects_all)
    serialize = serializers.serialize("json", objects_all)
    return HttpResponse(serialize)


@require_GET
def files(request):
    cmsFile = CMSFile.objects.all()
    cmsFileJSON = serializers.serialize("json", cmsFile)
    return HttpResponse(cmsFileJSON)


@require_POST
def upload(request):
    if request.FILES is not None:
        cmsTaskName = request.POST.get('cmsTaskName')

        cmsTask = CMSTask.create(cmsTaskName=cmsTaskName, cmsTaskStatus=CMSTaskStatus.CREATED)
        cmsTask.save()
        cmsTaskId = cmsTask.cmsTaskId
        cmsTaskStart = cmsTask.cmsTaskStart

        for cmsRequestFile in request.FILES.getlist('cmsFile'):
            cmsFilePath = FILE_PATH_PREFIX + str(cmsTaskStart.strftime('%Y-%m-%d-%H-%M-%S')) + '/'
            print(cmsFilePath)
            default_storage.save(cmsFilePath + cmsRequestFile.name, ContentFile(cmsRequestFile.read()))
            cmsFile = CMSFile.create(cmsFileName=cmsRequestFile.name, cmsFilePath=cmsFilePath, cmsTaskId=cmsTaskId,
                                     cmsFileStatus=CMSFileStatus.ON_DISK)
            cmsFile.save()
        responseMSG = 'success'
    else:
        responseMSG = 'failed'
    return HttpResponse(responseMSG)
