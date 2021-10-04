from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator
from .managers import UserManager



def get_user_image_folder(instance, filename):
    return "%s/%s" %(instance.phone, filename)


class User(AbstractBaseUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '9XX XXX XXXX'. Up to 15 digits allowed.")
    phone = models.CharField(max_length=17, validators=[phone_regex], unique=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    nickname = models.CharField(max_length=100, null=True, blank=True, unique=True)
    bio = models.TextField(null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to=get_user_image_folder, null=True, blank=True)
    
    is_verify = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['nickname',]

    def __str__(self):
        return self.phone
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True