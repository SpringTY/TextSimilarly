# 任务状态表 Map
import enum


class CMSTaskStatus(enum.IntEnum):
    """
    cmsTaskStatus = {
        0: '创建，未运行',
        1: '判断中',
        2: '已完成'
    }
    """
    CREATED = 0
    WORKING = 1
    FINISHED = 2


class CMSFileStatus(enum.IntEnum):
    """
    ON_DISK 未删除
    DELETE 已删除
    """
    ON_DISK = 0
    DELETE = 1


FILE_PATH_PREFIX = 'upload_files/'
