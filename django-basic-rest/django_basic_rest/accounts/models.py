from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): 
    email = models.EmailField(
        "email",
        max_length=254,
        unique=True,
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )