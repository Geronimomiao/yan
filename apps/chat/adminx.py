# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     adminx
   Description :
   Author :       wsm
   date：          2019-02-28
-------------------------------------------------
   Change Activity:
                   2019-02-28:
-------------------------------------------------
"""
__author__ = 'wsm'
import xadmin

from .models import UserChatRecord


class UserChatRecordAdmin(object):
    pass


xadmin.site.register(UserChatRecord, UserChatRecordAdmin)