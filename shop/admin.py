from django.contrib import admin
from .models import MainCategory, Product, SubCategory




@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','maincategory')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','discount','available','shipping')
    list_filter = ('available', 'created')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('name',)}