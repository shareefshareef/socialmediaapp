from django.db import models
from django.contrib.auth.models import User



class Tweets(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    topic = models.CharField(max_length=50,null=False,blank=False)
    tweet = models.CharField(max_length=250,null=False,blank=False)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.topic

