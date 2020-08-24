# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2020 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""


# Create your models here.

from django.db import models
#在读取django模型时调用models函数


#首先,定义一个Manager的子类
class HostModelManager(models.Manager):
    #提交
    def get_save(self,data):
    #在自定义管理器中定义一个方法创建对象
        try:
            HostModel.objects.create(
                theme=data.get('theme'),
                time=data.get('time'),
                venue=data.get('venue'),
                content=data.get('content'),
            )
            result = {'result': True, 'message': u"保存成功"}
        except Exception as e:
            result = {'result': False, 'message': u"保存失败, %s" % e}
        return result
# 然后,将它显式地插入到HostModel模型中
class HostModel(models.Model):
    theme = models.CharField(u"主题", max_length=30)
    time = models.DateTimeField(u"时间", max_length=30)
    venue = models.CharField(u"地点", max_length=30)
    content = models.TextField(u"内容", null=True, blank=True)
    objects = HostModelManager()

    def __unicode__(self):
        return self.theme

    class Meta:
        #改变数据库库名
        db_table = 'meeting'
        #在admin页面上的名字#
        verbose_name = u"meeting"
        verbose_name_plural = u"meeting"
