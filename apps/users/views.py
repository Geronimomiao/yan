import json, uuid

from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.core import serializers
from django.views.generic.base import View
from django.db.models import Q
from django.http import QueryDict

from .models import UserProfile

# Create your views here.

class UserProfileListView(View):

    def get(self, request):
        users = UserProfile.objects.all().filter(state=1).order_by('-level')
        data = serializers.serialize('json', users, fields=('nick_name', 'gender', 'email', 'phone',
                                                            'avatar', 'school', 'city', 'level'))
        # return JsonResponse(json.dumps(data), safe=True)
        return HttpResponse(data, content_type='application/json')


class UserLoginView(View):

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = UserProfile.objects.filter(Q(email=username)|Q(phone=username))
        if user:
            user = UserProfile.objects.filter(Q(email=username)|Q(phone=username) , password=password)
            if user:
                data = serializers.serialize('json', user, fields=('nick_name', 'gender', 'email', 'phone',
                                                            'avatar', 'school', 'city', 'level', 'state'))
                response = HttpResponse(data, content_type="application/json")
                cookies = user.values('uuid')[0].get('uuid')
                response.set_cookie('AccessToken', cookies, max_age=259200)
                return response
            else:
                res = {
                    'StatusCode': 102,
                    'detail': '请检测密码是否正确'
                }
                return HttpResponse(json.dumps(res), content_type="application/json")
        else:
            res = {
                'StatusCode': 101,
                'detail': '请检测用户名是否正确'
            }
            return HttpResponse(json.dumps(res), content_type="application/json")


class UserLoginOutView(View):

    def get(self, request):
        response = HttpResponse()
        response.delete_cookie('AccessToken')
        return response


class UserCheckLoginView(View):

    def get(self, request):
        uuid = request.COOKIES.get('AccessToken')
        if uuid:
            user = UserProfile.objects.filter(uuid=uuid)
            if user:
                data = serializers.serialize('json', user, fields=('nick_name', 'gender', 'email', 'phone',
                                                                   'avatar', 'school', 'city', 'level', 'state'))
                return HttpResponse(data, content_type="application/json")
            else:
                res = {
                    'StatusCode': 102,
                    'detail': '用户未登录'
                }
                return HttpResponse(json.dumps(res), content_type="application/json")
        else:
            res = {
                'StatusCode': 101,
                'detail': '用户未登录'
            }
            return HttpResponse(json.dumps(res), content_type="application/json")


class UserRegisterView(View):

    def post(self, request):
        nick_name = request.POST.get('nick_name', '')
        gender = request.POST.get('gender', 'female')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        password = request.POST.get('password', '')
        student_card_url_front = request.POST.get('student_card_url_front', '')
        student_card_url_back = request.POST.get('student_card_url_back', '')
        avatar = request.POST.get('student_card_url_back', 'http://wsmpage.cn/reddot/2f9c84d4-67b4-4de2-a991-620466b73ccd')
        school = request.POST.get('school', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '0')


        if UserProfile.objects.filter(phone=phone):
            res = {
                'StatusCode': 103,
                'detail': '手机号已注册'
            }
            return HttpResponse(json.dumps(res), content_type="application/json")
        elif UserProfile.objects.filter(email=email):
            res = {
                'StatusCode': 103,
                'detail': '邮箱已注册'
            }
            return HttpResponse(json.dumps(res), content_type="application/json")
        else:
            user = UserProfile()
            user.uuid = uuid.uuid4().hex
            user.nick_name = nick_name
            user.gender = gender
            user.email = email
            user.phone = phone
            user.password = password
            user.student_card_url_front = student_card_url_front
            user.student_card_url_back = student_card_url_back
            user.avatar = avatar
            user.school = school
            user.city = city
            user.state = state
            user.save()
            res = {
                'StatusCode': 200,
                'detail': '注册成功'
            }
            return HttpResponse(json.dumps(res), content_type="application/json")


class UserUpdateView(View):

    def post(self, request, update_filed):
        uuid = request.COOKIES.get('AccessToken')
        if uuid:
            user = UserProfile.objects.get(uuid=uuid)
            if user:
                new_value = request.POST.get(update_filed)
                update_filed = update_filed
                setattr(user, update_filed, new_value)
                user.save()
                res = {
                    'StatusCode': 200,
                    'detail': '修改成功'
                }

                return HttpResponse(json.dumps(res), content_type="application/json")
            else:
                res = {
                    'StatusCode': 102,
                    'detail': '用户未登录'
                }
                return HttpResponse(json.dumps(res), content_type="application/json")
        else:
            res = {
                'StatusCode': 101,
                'detail': '用户未登录'
            }
            return HttpResponse(json.dumps(res), content_type="application/json")