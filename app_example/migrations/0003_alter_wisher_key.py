# Generated by Django 5.1 on 2024-11-27 14:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_example", "0002_wisher_relationship"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wisher",
            name="key",
            field=models.CharField(
                blank=True, max_length=128, null=True, verbose_name="Key"
            ),
        ),
    ]
