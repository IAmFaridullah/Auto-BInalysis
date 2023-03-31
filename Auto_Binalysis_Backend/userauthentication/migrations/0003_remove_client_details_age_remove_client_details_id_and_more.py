# Generated by Django 4.1.7 on 2023-03-12 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauthentication', '0002_remove_client_details_age_remove_client_details_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client_details',
            name='age',
        ),
        migrations.RemoveField(
            model_name='client_details',
            name='id',
        ),
        migrations.RemoveField(
            model_name='client_details',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='client_details',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='client_details',
            name='name',
        ),
        migrations.AddField(
            model_name='client_details',
            name='account_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='client_details',
            name='client_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='client_details',
            name='org_city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='client_details',
            name='org_country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='client_details',
            name='org_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='client_details',
            name='username',
            field=models.CharField(default='1', max_length=100, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='client_details',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
    ]