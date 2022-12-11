from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password, **other_fields):
        if not phone_number:
            raise ValueError(_('You must provide an phone number'))

        user = self.model(phone_number=phone_number, password=password, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned: is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned: is_superuser=True.')
        return self.create_user(phone_number, password, **other_fields)


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        MANAGER = "MANAGER", 'Manager'
        STAFF = "STAFF", 'Staff'
        USER = "USER", 'User'

    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(_('E-mail address'), unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return str(self.phone_number)
    # base_role = Role.USER
    # # role = models.CharField
