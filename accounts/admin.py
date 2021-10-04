from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth.models import Group

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('phone','nickname','email','is_verify','is_superuser','is_admin','is_staff',)
    list_filter = ('is_admin','is_staff',)
    fieldsets = (
        (None, {'fields': ('phone','nickname','first_name','last_name','email', 'password', 'image', 'bio')}),
        ('Personal info', {'fields': ('is_active',)}),
        ('Permissions', {'fields': ('is_verify', 'is_superuser','is_admin','is_staff',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'nickname','password1', 'password2'),
        }),
    )
    search_fields = ('phone','email',)
    ordering = ('phone',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)