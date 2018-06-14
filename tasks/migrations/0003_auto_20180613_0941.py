# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-13 09:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_tools_toolsresults_variable'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tools',
            options={'permissions': set([('can_add_tools', '\u53ef\u4ee5\u6dfb\u52a0\u5de5\u5177'), ('can_change_tools', '\u53ef\u4ee5\u4fee\u6539\u5de5\u5177\u4fe1\u606f'), ('can_delete_tools', '\u53ef\u4ee5\u5220\u9664\u5de5\u5177'), ('can_view_tools', '\u53ef\u4ee5\u67e5\u770b\u5de5\u5177\u4fe1\u606f')]), 'verbose_name': '\u5de5\u5177', 'verbose_name_plural': '\u5de5\u5177'},
        ),
        migrations.AlterModelOptions(
            name='toolsresults',
            options={'permissions': set([('can_view_toolsresult', '\u53ef\u4ee5\u67e5\u770b\u4efb\u52a1\u7ed3\u679c')]), 'verbose_name': '\u4efb\u52a1\u7ed3\u679c', 'verbose_name_plural': '\u4efb\u52a1\u7ed3\u679c'},
        ),
        migrations.AlterModelOptions(
            name='variable',
            options={'permissions': set([('can_add_var', '\u53ef\u4ee5\u6dfb\u52a0\u53d8\u91cf'), ('can_change_var', '\u53ef\u4ee5\u4fee\u6539\u53d8\u91cf\u4fe1\u606f'), ('can_delete_var', '\u53ef\u4ee5\u5220\u9664\u53d8\u91cf'), ('can_view_var', '\u53ef\u4ee5\u67e5\u770b\u53d8\u91cf\u4fe1\u606f')]), 'verbose_name': '\u53d8\u91cf\u7ec4', 'verbose_name_plural': '\u53d8\u91cf\u7ec4'},
        ),
    ]
