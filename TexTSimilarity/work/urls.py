"""TexTSimilarity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TexTSimilarity.work.views import router, fileView
from .views import taskView, resultView

urlpatterns = [
    path('', router.index, name='index_base'),
    path('admin/', admin.site.urls),
    path('index/', router.index, name='index'),
    path('textFiles/', fileView.textFiles, name='upload'),
    path('mysqlTest/', fileView.mysqlTest, name='mysqlTest'),
    path('tasks/', taskView.tasks, name='tasks'),
    path('files/', fileView.files, name='files'),
    path('upload/', fileView.upload, name='upload'),
    path('run/task', taskView.runTask, name='runTask'),
    path('result', router.result, name='result'),
    path('resultInfo', resultView.resultInfo, name='resultInfo'),
]
