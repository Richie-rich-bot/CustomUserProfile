from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.

class CustomUserProfileManager(BaseUserManager):
    def create_user(self, email, password = None, **extra_fields):
        if not email:
                raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)



class CustomUserProfile(AbstractBaseUser,PermissionsMixin):
    Username = models.CharField(max_length = 255,blank = True, null = False)
    email = models.EmailField(unique = True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) 
    
    objects= CustomUserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email