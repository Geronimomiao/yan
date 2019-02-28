from datetime import datetime

from django.db import models

# Create your models here.

class UserChatRecord(models.Model):
    s_phone = models.CharField(max_length=100, verbose_name='发送者手机号', null=True, blank=True)
    s_nickname = models.CharField(max_length=100, verbose_name='发送者昵称', null=True, blank=True)
    r_phone = models.CharField(max_length=100, verbose_name='接收者手机号', null=True, blank=True)
    r_nickname = models.CharField(max_length=100, verbose_name='接收者昵称', null=True, blank=True)
    send_msg = models.TextField(verbose_name='发送信息', null=True, blank=True)
    type = models.CharField(choices=(('1', '未读'), ('0', '已读')), default='0', max_length=6, verbose_name='消息状态')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户聊天信息记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.s_phone + '添加完成'