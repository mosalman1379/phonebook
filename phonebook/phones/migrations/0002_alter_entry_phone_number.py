# Generated by Django 3.2.5 on 2021-07-05 13:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='phone_number',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='invalid pone number', regex='$09[0-9]{9,}')]),
        ),
    ]
