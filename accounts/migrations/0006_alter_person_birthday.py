# Generated by Django 3.2.9 on 2021-11-10 08:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0005_auto_20211106_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
