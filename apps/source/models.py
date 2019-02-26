from datetime import datetime

from django.db import models

from users.models import UserProfile
# Create your models here.

class RecommendBook(models.Model):
    name = models.CharField(max_length=100, verbose_name='推荐书籍/笔记名称', null=True, blank=True)
    cover_url = models.CharField(max_length=100, verbose_name='推荐书籍/笔记封面图', null=True, blank=True)
    text_url = models.CharField(max_length=100, verbose_name='内容链接', null=True, blank=True)
    state = models.CharField(choices=(('1', '笔记'), ('0', '书')), default='0', max_length=6)
    upload_user = models.ForeignKey(UserProfile, verbose_name=u'上传用户', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = '推荐书籍/笔记'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class RecommendVideo(models.Model):
    name = models.CharField(max_length=100, verbose_name='推荐视频名称', null=True, blank=True)
    cover_url = models.CharField(max_length=100, verbose_name='推荐视频资料', null=True, blank=True)
    text_url = models.CharField(max_length=100, verbose_name='内容链接', null=True, blank=True)
    state = models.CharField(max_length=10, verbose_name='所属类别', null=True, blank=True)
    upload_user = models.ForeignKey(UserProfile, verbose_name=u'上传用户', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = '推荐视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class PlanTable(models.Model):
    '''
      计划表
    '''
    create_user = models.ForeignKey(UserProfile, to_field='phone', verbose_name='创建用户', help_text='创建者的手机号', on_delete=models.CASCADE, null=True, blank=True)
    first = models.CharField(max_length=100, verbose_name='第一项', null=True, blank=True)
    second = models.CharField(max_length=100, verbose_name='第二项', null=True, blank=True)
    third = models.CharField(max_length=100, verbose_name='第三项', null=True, blank=True)
    fourth = models.CharField(max_length=100, verbose_name='第四项', null=True, blank=True)
    fifth = models.CharField(max_length=100, verbose_name='第五项', null=True, blank=True)
    sixth = models.CharField(max_length=100, verbose_name='第六项', null=True, blank=True)
    state1 = models.CharField(choices=(('1', '完成'), ('0', '未完成')), default='0', max_length=6, verbose_name='第一项完成状况')
    state2 = models.CharField(choices=(('1', '完成'), ('0', '未完成')), default='0', max_length=6, verbose_name='第二项完成状况')
    state3 = models.CharField(choices=(('1', '完成'), ('0', '未完成')), default='0', max_length=6, verbose_name='第三项完成状况')
    state4 = models.CharField(choices=(('1', '完成'), ('0', '未完成')), default='0', max_length=6, verbose_name='第四项完成状况')
    state5 = models.CharField(choices=(('1', '完成'), ('0', '未完成')), default='0', max_length=6, verbose_name='第五项完成状况')
    state6 = models.CharField(choices=(('1', '完成'), ('0', '未完成')), default='0', max_length=6, verbose_name='第六项完成状况')
    type = models.CharField(choices=(('1', '周计划'), ('0', '日计划')), default='0', max_length=6, verbose_name='计划类别')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '计划表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.create_user.nick_name + '添加完成'


class UserRecord(models.Model):
    '''
      考研路 对应的表
    '''
    create_user = models.ForeignKey(UserProfile, to_field='phone', verbose_name='创建用户', help_text='创建者的手机号',
                                    on_delete=models.CASCADE, null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    title = models.CharField(max_length=100, verbose_name='标题', null=True, blank=True)
    text = models.TextField(verbose_name='内容', null=True, blank=True)

    class Meta:
        verbose_name = '考研路'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.create_user.nick_name + '添加完成'


class UserExperience(models.Model):
    create_user = models.ForeignKey(UserProfile, to_field='phone', verbose_name='创建用户', help_text='创建者的手机号',
                                    on_delete=models.CASCADE, null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    title = models.CharField(max_length=100, verbose_name='标题', null=True, blank=True)
    text = models.TextField(verbose_name='内容', null=True, blank=True)
    img1_url = models.CharField(max_length=150, verbose_name='用户心得/吐槽配图1', null=True, blank=True)
    img2_url = models.CharField(max_length=150, verbose_name='用户心得/吐槽配图2', null=True, blank=True)
    img3_url = models.CharField(max_length=150, verbose_name='用户心得/吐槽配图3', null=True, blank=True)
    type = models.CharField(choices=(('1', '心得'), ('0', '吐槽')), default='0', max_length=6, verbose_name='发表类型')

    class Meta:
        verbose_name = '心得/吐槽'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.create_user.nick_name + '添加完成'