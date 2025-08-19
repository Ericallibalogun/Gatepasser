from django.contrib import admin
from .models import User, House
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = [ "first_name", "last_name","email",'username','phone','is_resident']


    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2","email","first_name","last_name","phone"),
            },
        ),
    )
    @admin.register(House)
    class HouseAdmin(admin.ModelAdmin):
        list_display = ["house_number","address"]