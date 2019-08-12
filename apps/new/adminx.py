import xadmin
from .models import News

class NewsAdmin(object):
    list_display = ['title','desc','detail','add_time']
    search_fields = ['title','desc','detail']
    list_filter = ['title','desc','detail','add_time']
    style_fields = {'detail': 'ueditor'}


xadmin.site.register(News,NewsAdmin)