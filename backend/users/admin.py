from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User, Document


# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "is_verified", 'is_active')


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('serial', 'number', 'user')
