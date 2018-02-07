from django.contrib import admin

# Register your models here.

from .models import UserProfile, EmailVerifyRecord, Banner


class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ('name', )


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register([EmailVerifyRecord, Banner])


