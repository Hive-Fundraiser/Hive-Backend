# Generated by Django 3.2.18 on 2023-05-24 16:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0007_remove_profile_bank_account_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="bank_account_number",
            field=models.CharField(max_length=16, null=True),
        ),
    ]
