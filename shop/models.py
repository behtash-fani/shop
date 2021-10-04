from django.db import models


class MainCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    maincategory = models.ForeignKey(MainCategory, related_name='subcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=150,null=True, blank=True, unique=True)
    slug = models.SlugField(max_length=150, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'

class Product(models.Model):
    maincategory = models.ForeignKey(MainCategory, on_delete=models.CASCADE, null=True)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE, blank=True, null=True)
    name  = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    description = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    specifications = models.TextField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    stock = models.IntegerField(null=True, blank=True)
    available = models.BooleanField(default=True)
    shipping = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def price_after_set_discount(self):
        calculate_set_discount = (self.price*self.discount)/100
        total_price = self.price - calculate_set_discount
        return total_price

