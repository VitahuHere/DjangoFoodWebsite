# Generated by Django 3.2.9 on 2021-12-02 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('login', models.CharField(default=None, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(default=None, max_length=200)),
                ('name', models.CharField(default=None, max_length=100)),
                ('surname', models.CharField(default=None, max_length=100)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
