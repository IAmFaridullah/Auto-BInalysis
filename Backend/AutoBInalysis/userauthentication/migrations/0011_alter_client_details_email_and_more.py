# Generated by Django 4.1.5 on 2023-01-12 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauthentication', '0010_clients_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_details',
            name='Email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='client_details',
            name='Org_Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterModelTable(
            name='client_details',
            table='client_details',
        ),
        migrations.AlterModelTable(
            name='clients_login',
            table='clients_login',
        ),
    ]