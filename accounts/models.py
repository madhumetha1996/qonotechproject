from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    # Add custom fields or methods as needed
    groups = models.ManyToManyField(Group, related_name='accounts_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='accounts_users', blank=True)
