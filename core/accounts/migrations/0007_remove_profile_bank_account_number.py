# Generated by Django 3.2.18 on 2023-05-23 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bank_account_number',
        ),
    ]
