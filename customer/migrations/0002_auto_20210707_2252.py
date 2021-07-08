# Generated by Django 3.2.5 on 2021-07-07 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerinfo',
            name='created_date',
            field=models.DateField(auto_now_add=True, db_column='created_date', null=True),
        ),
        migrations.AddField(
            model_name='customerinfo',
            name='selected_date',
            field=models.DateField(blank=True, db_column='selected_date', null=True),
        ),
        migrations.AddField(
            model_name='vehicleinfo',
            name='Transmission',
            field=models.CharField(blank=True, choices=[('Auto', 'Auto'), ('Standard', 'Standard')], db_column='Transmission', max_length=10),
        ),
        migrations.AddField(
            model_name='vehicleinfo',
            name='created_date',
            field=models.DateField(auto_now_add=True, db_column='created_date', null=True),
        ),
        migrations.AlterField(
            model_name='testdetails',
            name='selected_date',
            field=models.DateField(blank=True, db_column='selected_date', null=True),
        ),
    ]
