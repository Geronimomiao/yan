# Generated by Django 2.1.7 on 2019-02-25 21:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190225_1608'),
        ('source', '0009_auto_20190225_2046'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='标题')),
                ('text', models.TextField(blank=True, null=True, verbose_name='内容')),
                ('img1_url', models.CharField(blank=True, max_length=150, null=True, verbose_name='用户心得配图1')),
                ('img2_url', models.CharField(blank=True, max_length=150, null=True, verbose_name='用户心得配图2')),
                ('img3_url', models.CharField(blank=True, max_length=150, null=True, verbose_name='用户心得配图3')),
                ('type', models.CharField(choices=[('1', '心得'), ('0', '吐槽')], default='0', max_length=6, verbose_name='发表类型')),
                ('create_user', models.ForeignKey(blank=True, help_text='创建者的手机号', null=True, on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile', to_field='phone', verbose_name='创建用户')),
            ],
            options={
                'verbose_name': '心得/吐槽',
                'verbose_name_plural': '心得/吐槽',
            },
        ),
    ]
