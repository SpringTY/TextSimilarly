from django.core import serializers
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.views.decorators.http import require_POST, require_GET
from TexTSimilarity.work.models.models import CMSFile, CMSTask, CMSResult
from django.core.files.storage import default_storage


@require_POST
def textFiles(request):
    if request.FILES is not None:
        for i in request.FILES:
            my_file = request.FILES[i]
            print(my_file.name)
    else:
        print("None")
    return HttpResponse('ok')


@require_GET
def mysqlTest(request):
    objects_all = CMSResult.objects.all()
    print(objects_all)
    serialize = serializers.serialize("json", objects_all)
    return HttpResponse(serialize)


@require_GET
def files(request):
    cms_file = CMSFile.objects.all()
    cms_file_json = serializers.serialize("json", cms_file)
    return HttpResponse(cms_file_json)

'''
 明天需要把结果写入数据库,还需要搞一搞分析结果
'''
@require_POST
def upload(request):
    if request.FILES is not None:
        for my_file in request.FILES.getlist('cmsfile'):
            print('upload_files/' + my_file.name)
            default_storage.save('upload_files/' + my_file.name, ContentFile(my_file.read()))
    else:
        print("None")
    return HttpResponse('ok')
