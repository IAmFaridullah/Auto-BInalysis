# Generated by Django 4.1.5 on 2023-01-12 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauthentication', '0004_clients_login_alter_client_details_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='clients',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('Username', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('Pswd_Hash', models.CharField(db_column='Pswd_Hash', max_length=100)),
                ('Client_Type', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'clients_login',
            },
        ),
        migrations.DeleteModel(
            name='clients_login',
        ),
    ]
