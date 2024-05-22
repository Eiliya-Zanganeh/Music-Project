from django.contrib import admin
from User_Module.models import *


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    ...


@admin.register(MusicModel)
class MusicAdmin(admin.ModelAdmin):
    ...


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['music', 'user', 'date']
