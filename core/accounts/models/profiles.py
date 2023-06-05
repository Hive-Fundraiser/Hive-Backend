from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User for our app.
    """
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=20)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is_verified = models.CharField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    def __str__(self):
        return self.email