from django.db import models

# Create your models here.
class user(models.Model):
    id = models.AutoField(primary_key=True)
    test = models.CharField(max_length=10)
    win= models.IntegerField(default=10)
     
        

