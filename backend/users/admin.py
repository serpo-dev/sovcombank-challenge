from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserChangeForm, CustomUserCreationForm
from users.models import User, Document


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'phone', 'is_staff', 'is_active', 'is_verified')
    list_filter = ('email', 'phone', 'is_staff', 'is_active', 'is_verified')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'phone')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_verified')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'password1', 'password2', 'is_staff', 'is_active', 'is_verified')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('serial', 'number', 'user_id')
