from django.contrib import admin

# Register your models here.

from .models import UserAsk, UserCourse, UserFavorite, UserMessage, CourseComments

admin.site.register([UserMessage, UserFavorite, UserCourse, UserAsk, CourseComments])
