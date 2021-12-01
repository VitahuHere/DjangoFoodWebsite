# Generated by Django 3.2.9 on 2021-11-06 22:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0004_alter_person_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='height',
            field=models.PositiveIntegerField(default=None, validators=[django.core.validators.MaxValueValidator(999),
                                                                        django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='person',
            name='weight',
            field=models.DecimalField(decimal_places=1, default=None, max_digits=5,
                                      validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
