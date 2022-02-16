from django.db import models
import uuid

# Create your models here.

class userData(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    user_id=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    
    

    
