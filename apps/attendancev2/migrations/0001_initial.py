# Generated by Django 5.0.3 on 2024-04-16 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LabSystemModel",
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
                ("lab_no", models.CharField(blank=True, max_length=200, null=True)),
                ("systems", models.JSONField(default=list)),
            ],
        ),
    ]