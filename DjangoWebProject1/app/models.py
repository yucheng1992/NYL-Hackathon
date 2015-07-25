from django.db import models
from pyzipcode import ZipCodeDatabase
import pandas as pd
import random

def load_data(fileName='table.xls'):
    for row in pd.read_excel(fileName).iterrows():
        customer = MasterTable(
                    cl=row[1]['CL_ID'],
                    esda=row[1]['ESDA_ALTERNATE_PRODUCT_CD'],
                    contract=row[1]['CMR_CONTRACT_ID'],
                    first_name=row[1]['FIRST_NAME'],
                    last_name=row[1]['LAST_NAME'],
                    street_address=row[1]['STR_ONE_AD'],
                    city=row[1]['CTY_AD'],
                    state=row[1]['STATE_CD'],
                    zipcode=int(row[1]['ZIP']),
                    extend_zip=int(row[1]['EXTND_ZIP_CD']),
                    country=row[1]['CNTRY_CD'],
                    us_county=int(row[1]['US_CNTY_CD']),
                    is_male=True if row[1]['GENDER_CD'] == 'M' else False,
                    )
        customer.save()

class MasterTable(models.Model):
    cl = models.IntegerField(blank=True, null=True)
    esda = models.CharField(blank=True, max_length=20)
    contract = models.CharField(blank=True, max_length=20)
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

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
