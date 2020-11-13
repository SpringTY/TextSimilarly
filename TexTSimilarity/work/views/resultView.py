from django.core import serializers
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.views.decorators.http import require_POST, require_GET
from TexTSimilarity.work.models.models import CMSFile, CMSTask, CMSResult
from django.core.files.storage import default_storage
from TexTSimilarity.work.utils.constValues import *
from TexTSimilarity.work.redisTemplate import query

'''
接收结果的ajax请求
'''


def resultInfo(request):
    """
    :param request: GET请求,带有cmsTaskId参数
    :return: 根据cmsTaskId获取对应的结果返回
    """
    cmsTaskId = request.GET.get('cmsTaskId')
    cmsResultInfo = query(cmsTaskId)
    return HttpResponse(cmsResultInfo)
