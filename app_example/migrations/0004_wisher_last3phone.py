# Generated by Django 5.1 on 2024-11-28 16:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_example", "0003_alter_wisher_key"),
    ]

    operations = [
        migrations.AddField(
            model_name="wisher",
            name="last3phone",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
