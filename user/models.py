from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    last_date_of_payment = models.DateTimeField(null = True)
    slot = models.IntegerField(null = True)


class Payments(models.Model):
    user = models.ForeignKey(User,on_delete = models.PROTECT)
    amount = models.IntegerField()
    transaction_id = models.CharField(max_length=50)
    date_of_payment = models.DateTimeField()
    slot = models.IntegerField()
