# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     csrf
   Description :
   Author :       wsm
   date：          2019-02-25
-------------------------------------------------
   Change Activity:
                   2019-02-25:
-------------------------------------------------
"""
__author__ = 'wsm'

from rest_framework.authentication import SessionAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return