# Generated by Django 4.1 on 2022-10-12 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("servicios", "0009_alter_modelservicio_estudio_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="modelservicio",
            name="estudio",
            field=models.ManyToManyField(to="servicios.modelestudio"),
        ),
    ]
