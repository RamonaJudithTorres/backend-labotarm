# Generated by Django 4.1 on 2022-09-29 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("servicios", "0003_rename_resultado_modelservicio_resultado"),
    ]

    operations = [
        migrations.RemoveField(model_name="modelservicio", name="estudio",),
        migrations.AddField(
            model_name="modelservicio",
            name="estudio",
            field=models.ManyToManyField(to="servicios.modelestudio"),
        ),
    ]