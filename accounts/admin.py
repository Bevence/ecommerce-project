from django.contrib import admin
from accounts.models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class AccountManager(UserAdmin):
    list_display = ['first_name', 'last_name', 'username', 'email', 'last_login', 'is_active', 'is_admin']
    list_display_links = ['first_name', 'last_name', 'username', 'email', 'last_login']
    list_editable = ['is_active']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountManager)
