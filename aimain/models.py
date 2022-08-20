from django.db import models
from django.db.models.fields import TextField


# Create your models here.

#Every model must be class

# Django web applications access and manage data through Python objects referred to as models

class Aisource(models.Model): #database creation
    source=models.CharField(max_length=64)
    destination=models.CharField(max_length=64)
    #for character we use the CharField
    #for Integer we use the IntegerField
    
    def __str__(self):
        return f"{self.id}: {self.source }  to  {self.destination }"

class Type(models.Model):
    automated_Mode=models.CharField(max_length=3)
    manual_Mode=models.CharField(max_length=3)
    def __str__(self):
        if(self.automated_Mode=="Yes"):
            return f" Automated Mode:  {self.automated_Mode}"

        else:
            return f" Manual Mode:  {self.manual_Mode}"



class motioncontrol(models.Model):
    sensor=models.CharField(max_length=3)
    camera=models.CharField(max_length=3)
    radar=models.CharField(max_length=3)
    sonar=models.CharField(max_length=3)

    def __str__(self):
        return f" Sensor -> {self.sensor},Camera -> {self.camera},Radar -> {self.radar},Sonar -> {self.sonar}"