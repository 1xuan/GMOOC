__author__ = 'yixuan'
__date__ = ' 下午10:11'

from django.conf.urls import url, include

from .views import UserinfoView

urlpatterns = [
    # 用户信息
    url(r'^info/$', UserinfoView.as_view(), name='user_info'),


]