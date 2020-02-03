from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=32)
    body = models.TextField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)