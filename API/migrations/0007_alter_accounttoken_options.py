# Generated by Django 4.0.2 on 2022-02-18 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_alter_accounttoken_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accounttoken',
            options={'verbose_name': 'Token', 'verbose_name_plural': 'Tokens'},
        ),
    ]
