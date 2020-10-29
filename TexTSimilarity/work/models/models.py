import json

from django.db import models


class CMSFile(models.Model):
    cmsFileId = models.AutoField(primary_key=True)
    cmsFileName = models.CharField(max_length=64)
    cmsFilePath = models.CharField(max_length=128)
    cmsTaskId = models.IntegerField()
    cmsFileStatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cmsFile'

    @classmethod
    def create(cls, cmsFileName, cmsFilePath, cmsTaskId, cmsFileStatus):
        cmsFile = cls(cmsFileName=cmsFileName, cmsFilePath=cmsFilePath, cmsTaskId=cmsTaskId,
                      cmsFileStatus=cmsFileStatus)
        return cmsFile

    def __str__(self):
        _res_str = list()
        for field in self._meta.fields:
            _res_str.append({str(field.column): str(self.__getattribute__(field.column))})
        return json.dumps(_res_str, indent=2)  # 非json打印格式，去掉indent参数


class CMSResult(models.Model):
    cmsResultId = models.AutoField(primary_key=True)
    cmsTaskId = models.IntegerField()
    cmsResultInfo = models.CharField(max_length=1024)

    @classmethod
    def create(cls, cmsTaskId, cmsResultInfo):
        cmsResult = cls(cmsTaskId=cmsTaskId, cmsResultInfo=cmsResultInfo)
        return cmsResult

    class Meta:
        managed = False
        db_table = 'cmsResult'

    def __str__(self):
        _res_str = list()
        for field in self._meta.fields:
            _res_str.append({str(field.column): str(self.__getattribute__(field.column))})
        return json.dumps(_res_str, indent=2)  # 非json打印格式，去掉indent参数


class CMSTask(models.Model):
    cmsTaskId = models.AutoField(primary_key=True)
    cmsTaskName = models.CharField(max_length=50)
    cmsTaskStart = models.DateTimeField(auto_now=True)
    cmsTaskFinish = models.DateTimeField(null=True)
    cmsTaskStatus = models.IntegerField()

    @classmethod
    def create(cls, cmsTaskName, cmsTaskStatus):
        cmsResult = cls(cmsTaskName=cmsTaskName,
                        cmsTaskStatus=cmsTaskStatus)
        return cmsResult

    class Meta:
        managed = False
        db_table = 'cmsTask'

    def __str__(self):
        _res_str = list()
        for field in self._meta.fields:
            _res_str.append({str(field.column): str(self.__getattribute__(field.column))})
        return json.dumps(_res_str, indent=2)  # 非json打印格式，去掉indent参数
