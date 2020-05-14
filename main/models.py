from django.db import models
# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=100)
    desc= models.TextField()
    TeamSize= models.IntegerField(default=1)
    Event_Pics = models.ImageField(upload_to='event_pics')
class urd(models.Model):
    name=models.CharField(max_length=100)
    emailid=models.CharField(max_length=100)
    collegename=models.CharField(max_length=100)
    semester=models.IntegerField()
    mobilenum=models.CharField(max_length=100)
    events=models.CharField(max_length=100)