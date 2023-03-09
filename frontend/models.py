from django.db import models

# Create your models here.


class savelogindb(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Password = models.IntegerField(null=True, blank=True)
    Confirm = models.IntegerField( null=True, blank=True)
