# Generated by Django 4.1 on 2022-10-12 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("servicios", "0005_tarjetas"),
    ]

    operations = [
        migrations.AlterField(
            model_name="modelservicio",
            name="costo",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AlterField(
            model_name="modelservicio",
            name="resultado",
            field=models.TextField(default="", null=True),
        ),
    ]