from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager

class User_manager(BaseUserManager):
    def create_user(self, username, email, gender, nickname, password):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, gender=gender, nickname=nickname)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, gender, password, nickname=None):
        user = self.create_user(username=username, email=email, gender=gender, nickname=nickname, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user