# Generated by Django 3.2.9 on 2021-11-29 13:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0008_alter_person_weight'),
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keys',
            name='client_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='keys',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False,
                                       to='accounts.person'),
        ),
    ]