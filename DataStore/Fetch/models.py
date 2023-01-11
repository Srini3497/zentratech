from django.db import models

# Create your models here.
class PageData(models.Model):
    url   = models.URLField(max_length=500)
    desc  = models.CharField(max_length=300)
    price = models.FloatField()
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)

