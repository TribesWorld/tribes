# !-*- encoding=utf-8 -*-
"""
    common.Database.py
    ~~~~~~~~~~~~~~~~~~

    数据库操作抽象类

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from enum import Enum
from flask_sqlalchemy import SQLAlchemy


def database(datasource, with_transaction=False):
    """数据库支持db"""
    if with_transaction:
        def _db(func):
            def wrapper(*args, **kwargs):
                try:
                    datasource.begin_transaction()
                    return func(*args, **kwargs)
                except Exception as ex:
                    datasource.abort_transaction()
                    raise ex
                finally:
                    datasource.end_transaction()
                    datasource.close()
            return wrapper
    else:
        def _db(func):
            def wrapper(*args, **kwargs):
                try:
                    datasource.connect()
                    return func(*args, **kwargs)
                except Exception as ex:
                    raise ex
                finally:
                    datasource.close()
            return wrapper
    return _db


class ConnectState(Enum):
    """
    数据库连接状态枚举值
    """
    PREPARED = -1,
    CLOSE = 0,
    OPENED = 1


def format_sql(sql, *args):
    """格式化sql语句"""
    if not isinstance(sql, str) or None:
        raise ValueError('query sentence must not be empty.')
    return sql.format(*args)


def _default_connect_handler():
    """开启或关闭连接是的处理方法"""
    pass


def _default_transcation_handler():
    """开启或关闭事务的默认处理方法"""
    pass


def _default_error_handler(error):
    """操作过程中的错误处理方法"""
    pass


def _default_execute_handler(sql):
    """执行sql语句"""
    pass


class Database(object):
    """
    数据库操作抽象类

    封装常用的查询方法

    Public Attributes
         An integer count of the eggs we have laid.
    """

    def __init__(self, database):
        if not isinstance(database, SQLAlchemy) or None:
            raise TypeError('database must be set by a SQLAlchemy object.')
        self._db = database
        self._conn = None
        self._trans = None
        self._conn_state = ConnectState.PREPARED

        # operation handler
        self._before_connect_handler = _default_connect_handler
        self._after_connect_handler = _default_connect_handler
        self._before_transcation_handler = _default_transcation_handler
        self._after_transcation_handler = _default_transcation_handler
        self._across_error_handler = _default_error_handler
        self._on_execute_sql_handler = _default_execute_handler

    def _execute(self, sql, *args):
        """执行sql语句"""
        from sqlalchemy.exc import SQLAlchemyError

        try:
            if not self._conn_state == ConnectState.OPENED:
                raise SQLAlchemyError('database connection is closed.')

            sql = format_sql(sql, *args)
            self._on_execute_sql_handler(sql)

            result = self._conn.execute(sql)
            return result
        except Exception as ex:
            self._across_error_handler(ex)
            raise ex

    def begin_transaction(self):
        """开启事务支持"""
        self._before_transcation_handler()
        self.connect()
        self._trans = self._conn.begin()

    def abort_transaction(self):
        """中断事务"""
        if self._trans is not None and self._trans.is_active:
            self._trans.rollback()

    def end_transaction(self):
        """提交事务"""
        self._after_transcation_handler()
        if self._trans is not None and self._trans.is_active:
            self._trans.commit()

    def execute(self, sql, *args):
        """执行sql语句"""
        result = self._execute(sql, *args)

        return self.process_result(result)

    def query(self, sql, *args):
        """查询方法"""
        result = self._execute(sql, *args)

        return self.process_result(result)

    def query_count(self, sql, *args):
        """查询数量使用"""
        result = self._execute(sql, *args)
        return result.first()[0]

    def query_one(self, sql, *args):
        """查询单行使用"""

        result = self.execute(sql, *args)
        if len(result) > 0:
            return result[0]
        else:
            return None

    def process_result(self, result):
        """
        : param ResultProxy
        """
        lis = []
        if result.returns_rows:
            for row in result:
                column = {}
                for key in result._metadata.keys:
                    column[key] = row[key]

                lis.append(column)

        return lis

    def connect(self):
        """开启数据库连接"""
        if not self._conn_state == ConnectState.OPENED:
            self._conn = self._db.engine.connect()
            self._before_connect_handler()
            self._conn_state = ConnectState.OPENED

    def close(self):
        """关闭数据库连接"""
        if self._conn_state == ConnectState.OPENED:
            self._conn.close()
            self._after_connect_handler()
            self._conn_state = ConnectState.CLOSE

    def before_connect(self, callback):
        """指定在开启连接前的操作

            @database.before_connect
            def before_connect():
                print 'b'
        """
        self._before_connect_handler = callback

        return callback

    def after_connect(self, callback):
        """指定在关闭连接前的操作

            @database.after_connect
            def after_connect():
                print 'c'
        """
        self._after_connect_handler = callback

        return callback

    def before_transcation(self, callback):
        """开启事务前的操作"""
        self._before_transcation_handler = callback

        return callback

    def after_transcation(self, callback):
        """结束事务前的操作"""
        self._after_transcation_handler = callback

        return callback

    def across_error(self, callback):
        """指定发生错误时的操作

            @database.across_error
            def across_error():
                print 'c'

        : param callback: the exception object.
        """
        self._across_error_handler = callback

        return callback

    def on_execute_sql(self, callback):
        """执行sql语句时的处理方法

            @database.on_execute_sql
            def on_execute_sql(sql):
                print sql
        """
        self._on_execute_sql_handler = callback

        return callback

    def init_db(self, script_folder=None):
        """初始化数据库"""
        if script_folder is None:
            return

        def _read_file(file_path):
            with open(file_path, 'r') as f:
                return f.read()

        def _file_generator(root_path):
            import os

            for file_name in os.listdir(root_path):
                if os.path.splitext(file_name)[1] == '.sql':
                    yield os.path.join(root_path, file_name)

        self.begin_transaction()
        for script in _file_generator(script_folder):
            sql = _read_file(script)
            if sql:
                self._execute(sql)
