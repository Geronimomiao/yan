# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     serializers
   Description :
   Author :       wsm
   date：          2019-02-25
-------------------------------------------------
   Change Activity:
                   2019-02-25:
-------------------------------------------------
"""
__author__ = 'wsm'

from rest_framework import serializers
from .models import PlanTable

class PlanTableSerializers(serializers.ModelSerializer):
    class Meta:
        model = PlanTable
        fields = "__all__"

