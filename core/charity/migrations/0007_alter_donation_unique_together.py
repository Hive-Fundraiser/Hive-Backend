# Generated by Django 3.2.18 on 2023-05-18 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0006_alter_advertisement_image'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='donation',
            unique_together=set(),
        ),
    ]