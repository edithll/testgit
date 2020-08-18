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

# from django.db import models

# Create your models here.

class HostModelManager(models.Manager):
    def to_dict(self):
        qs = super().get_queryset()
        res_dict = [{
            'host_theme':item.theme,
            'host_venue':item.venue,
            'host_content':item.content,
        } for item in qs ]
        return res_dict

class HostModel(models.Model):
    theme = models,CharField(max_length=30,verbose_name='主题')
    venue = models,CharField(max_length=30,verbose_name='地点')
    content = models.CharField(max_length=200,verbose_name='内容')

    objects = HostModelManager()
