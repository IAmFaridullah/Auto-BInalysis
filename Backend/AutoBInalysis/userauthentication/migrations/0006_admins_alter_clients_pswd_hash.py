# Generated by Django 4.1.5 on 2023-01-12 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauthentication', '0005_clients_delete_clients_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='admins',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('Admin_Username', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('Admin_PswdHash', models.CharField(max_length=100)),
                ('Admin_Name', models.CharField(max_length=100)),
                ('Admin_Gender', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'admins',
            },
        ),
        migrations.AlterField(
            model_name='clients',
            name='Pswd_Hash',
            field=models.CharField(max_length=100),
        ),
    ]
