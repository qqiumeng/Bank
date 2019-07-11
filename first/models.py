from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=16)
    money = models.FloatField(default=0)
    card_num = models.IntegerField(default=0)



