from django.db import models
from django.conf import settings

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length = 180)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    completed = models.BooleanField(default = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.task


class Note(models.Model):
    text = models.TextField(max_length=512, blank=False, null=False)
    TYPE_CHOICES = (
        ('warning', 'Warning'),
        ('info', 'Information'),
        ('do_before', 'Do before'),
    )
    type = models.CharField(choices=TYPE_CHOICES, default='warning', max_length=15)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, null=False, blank=False)