# Generated by Django 2.1.1 on 2018-12-09 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0004_auto_20181209_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trademanage',
            name='finishDate',
            field=models.CharField(default=None, max_length=8, verbose_name='完了日'),
        ),
        migrations.AlterField(
            model_name='trademanage',
            name='finishTime',
            field=models.CharField(default=None, max_length=12, verbose_name='完了時刻'),
        ),
    ]