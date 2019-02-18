# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     adminx
   Description :
   Author :       wsm
   date：          2019-02-16
-------------------------------------------------
   Change Activity:
                   2019-02-16:
-------------------------------------------------
"""
__author__ = 'wsm'

import xadmin
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '一路考研管理系统'
    site_footer = '一路考研'
    menu_style = "accordion"


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
