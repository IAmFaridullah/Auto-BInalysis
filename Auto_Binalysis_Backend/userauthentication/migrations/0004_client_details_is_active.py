# Generated by Django 4.1.7 on 2023-03-12 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauthentication', '0003_remove_client_details_age_remove_client_details_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_details',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
