# Generated by Django 5.0.1 on 2024-02-11 11:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taxiparty", "0005_alter_taxiparty_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="taxiparty",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 2, 11, 11, 21, 33, 600124, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
