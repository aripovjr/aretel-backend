from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'fullname', 'is_admin', 'is_staff', 'is_active', 'is_superadmin')
    list_filter = ('is_admin', 'is_staff', 'is_active', 'is_superadmin')
    search_fields = ('phone_number', 'fullname')