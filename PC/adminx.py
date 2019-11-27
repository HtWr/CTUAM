from .models import PC

import xadmin


# Register your models here.



class PCxadmin(object):
    # fields = ['host_name', 'wks_assets_num']
    fieldsets = [
        ('WKS', {'fields': ['host_name']}),
        ('Assets', {'fields': ['wks_assets_num']}),
        ('User', {'fields': ['user_name']}),
    ]
    list_display = ('host_name', 'wks_assets_num', 'user_name')
    # 在面板中显示过滤选项
    list_filter = ['host_name']
    # 在顶部显示基于题目的搜索栏
    search_fields = ['host_name', 'user_name', 'wks_assets_num']


xadmin.site.register(PC, PCxadmin)