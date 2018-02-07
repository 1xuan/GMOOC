from django.contrib import admin

# Register your models here.

from .models import CityDict, CourseOrg, Teacher

admin.site.register([CourseOrg, CityDict, Teacher])
