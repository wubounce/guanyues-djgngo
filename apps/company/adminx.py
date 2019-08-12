import xadmin
from xadmin import views
from .models import Company,Banner

class CompanyAdmin(object):
    list_display = ['mobile','telephone','address','desc','company_intro','company_website']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time'] # 显示列表表格的列
    search_fields = ['title', 'image', 'url', 'index']# 显示列表搜索
    list_filter = ['title', 'image', 'url', 'index', 'add_time']# 显示列表筛选


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "东莞市冠粤自动化科技有限公司"
    site_footer = "冠粤自动化"
    menu_style = "accordion" #设置左侧菜单收起

xadmin.site.register(Company,CompanyAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)