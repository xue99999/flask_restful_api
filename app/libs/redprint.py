class Redprint:
    def __init__(self, name):
        self.name = name
        self.mound = []

    # route装饰器
    def route(self, rule, **options):
        def decorator(f):
            # 以元祖的形式写入列表
            self.mound.append((f, rule, options))
            return f
        return decorator

    def register(self, bp, url_prefix=None):
        if url_prefix is None:
            url_prefix = '/' + self.name
        for f, rule, options in self.mound:
            # 为什么修改? scope里面方便的管理module权限
            endpoint = self.name + '+' + options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)

