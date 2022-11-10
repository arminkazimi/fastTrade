from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        MANAGER = "MANAGER", 'Manager'
        STAFF = "STAFF", 'Staff'
        USER = "USER", 'User'

    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(_('E-mail address'), unique=True)
    # first_name =
    base_role = Role.USER
    # role = models.CharField
