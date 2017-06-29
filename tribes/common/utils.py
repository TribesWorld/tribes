# !-*- encoding=utf-8 -*-
"""
utility functions

"""


def import_module(dotted_path):
    """
    Imports the specified module based on the
    dot notated import path for the module.
    """
    import importlib

    module_parts = dotted_path.split('.')
    module_path = '.'.join(module_parts[:-1])
    module = importlib.import_module(module_path)

    return getattr(module, module_parts[-1])


def initialize_class(data, **kwargs):
    """
    :param data: A string or dictionary containing a import_path attribute.
    """
    if isinstance(data, dict):
        import_path = data.pop('import_path')
        data.update(kwargs)
        Class = import_module(import_path)

        return Class(**data)
    else:
        Class = import_module(data)

        return Class(**kwargs)


def encode_password(password):
    """计算密码散列"""
    from werkzeug.security import generate_password_hash

    return generate_password_hash(password)


def verify_password(password, password_hash):
    """验证密码正确性"""
    from werkzeug.security import check_password_hash

    return check_password_hash(password_hash, password)


def generate_avatar():
    """生成默认头像地址"""
    return "test_url"


def generate_token(data, secret_key, expires_in=3600):
    """生成确认令牌"""
    from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
    s = Serializer(secret_key, expires_in)
    return s.dumps(data)


def load_token(secret_key, token):
    """加载令牌"""
    from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
    s = Serializer(secret_key)

    return s.loads(token)
