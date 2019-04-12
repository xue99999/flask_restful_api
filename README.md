# 简介
用flask框架改写的flask restful api风格的框架

# 如何把用到的python包导出到txt文件
```python
pip freeze > requirements.txt
```

# flask-sqlalchemy 查询分页
```
    Thing.query.filter_by(uid=uid).paginate(page=page, per_page=10)
```
items 当前页面中的所有记录(比如当前页上有5条记录，items就是以列表形式组织这5个记录)
query 当前页的query对象(通过query对象调用paginate方法获得的Pagination对象)
page 当前页码(比如当前页是第5页，返回5)
total 一共有多少条数据

```
{
    'query': <app.models.base.Query object at 0x04720DF0>, 
    'page': 1, 
    'per_page': 10, 
    'total': 12, 
    'items': [<Thing 1>, <Thing 2>, <Thing 3>, <Thing 4>, <Thing 13>, <Thing 15>, <Thing 18>, <Thing 22>, <Thing 28>, <Thing 29>]
}
```
