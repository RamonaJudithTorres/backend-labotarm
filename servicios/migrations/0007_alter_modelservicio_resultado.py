# Generated by Django 4.1 on 2022-10-12 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("servicios", "0006_alter_modelservicio_costo_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="modelservicio",
            name="resultado",
            field=models.TextField(blank=True, default="", null=True),
        ),
    ]
