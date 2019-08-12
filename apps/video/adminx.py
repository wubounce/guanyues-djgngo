import xadmin
from .models import Video

class VideoAdmin(object):
    list_display = ['product_series','product','name','url','video','video_times','add_time']
    search_fields = ['product_series__name','product__name','name',] #product__name 外键中的name
    # list_filter = ['name','video_times','add_time']


xadmin.site.register(Video,VideoAdmin)