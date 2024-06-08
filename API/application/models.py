from django.db import models

# Create your models here.


class products(models.Model):
      pid = models.IntegerField()
      pname = models.CharField(max_length=255)
      price = models.FloatField()
      company = models.CharField(max_length=255)
      m_date = models.DateField()
      E_date = models.DateField()
