from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser): 
    email = models.EmailField(
        _("email"),
        max_length=254,
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar_image = models.ImageField(upload_to='images/', null=True, blank=True, max_length=254)
    bio_text = models.TextField(blank=True, max_length=254)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username