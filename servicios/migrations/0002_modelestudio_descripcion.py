# Generated by Django 4.1 on 2022-08-24 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("servicios", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="modelestudio",
            name="descripcion",
            field=models.TextField(null=True),
        ),
    ]
