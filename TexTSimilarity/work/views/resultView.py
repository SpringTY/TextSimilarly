from django.core import serializers
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.views.decorators.http import require_POST, require_GET
from TexTSimilarity.work.models.models import CMSFile, CMSTask, CMSResult
from django.core.files.storage import default_storage
from TexTSimilarity.work.utils.constValues import *
from TexTSimilarity.work.redisTemplate import query

def resultInfo(request):
    cmsTaskId = request.GET.get('cmsTaskId')
    print('test')
    cmsResultInfo = query(cmsTaskId)
    return HttpResponse(cmsResultInfo)
