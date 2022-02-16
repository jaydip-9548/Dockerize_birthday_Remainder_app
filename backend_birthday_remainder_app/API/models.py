from django.db import models
from API_SignIn_Up.models import userData
import uuid
# Create your models here.
class remainderData(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    quota = models.CharField(max_length=1000)
    user_id=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    # photoName = models.ImageField(upload_to='myImage',max_length=100,blank=True)

    