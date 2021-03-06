# Generated by Django 2.1.7 on 2019-02-21 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20190221_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='推荐书籍/笔记名称')),
                ('cover_url', models.CharField(blank=True, max_length=100, null=True, verbose_name='推荐书籍/笔记封面图')),
                ('text_url', models.CharField(blank=True, max_length=100, null=True, verbose_name='内容链接')),
                ('state', models.CharField(choices=[('1', '笔记'), ('0', '书')], default='0', max_length=6)),
                ('upload_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile', verbose_name='上传用户')),
            ],
            options={
                'verbose_name': '推荐书籍/笔记',
                'verbose_name_plural': '推荐书籍/笔记',
            },
        ),
        migrations.CreateModel(
            name='RecommendVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='推荐视频名称')),
                ('cover_url', models.CharField(blank=True, max_length=100, null=True, verbose_name='推荐视频资料')),
                ('text_url', models.CharField(blank=True, max_length=100, null=True, verbose_name='内容链接')),
                ('state', models.CharField(blank=True, max_length=10, null=True, verbose_name='所属类别')),
                ('upload_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile', verbose_name='上传用户')),
            ],
            options={
                'verbose_name': '推荐视频',
                'verbose_name_plural': '推荐视频',
            },
        ),
    ]
