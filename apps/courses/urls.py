__author__ = 'yixuan'
__date__ = ' 上午8:58'

from django.conf.urls import url, include
from .views import CourseListView, CourseDetailView

urlpatterns = [
    # 机构列表页
    url(r'^list/$', CourseListView.as_view(), name='course_list'),

    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),


]