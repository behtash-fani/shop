from django.contrib import admin
from .models import WishList


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('user',)
    # list_display = ('user','name',)
    # prepopulated_fields = {'slug': ('user.username',)}
