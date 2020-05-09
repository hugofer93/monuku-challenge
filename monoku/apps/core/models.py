from django.contrib.auth.models import AbstractUser
from django.db import models


# To modify the roles, if required.
class Role(models.Model):
    """
    Class for handling roles and user permissions
    """
    ADMIN = 'admin'
    READER = 'reader'
    EDITOR = 'editor'

    ROLE_CHOICES = (
        (ADMIN, 'admin'),
        (READER, 'reader'),
        (EDITOR, 'editor')
    )

    name = models.CharField(max_length=15, unique=True, choices=ROLE_CHOICES)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()


# Custom User Model
class User(AbstractUser):
    """
    Custom user model inherits from AbstractUser.

    """
    role = models.ManyToManyField(Role)
