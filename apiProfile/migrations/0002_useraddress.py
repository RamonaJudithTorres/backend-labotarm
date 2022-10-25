# Generated by Django 4.1 on 2022-09-07 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("apiProfile", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserAddress",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address_line_1", models.CharField(max_length=200)),
                ("city", models.CharField(max_length=200)),
                ("zip_code", models.CharField(max_length=200)),
                ("country", models.CharField(max_length=200)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apiProfile.profile",
                    ),
                ),
            ],
        ),
    ]