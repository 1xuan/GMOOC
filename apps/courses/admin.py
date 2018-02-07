from django.contrib import admin

# Register your models here.

from .models import Course, CourseResource, Lesson, Video

admin.site.register([CourseResource, Course, Lesson, Video])
