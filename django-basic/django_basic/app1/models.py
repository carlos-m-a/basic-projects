from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
# Create your models here.

User = get_user_model()


class OtherModel1(models.Model):
    name = models.CharField('Customer', max_length=50)

class OtherModel2(models.Model):
    name = models.CharField('Customer', max_length=50)

class MyModel(models.Model):
    name = models.CharField('Customer', max_length=120)
    small_int = models.PositiveSmallIntegerField()
    text = models.TextField(blank=True, null = True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    float_number = models.FloatField(null=True, blank=True)
    boolean_field = models.BooleanField(default=True)
    date = models.DateField(null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    file = models.FileField(upload_to='my-model-files/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Select Field (return value, display value)
    TYPE_CHOICES = (
        ('Customer', 'Customer'),
        ('Supplier', 'Supplier'),
        ('Student', 'Student'),
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=120)
    
    # RELATIONSHIPS
    
    # Many-to-One:
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    # Many-to-Many: 
    other_models_2 = models.ManyToManyField(OtherModel2, blank=True)

    # One to One 
    other_model_1 = models.OneToOneField(OtherModel1, on_delete=models.CASCADE, null=True, blank=True)

    
    def __str__(self):
        string = self.name
        string += ', int:'
        string += str(self.small_int)
        return string
