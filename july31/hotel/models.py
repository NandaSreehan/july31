from django.db import models
class menu(models.Model):
    dishname=models.CharField(max_length=20)
    price=models.IntegerField()

def __str__(self):
    return self.name