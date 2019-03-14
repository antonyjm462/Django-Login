from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=50,primary_key=True)
    company_name  = models.CharField(max_length=40)