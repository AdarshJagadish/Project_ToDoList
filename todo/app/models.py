from django.db import models

# Create your models here.
class lists(models.Model):
    tasks=models.TextField()
    date=models.DateField(auto_now_add=True,null=True)