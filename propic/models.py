from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class AccountImages(models.Model):
    iuser = models.ForeignKey(User,on_delete=models.CASCADE)
    iimage = models.ImageField(upload_to="folderpropics")
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)
