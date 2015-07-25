from django.db import models

class MasterTable(models.Model):
    cl = models.IntegerField(blank=True)
    esda = models.CharField(blank=True, max_length=20)
    contract = models.IntegerField(blank=True)
    first_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    street_address = models.CharField(blank=True, max_length=100)
    city = models.CharField(blank=True, max_length=50)
    state =models.CharField(blank=True, max_length=2)
    zipcode = models.IntegerField(blank=True)
    extend_zip = models.IntegerField(blank=True)
    country = models.CharField(max_length=3, default='U')
    us_county = models.IntegerField(blank=True)
    is_male = models.BooleanField(blank=True)
