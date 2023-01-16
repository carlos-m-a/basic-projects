from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings

class User(AbstractUser): 
    email = models.EmailField(
        _("email address"),
        max_length=254,
        unique=True,
        error_messages={
            "unique": "A user with that email already exists.",
        },
        blank=False,
        null=False
    )


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=False, 
        related_name='profile'
    )
    avatar_image = models.ImageField(
        upload_to='images/', 
        null=True, 
        blank=True, 
        max_length=254
    )
    bio_text = models.TextField(
        blank=True, 
        max_length=254, 
        null=True
    )
    date_of_birth = models.DateField(
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.user.username


class Setting(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=False, 
        related_name='setting'
    )
    activated_email_notifications = models.BooleanField(
        null=False, 
        default=False
    )
    language = models.SmallIntegerField(
        null=False, 
        default=1
    )

    def __str__(self):
        return self.user.username