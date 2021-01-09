from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Cart(models.Model):
    user_id = models.IntegerField()
    products =ArrayField(models.CharField(max_length=100),default=None)



