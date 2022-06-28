
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from ..manager import User_manager


class User(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(max_length=32, unique=True, )
    email = models.EmailField(max_length=32)
    
    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    
    gender_choices = [("M", "Male"), ("F", "Female"), ("O", "Others")]
    
    gender = models.CharField(choices=gender_choices, default="M", max_length=1)
    nickname = models.CharField(max_length=32, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    REQUIRED_FIELDS = ["email", "gender"]           # some required fields
    USERNAME_FIELD = "username"                     # need to login with username
    objects = User_manager()                        # passing user managet to manage the user creation

    # def __str__(self):
    #     return self.email

    def __str__(self):
        return (self.first_name + " " + self.last_name)