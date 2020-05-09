from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import Role

UserModel = get_user_model()

# Register the User model
admin.site.register(UserModel, UserAdmin)


# Custom AdminSite
class AdminSite(admin.AdminSite):
    admin.AdminSite.site_header = 'MONOKU'
    admin.AdminSite.site_title = admin.AdminSite.site_header


@admin.register(Role)
class AdminRole(admin.ModelAdmin):
    list_display = ('name', )
    list_display_link = ('name', )
    search_fields = ('name', )
    list_filter = ('name', )
