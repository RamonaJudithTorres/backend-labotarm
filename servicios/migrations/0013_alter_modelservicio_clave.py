# Generated by Django 4.1 on 2022-10-14 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("servicios", "0012_modelservicio_estudio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="modelservicio",
            name="clave",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
