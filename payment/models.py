from django.db import models
from service.models import ServicesList
from customer.models import VehicleInfo
from users.models import UserType, UserInfo


# Create your models here.


class PaymentEntry(models.Model):
    Pending = 'Pending'
    Completed = 'Completed'
    Cancelled = 'cancelled'
    STATUS = (
        (Pending, 'Pending'),
        (Completed, 'Completed'),
        (Cancelled, 'cancelled')
    )
    Cash = 'Cash'
    Card = 'Card'
    Other = 'Other'
    MODE = (
        (Cash, 'Cash'),
        (Card, 'Card'),
        (Other, 'Other')
    )
    final_amount = models.FloatField(db_column='final_amount', max_length=200, blank=True, null=True)
    # invoice_no = models.CharField(db_column='invoice_no', max_length=200, blank=True)
    tax_offered = models.FloatField(db_column='tax_offered', max_length=200, blank=True, null=True)
    amount_tendered = models.FloatField(db_column='amount_tendered', max_length=200, blank=True, null=True)
    changed_given = models.FloatField(db_column='changed_given', max_length=200, blank=True, null=True)
    discount_offered = models.FloatField(db_column='discount_offered', max_length=200, blank=True, null=True)
    payment_mode = models.CharField(db_column='payment_mode', max_length=10, choices=MODE, blank=True)
    status = models.CharField(db_column='status', max_length=10, choices=STATUS, blank=True)
    Vehicle = models.ForeignKey(VehicleInfo, db_column='Vehicle', null=True, on_delete=models.PROTECT)
    created_date = models.DateField(db_column='created_date', blank=True, null=True, auto_now_add=True)
    modified_date = models.DateField(db_column='modified_date', blank=True, null=True, auto_now_add=True)


class InvoiceItem(models.Model):
    service_item = models.ForeignKey(ServicesList, db_column='service_item', null=True, on_delete=models.PROTECT)
    service_name = models.CharField(db_column='service_name', blank=True, max_length=100)
    amount = models.FloatField(db_column='amount', blank=True, max_length=100, null=True)
    Payment = models.ForeignKey(PaymentEntry, db_column='payment', null=True, on_delete=models.PROTECT)

#
# class SquareTerminal(models.Model):
#     square_token = models.CharField(db_column="token", max_length=200, blank=True)
#     expires_at = models.CharField(db_column="expires_at", max_length=200, blank=True)
#     merchant_id = models.CharField(db_column="merchant_id", max_length=200, blank=True)
#     refresh_token = models.CharField(db_column="refresh_token", max_length=200, blank=True)
#     client = models.ForeignKey(UserInfo, db_column='client', null=True, on_delete=models.PROTECT)
#
#
# class SquareDevice(models.Model):
#     device_id = models.CharField(db_column="device", max_length=100, blank=True)
#     name = models.CharField(db_column="name_device", max_length=100, blank=True)
#     code = models.CharField(db_column="code", max_length=100, blank=True)
#     location = models.CharField(db_column="location", max_length=100, blank=True)
#     status = models.CharField(db_column="status", max_length=100, blank=True)
#     client = models.ForeignKey(UserInfo, db_column='client', null=True, on_delete=models.PROTECT)
