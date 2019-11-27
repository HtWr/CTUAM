from django.contrib import admin

from .models import PC

import xadmin


# Register your models here.
# 原生admin系统

class PCAdmin(admin.ModelAdmin):
    # fields = ['host_name', 'wks_assets_num']
    fieldsets = [
        ('WKS', {'fields': ['host_name']}),
        ('Assets', {'fields': ['wks_assets_num']}),
    ]
    list_display = ('host_name', 'wks_assets_num')
    # 在面板中显示过滤选项
    list_filter = ['host_name']
    # 在顶部显示基于题目的搜索栏
    search_fields = ['host_name']





admin.site.register(PC, PCAdmin)

