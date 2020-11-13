from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.http import require_POST, require_GET
from TexTSimilarity.work.models.models import CMSFile, CMSTask, CMSResult
from TexTSimilarity.work.service.taskService import runTaskService
from TexTSimilarity.work.similarCalc.similarCalc import similar
from TexTSimilarity.work.utils.constValues import CMSTaskStatus, CMSFileStatus
from TexTSimilarity.work.redisTemplate import insert_one, query
from TexTSimilarity.work.utils.fileUtils import del_file
import json


@require_GET
def tasks(request):
    """
    获取所有任务
    :param request: GET请求
    :return: json化的 cmsTasks 实体
    """
    cms_tasks = CMSTask.objects.all().order_by('cmsTaskId')
    cms_tasks_json = serializers.serialize("json", cms_tasks)
    return HttpResponse(cms_tasks_json)


@require_GET
def runTask(request):
    """
    运行任务
    :param request: GET请求,带有参数cmsTaskId
    :return:
    """
    cmsTaskId = request.GET.get('cmsTaskId')
    response = runTaskService(cmsTaskId)
    return HttpResponse(response)
