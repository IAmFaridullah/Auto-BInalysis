# Generated by Django 4.1.7 on 2023-04-16 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauthentication', '0010_rename_username_client_details_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_details',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]