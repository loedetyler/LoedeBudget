from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    account = models.CharField(max_length=100, null=False)
    exclude = ["owner"]

    def __str__(self):
        return self.name
