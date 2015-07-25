from django.db import models

class MasterTable(models.Model):
    cl = models.IntegerField(blank=True)
    esda = models.CharField(blank=True)
    contract = models.IntegerField(blank=True)
    first_name = models.CharField(blank=True)
    last_name = models.CharField(blank=True)
    street_address = models.CharField(blank=True)
    city = models.CharField(blank=True)
    state =models.CharField(blank=True, max_length=2)
    zipcode = models.IntegerField(blank=True)
    extend_zip = models.IntegerField(blank=True)
    country = models.CharField(max_length=3, default='U')
    us_county = models.IntegerField(blank=True)
    is_male = BooleanField(blank=True, null=True)
