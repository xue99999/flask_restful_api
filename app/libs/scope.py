class Scope:
    # scope 支持整个module 注册
    allow_api = []
    allow_module = []
    forbidden = []

    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))

        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))

        return self


class AdminScope(Scope):
    allow_module = ['v1.user', 'v1.book', 'v1.gift', 'v1.token', 'v1.thing']

    def __init__(self):
        pass


class UserScope(Scope):
    forbidden = ['v1.user+super_get_user']

    def __init__(self):
        self + AdminScope()


# 暂时用不到，做实验的
class SuperScope(Scope):
    allow_api = ['v1.C']

    def __init__(self):
        self + UserScope() + AdminScope()


def is_in_scope(scope, endpoint):
    # 从字符串 转换成 类 java里面叫反射
    # globals()
    # v1.view_func  v1.module + view_func
    # v1.red_name + view_func
    scope = globals()[scope]()
    splits = endpoint.split('+')
    red_name = splits[0]

    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_module:
        return True
    else:
        return False
