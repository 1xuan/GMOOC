__author__ = 'yixuan'
__date__ = ' 下午3:30'

from django.conf.urls import url, include
from .views import OrgView, AddUserAskView


urlpatterns = [
    # 机构列表页
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name="add_ask")
]