from django.db import models


class CMSFile(models.Model):
    cmsFileId = models.IntegerField(primary_key=True)
    cmsFileName = models.CharField(max_length=64)
    cmsFilePath = models.CharField(max_length=128)
    cmsTaskId = models.IntegerField()
    cmsFileStatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cmsFile'


class CMSResult(models.Model):
    cmsResultId = models.IntegerField(primary_key=True)
    cmsTaskId = models.IntegerField()
    cmsResultInfo = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'cmsResult'


class CMSTask(models.Model):
    cmsTaskId = models.IntegerField(primary_key=True)
    cmsTaskName = models.CharField(max_length=50)
    cmsTaskStart = models.DateTimeField()
    cmsTaskFinish = models.DateTimeField()
    cmsTaskStatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cmsTask'
