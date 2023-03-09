from django.db import models


# Create your models here.
class admindb(models.Model):
    Name = models.CharField(max_length=100,blank=True,null=True)
    Email = models.CharField(max_length=100, blank=True, null=True)
    Password = models.CharField(max_length=100, blank=True, null=True)
    Confirm = models.CharField(max_length=100, blank=True, null=True)
    Image = models.ImageField(upload_to="media", blank=True, null=True)

class catdb(models.Model):
    Category = models.CharField(max_length=100,blank=True,null=True)
    Description = models.CharField(max_length=100, blank=True, null=True)
    Image = models.ImageField(upload_to="media", blank=True, null=True)

class breeddb(models.Model):
    Breed = models.CharField(max_length=100, blank=True, null=True)
    Description = models.CharField(max_length=100, blank=True, null=True)
    Category = models.CharField(max_length=100, blank=True, null=True)
    Image = models.ImageField(upload_to="media", blank=True, null=True)
    Distributer = models.CharField(max_length=100, blank=True, null=True)
    Dinfo = models.CharField(max_length=100, blank=True, null=True)


class fooddb(models.Model):
    Food = models.CharField(max_length=100, blank=True, null=True)
    Price = models.IntegerField(blank=True, null=True)
    Description = models.CharField(max_length=100, blank=True, null=True)
    Category = models.CharField(max_length=100,blank=True,null=True)
    Image = models.ImageField(upload_to="media", blank=True, null=True)


class contactdb(models.Model):
    Name = models.CharField(max_length=100, blank=True, null=True)
    Email = models.EmailField(max_length=100, blank=True, null=True)
    Subject = models.CharField(max_length=100,blank=True,null=True)
    Message = models.CharField(max_length=100,blank=True,null=True)


class disrtibuterdb(models.Model):
    Name = models.CharField(max_length=100, blank=True, null=True)
    Address = models.CharField(max_length=100, blank=True, null=True)
    Mobile = models.CharField(max_length=100, blank=True, null=True)
    Category = models.CharField(max_length=100, blank=True, null=True)
    Image = models.ImageField(upload_to="media", blank=True, null=True)



class cartdb(models.Model):
    Food = models.CharField(max_length=50, null=True, blank=True)
    Category = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)



class checkout(models.Model):
    Fname = models.CharField(max_length=50, null=True, blank=True)
    Lname = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100,null=True, blank=True)
    Address = models.CharField(max_length=100,null=True, blank=True)
    Country = models.CharField(max_length=100,null=True, blank=True)
    State = models.CharField(max_length=100,null=True, blank=True)
    Pin = models.IntegerField(null=True, blank=True)
    Food = models.CharField(max_length=100,null=True, blank=True)
    Pin = models.IntegerField(null=True, blank=True)
    #-------------Payment-------------#
    NOC = models.CharField(max_length=100, null=True, blank=True)
    CCN = models.IntegerField(null=True, blank=True)
    Expiration = models.CharField(max_length=100,null=True, blank=True)
    CVV = models.IntegerField(null=True, blank=True)




