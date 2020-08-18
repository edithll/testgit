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

from django.shortcuts import render


# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
from home_application.models import HostModel


def home(request):
    """
    首页
    """
    return render(request, 'home_application/index_home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render(request, 'home_application/dev_guide.html')


def contact(request):
    """
    联系页
    """
    return render(request, 'home_application/contact.html')


def index(request):
    """
    会议管理系统
    """
    return render(request, 'home_application/index.html')


def host_data(requset):
    if requset.method == 'POST':
        host_theme = requset.POST.get('hosttheme',None)
        host_venue = requset.POST.get('hostvenue',None)
        host_content = requset.POST.get('hostcontent',None)

        if ""in[host_theme,host_venue,host_content]:
            return render_json({'code':-1,'msg':'some of params lost.'})

        try:
            HostModel.objects.create(主题=host_theme,地点=host_venue,内容=host_content)
        except Exception as e:
            return render_json({'code':-1,'msg':'exists same host_theme and host_content pair.'})

        return render_json({'code':0,'msg':'data insert success.'})
    else:
        return render({'code':0,'items':HostModel.objects.to_dict(),
                       'catalogues':{
                           'host_theme':'主题',
                           'host_venue':'地点',
                           'host_content':'内容',
                       }})