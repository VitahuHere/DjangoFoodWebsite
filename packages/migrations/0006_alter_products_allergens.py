# Generated by Django 3.2.9 on 2021-12-05 23:12

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0005_alter_products_allergens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='allergens',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=None), blank=True, null=True, size=None),
        ),
    ]
