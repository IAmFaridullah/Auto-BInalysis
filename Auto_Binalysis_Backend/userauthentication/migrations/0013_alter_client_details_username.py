# Generated by Django 4.1.7 on 2023-05-01 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauthentication', '0012_alter_client_details_account_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_details',
            name='username',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]