# Generated by Django 3.2.9 on 2021-11-10 16:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_person_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='weight',
            field=models.DecimalField(decimal_places=1, default=None, max_digits=4, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]