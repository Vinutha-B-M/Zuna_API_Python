# Generated by Django 3.2.5 on 2021-08-20 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_userinfo_company_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertype',
            name='image_name',
            field=models.CharField(blank=True, db_column='image_name', max_length=300),
        ),
    ]
