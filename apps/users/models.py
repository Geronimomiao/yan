from django.db import models

# Create your models here.

class UserProfile(models.Model):
    uuid = models.CharField(max_length=40, verbose_name='Access Token', null=True, blank=True)
    nick_name = models.CharField(max_length=20, verbose_name='昵称', null=True, blank=True)
    gender = models.CharField(choices=(('male', '男'), ('female', '女')), default='female', max_length=6)
    email = models.CharField(max_length=30, verbose_name='邮箱', null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name='电话', null=True, blank=True)
    password = models.CharField(max_length=40, verbose_name='密码', null=True, blank=True)
    student_card_url_front = models.CharField(max_length=100, verbose_name='学生证正面', null=True, blank=True)
    student_card_url_back = models.CharField(max_length=100, verbose_name='学生证反面', null=True, blank=True)
    avatar = models.CharField(max_length=100, verbose_name='用户头像', default='http://wsmpage.cn/reddot/2f9c84d4-67b4-4de2-a991-620466b73ccd')
    school = models.CharField(max_length=30, verbose_name='学校',  default='')
    city = models.CharField(max_length=30, verbose_name='城市',  default='')
    state = models.CharField(choices=(('1', '研究生'), ('0', '本科生')), default='0', max_length=6)
    # 该字段仅针对 研究生 level 搜索页面的推荐结果 越靠前
    level = models.CharField(choices=(('1', 'level_1'), ('2', 'level_2'), ('3', 'level_3'), ('4', 'level_4'),
                                      ('5', 'level_5'), ('6', 'level_6'), ('7', 'level_7')), default='1', max_length=6)

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nick_name

