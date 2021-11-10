# Generated by Django 3.2.9 on 2021-11-06 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211101_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='id',
        ),
        migrations.AddField(
            model_name='person',
            name='login',
            field=models.CharField(default=None, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='surname',
            field=models.CharField(default=None, max_length=100),
        ),
    ]