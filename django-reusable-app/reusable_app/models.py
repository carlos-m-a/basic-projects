from django.db import models
from django.conf import settings

# Create your models here.
class MyModel(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name='mymodel'
    )
    name = models.CharField(max_length=50, blank=False, null=False, default="name example")
    text = models.CharField(max_length=200, blank=False, null=False, default="text example")

    def __str__(self):
        return self.task