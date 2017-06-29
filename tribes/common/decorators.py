# !-*- encoding=utf-8 -*-
"""
    common.decorators.py
    ~~~~~~~~~~~~~~~~~~

    应用程序中的所有装饰器

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""

from threading import Thread


def singleton(cls):
    """单例模式装饰器"""
    instances = {}
    from functools import wraps

    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance


def async(f):
    """异步任务"""
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper
