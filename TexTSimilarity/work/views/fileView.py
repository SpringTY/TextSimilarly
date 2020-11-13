from django.core import serializers
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.views.decorators.http import require_POST, require_GET
from TexTSimilarity.work.models.models import CMSFile, CMSTask, CMSResult
from django.core.files.storage import default_storage
from TexTSimilarity.work.utils.constValues import *
from django.shortcuts import render


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
    """
    批量上传文件并生成任务
    :param request:
    :return:
    """
    if request.FILES is not None:
        # 获取任务名
        cmsTaskName = request.POST.get('cmsTaskName')
        # 生成新的任务
        cmsTask = CMSTask.create(cmsTaskName=cmsTaskName, cmsTaskStatus=CMSTaskStatus.CREATED)
        cmsTask.save()
        # 获取生成的任务信息
        cmsTaskId = cmsTask.cmsTaskId
        cmsTaskStart = cmsTask.cmsTaskStart
        # 处理每一个文件
        for cmsRequestFile in request.FILES.getlist('cmsFile'):
            cmsFilePath = FILE_PATH_PREFIX + str(cmsTaskStart.strftime('%Y-%m-%d-%H-%M-%S')) + '/'
            print(cmsFilePath)
            default_storage.save(cmsFilePath + cmsRequestFile.name, ContentFile(cmsRequestFile.read()))
            cmsFile = CMSFile.create(cmsFileName=cmsRequestFile.name, cmsFilePath=cmsFilePath, cmsTaskId=cmsTaskId,
                                     cmsFileStatus=CMSFileStatus.ON_DISK)
            cmsFile.save()
        responseMSG = render(request, 'index.html')
    else:
        responseMSG = HttpResponse('failed')
    return responseMSG
