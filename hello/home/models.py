from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=112)
    email = models.CharField(max_length=112)
    phone = models.CharField(max_length=112)
    message = models.TextField()
    date = models.DateField()
# Create your models here.

    def __str__(self):
        return self.name

class Services(models.Model):
    flavour = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    message = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.flavour
    
    
    
    
    