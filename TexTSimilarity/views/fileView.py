from django.http import HttpResponse
from django.views.decorators.http import require_POST


@require_POST
def textFiles(request):
    if request.FILES is not None:
        for i in request.FILES:
            my_file = request.FILES[i]
            print(my_file.name)
    else:
        print("None")
    return HttpResponse('ok')
