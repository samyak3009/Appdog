from calendar import prmonth
from operator import truediv
from pyexpat import model
from venv import create
from django.db import models
import datetime
import uuid
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager



# Create your models here.

    # 1. Name of dog
    # 2. Age of dog
    # 3. Gender
    # 4. Breed 
    # 5. Size
    # 6. Bio (about me(dog)) 
    # 7. Location should be taken from phone or if they type it, should be accurate
    # 8. Profile pictures—4 images


class BaseModel(models.Model):
    # universally unique identifiers
    uuid = models.UUIDField(primary_key=True,default = uuid.uuid4,editable = False)
    # updates the value with the time and date of creation of record.
    created_at  = models.DateTimeField(auto_now_add=True)
    # updates the value of field to current time and date every time the Model.save() is called.
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel,AbstractBaseUser,PermissionsMixin):

    dog_name = models.CharField(max_length=254,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True) 
    gender = models.CharField(max_length=100,null=True,blank=True)
    breed = models.CharField(max_length=254,null=True,blank=True)
    size = models.IntegerField(null=True,blank=True) 
    Bio = models.TextField(null=True,blank=True)
    location = models.CharField(max_length=255,null=True,blank=True)
    # is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=100)
    mobile = models.BigIntegerField(unique=True,null =True)
    
    objects = UserManager()
    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []


    class Meta:
        db_table='user'

