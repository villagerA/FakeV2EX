# Generated by Django 2.0.2 on 2018-03-03 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0012_auto_20180303_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topicvote',
            name='favorite',
            field=models.CharField(default='-1', max_length=10, verbose_name='是否收藏此贴'),
        ),
        migrations.AlterField(
            model_name='topicvote',
            name='like',
            field=models.CharField(default='-1', max_length=10, verbose_name='是否喜欢此贴'),
        ),
        migrations.AlterField(
            model_name='topicvote',
            name='thanks',
            field=models.CharField(default='-1', max_length=10, verbose_name='是否感谢此贴'),
        ),
    ]