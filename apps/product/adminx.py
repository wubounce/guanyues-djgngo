import xadmin
from .models import ProductSeries, Product

class ProductSeriesAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name']
    list_filter = ['name', 'add_time']


class ProductAdmin(object):
    list_display = ['name', 'category', 'tag', 'desc', 'detail', 'add_time']
    search_fields = ['name', 'category', 'tag', 'desc', 'detail']
    list_filter = ['name', 'category', 'tag', 'desc', 'detail', 'add_time']
    style_fields = {'detail': 'ueditor'}


xadmin.site.register(ProductSeries,ProductSeriesAdmin)
xadmin.site.register(Product,ProductAdmin)