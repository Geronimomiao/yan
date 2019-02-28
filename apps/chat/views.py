
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import UserChatRecord
from .serializers import UserChatRecordSerializers
# Create your views here.

class UserChatRecordView(APIView):

    def get(self, request):
        r_phone = request.GET.get('r_phone')
        s_phone = request.GET.get('s_phone')
        type = request.GET.get('type')
        if r_phone and type:
            '''
              查询 此手机号所有 未读/已读 接收消息
            '''
            chats = UserChatRecord.objects.filter(r_phone=r_phone, type=type)
            data = UserChatRecordSerializers(chats, many=True)
        elif r_phone:
            '''
              查询 此手机号所有接收消息
            '''
            chats = UserChatRecord.objects.filter(r_phone=r_phone)
            data = UserChatRecordSerializers(chats, many=True)
        elif s_phone and r_phone:
            '''
              查询 s_phone 向 r_phone 所有发送消息
            '''
            chats = UserChatRecord.objects.filter(s_phone=s_phone, r_phone=r_phone)
            data = UserChatRecordSerializers(chats, many=True)

        return Response(data.data)


class UserChatRecordViewset(viewsets.ModelViewSet):

    queryset = UserChatRecord.objects.all()
    serializer_class = UserChatRecordSerializers