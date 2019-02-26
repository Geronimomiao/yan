# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     adminx
   Description :
   Author :       wsm
   date：          2019-02-21
-------------------------------------------------
   Change Activity:
                   2019-02-21:
-------------------------------------------------
"""
__author__ = 'wsm'

import xadmin
from xadmin import views

from .models import RecommendBook, RecommendVideo, PlanTable, UserRecord, UserExperience

class RecommendBookAdmin(object):
    pass


class RecommendVideoAdmin(object):
    pass


class PlanTableAdmin(object):
    pass


class UserRecordAdmin(object):
    pass


class UserExperienceAdmin(object):
    pass


xadmin.site.register(RecommendBook, RecommendBookAdmin)
xadmin.site.register(RecommendVideo, RecommendVideoAdmin)
xadmin.site.register(PlanTable, PlanTableAdmin)
xadmin.site.register(UserRecord, UserRecordAdmin)
xadmin.site.register(UserExperience, UserExperienceAdmin)

