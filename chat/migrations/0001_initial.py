# Generated by Django 4.2.1 on 2023-06-07 08:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Friends",
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
                ("friend", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Messages",
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
                ("description", models.TextField()),
                ("time", models.TimeField(auto_now_add=True)),
                ("seen", models.BooleanField(default=False)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ("timestamp",),
            },
        ),
    ]