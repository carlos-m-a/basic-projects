from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar_image = models.ImageField(upload_to='images/', null=True, blank=True, max_length=254)
    bio_text = models.TextField(blank=True, max_length=254)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username