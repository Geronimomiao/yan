import json

from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.core import serializers
from django.views.generic.base import View
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from source.models import RecommendBook, RecommendVideo, PlanTable, UserRecord, UserExperience
from users.models import UserProfile
from .serializers import PlanTableSerializers, UserRecordSerializers, UserExperienceSerializers
# Create your views here.

class SourceRecommendBookView(View):

    def get(self, request):
        books = RecommendBook.objects.all()
        data = serializers.serialize('json', books)

        return HttpResponse(data, content_type='application/json')

    def post(self, request):
        name = request.POST.get('name', '')
        if RecommendBook.objects.filter(name=name):
            res = {
                'StatusCode': 103,
                'detail': '已存在同名书/笔记'
            }
            return HttpResponse(json.dumps(res), content_type="application/json")

        book = RecommendBook()
        book.name = request.POST.get('name', '')
        book.cover_url = request.POST.get('cover_url', '')
        book.text_url = request.POST.get('text_url', '')
        book.state = request.POST.get('state', '0')
        # book.upload_user = request.POST.get('upload_user')
        phone = request.POST.get('phone')
        if phone:
            book.upload_user = UserProfile.objects.get(phone=phone)

        book.save()
        res = {
            'StatusCode': 200,
            'detail': '添加成功'
        }
        return HttpResponse(json.dumps(res), content_type="application/json")


class SourceRecommendVideoView(View):

    def get(self, request):
        videos = RecommendVideo.objects.all()
        data = serializers.serialize('json', videos)

        return HttpResponse(data, content_type='application/json')

    def post(self, request):
        name = request.POST.get('name', '')
        if RecommendVideo.objects.filter(name=name):
            res = {
                'StatusCode': 103,
                'detail': '已存在同名视频'
            }
            return HttpResponse(json.dumps(res), content_type="application/json")

        video = RecommendVideo()
        video.name = request.POST.get('name', '')
        video.cover_url = request.POST.get('cover_url', '')
        video.text_url = request.POST.get('text_url', '')
        video.state = request.POST.get('state', '')
        phone = request.POST.get('phone')
        if phone:
            video.upload_user = UserProfile.objects.get(phone=phone)

        video.save()
        res = {
            'StatusCode': 200,
            'detail': '添加成功'
        }
        return HttpResponse(json.dumps(res), content_type="application/json")


class PlanTableView(APIView):

    def get(self, request):
        phone = request.GET.get('phone')
        plans = PlanTable.objects.filter(create_user=phone)
        data = PlanTableSerializers(plans, many=True)

        return Response(data.data)


class PlanTableViewset(viewsets.ModelViewSet):

    queryset = PlanTable.objects.all()
    serializer_class = PlanTableSerializers


class UserRecordView(APIView):

    def get(self, request):
        phone = request.GET.get('phone')
        plans = UserRecord.objects.filter(create_user=phone)
        data = UserRecordSerializers(plans, many=True)

        return Response(data.data)


class UserRecordViewset(viewsets.ModelViewSet):

    queryset = UserRecord.objects.all()
    serializer_class = UserRecordSerializers


class UserExperienceView(APIView):

    def get(self, request):
        phone = request.GET.get('phone', '')
        type = request.GET.get('type', '')

        if phone and type:
            plans = UserExperience.objects.filter(create_user=phone, type=type)
            data = UserExperienceSerializers(plans, many=True)
        elif type:
            plans = UserExperience.objects.filter(type=type)
            data = UserExperienceSerializers(plans, many=True)

        return Response(data.data)


class UserExperienceViewset(viewsets.ModelViewSet):

    queryset = UserExperience.objects.all()
    serializer_class = UserExperienceSerializers





