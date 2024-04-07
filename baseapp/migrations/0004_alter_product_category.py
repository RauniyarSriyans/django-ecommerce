# Generated by Django 5.0.4 on 2024-04-07 08:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("baseapp", "0003_product_vendor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="category",
                to="baseapp.category",
            ),
        ),
    ]
