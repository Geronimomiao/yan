# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     serializers
   Description :
   Author :       wsm
   date：          2019-02-28
-------------------------------------------------
   Change Activity:
                   2019-02-28:
-------------------------------------------------
"""
__author__ = 'wsm'

from rest_framework import serializers
from .models import UserChatRecord

class UserChatRecordSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserChatRecord
        fields = "__all__"
