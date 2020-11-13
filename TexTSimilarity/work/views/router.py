from django.shortcuts import render

from TexTSimilarity.work.models.models import CMSTask

'''
    页面路由
'''


def index(request):
    return render(request, 'index.html')


def result(request):
    cmsTaskId = request.GET.get('cmsTaskId')
    cmsTask = CMSTask.objects.filter(cmsTaskId=cmsTaskId).first()
    return render(request, 'result.html', {
        'cmsTaskId': cmsTaskId,
        'cmsTask': cmsTask
    })
