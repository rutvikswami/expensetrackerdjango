from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Expense(models.Model):
    item = models.CharField(max_length = 50)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.name