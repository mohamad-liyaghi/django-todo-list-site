from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    '''Manager for creating user'''

    def create_user(self, email, password, **kwargs):
        email = self.normalize_email(email)

        user = self.model(email= email, is_active=True, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        return  self.create_user(email=email, password= password,
                                 is_superuser= True, is_staff=True)



class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    username = None

    # telegram userid (for telegram service)
    telegram_id = models.IntegerField(blank=True, null=True)
    token = models.CharField(max_length=12,blank=True,null=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email