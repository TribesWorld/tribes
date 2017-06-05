# !-*- encoding=utf-8 -*-
"""
    tribes.tribes
    ~~~~~~~~~~~~~~~~~~

    应用程序的主入口，继承自common.service模块，主要作用是组装多个应用，并做一些全局上的配置

    :copyright: (c) YEAR by v-zhidu.
    :license: LICENSE_NAME, see LICENSE_FILE
"""

from common.app import App
from services import users, auth


class Tribes(App):
    """
    Tribes类

    用于创建Flask实例

    Public Attributes
         : instance Flask实例
    """

    def register_component(self, app, **kwargs):
        """覆盖common.service模块中的默认注册方法，组合项目中不同的服务
        """

        super(Tribes, self).register_component(app, **kwargs)


# 必须在实例Tribes之前导入资源文件

app = Tribes(use_db=True).instance

app.register_blueprint(users)
app.register_blueprint(auth)
