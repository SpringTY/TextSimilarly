from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.http import require_POST, require_GET
from TexTSimilarity.work.models.models import CMSFile, CMSTask, CMSResult


@require_GET
def tasks(request):
    cms_tasks = CMSTask.objects.all()
    cms_tasks_json = serializers.serialize("json", cms_tasks)
    return HttpResponse(cms_tasks_json)
