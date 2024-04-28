from django.db import models
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
# Create your models here.
class User:
    userID = models.AutoField(primary_key=True)
    fullName = models.CharField()
    gender = models.CharField()
    status = models.BooleanField()
    passwordHash =  models.CharField()
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True)
