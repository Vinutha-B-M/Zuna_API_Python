# Generated by Django 3.2.5 on 2021-07-07 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, db_column='full_name', max_length=200)),
                ('username', models.CharField(blank=True, db_column='username', max_length=200)),
                ('password', models.CharField(blank=True, db_column='password', max_length=100)),
            ],
        ),
    ]
