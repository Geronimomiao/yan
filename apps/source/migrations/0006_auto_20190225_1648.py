# Generated by Django 2.1.7 on 2019-02-25 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0005_auto_20190225_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantable',
            name='uuid',
        ),
        migrations.AlterField(
            model_name='plantable',
            name='create_user',
            field=models.ForeignKey(blank=True, help_text='创建者的手机号', null=True, on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile', to_field='phone', verbose_name='创建用户'),
        ),
    ]
