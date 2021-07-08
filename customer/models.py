from django.db import models


class CustomerInfo(models.Model):
    selected_date = models.DateField(db_column='selected_date', blank=True,null=True, auto_now_add=False)
    company_name = models.CharField(db_column='company_name', max_length=100, blank=True)
    full_name = models.CharField(db_column='full_name', max_length=200, blank=True)
    email_id = models.CharField(db_column='email_id', max_length=200, blank=True)
    address = models.CharField(db_column='address', max_length=200, blank=True)
    phone_number = models.CharField(db_column='phone_number', max_length=200, blank=True)
    postal_code = models.CharField(db_column='postal_code', max_length=200, blank=True)
    created_date = models.DateField(db_column='created_date', blank=True, null=True, auto_now_add=True)

class VehicleInfo(models.Model):
    Auto = 'Auto'
    Standard = 'Standard'
    STATUS = (
        (Auto, 'Auto'),
        (Standard, 'Standard')
    )
    year = models.CharField(db_column='year', max_length=100, blank=True)
    brand = models.CharField(db_column='brand', max_length=200, blank=True)
    brand_model = models.CharField(db_column='brand_model', max_length=200, blank=True)
    odo_meter = models.CharField(db_column='odo_meter', max_length=200, blank=True)
    lic_plate = models.CharField(db_column='lic_plate', max_length=200, blank=True)
    gvwr = models.CharField(db_column='gvwr', max_length=200, blank=True)
    vin = models.CharField(db_column='vin', max_length=200, blank=True)
    engine = models.CharField(db_column='engine', max_length=200, blank=True)
    cylinder = models.CharField(db_column='cylinder', max_length=200, blank=True)
    Transmission = models.CharField(db_column='Transmission', max_length=10, choices=STATUS, blank=True)
    customer_id = models.ForeignKey(CustomerInfo, db_column='customer_id', null=True, on_delete=models.PROTECT)
    created_date = models.DateField(db_column='created_date', blank=True, null=True, auto_now_add=True)


class TestDetails(models.Model):
    selected_date = models.DateField(db_column='selected_date', blank=True,null=True, auto_now_add=False)
    vehicle_id = models.ForeignKey(VehicleInfo, db_column='customer_id', null=True, on_delete=models.PROTECT)
