from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from off_campus_housing_app.models import CustomUser


class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)