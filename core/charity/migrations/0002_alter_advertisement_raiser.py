# Generated by Django 3.2.18 on 2023-04-20 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_auto_20230420_1311"),
        ("charity", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="advertisement",
            name="raiser",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.profile",
            ),
        ),
    ]
