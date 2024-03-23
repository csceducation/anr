# Generated by Django 5.0.3 on 2024-03-20 18:34

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("batch", "0002_initial"),
        ("students", "0004_alter_student_pincode"),
    ]

    operations = [
        migrations.CreateModel(
            name="BatchLabAttendance",
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
                ("date", models.DateField(default=django.utils.timezone.now)),
                ("session", models.IntegerField()),
                ("entry_time", models.TimeField()),
                ("exit_time", models.TimeField()),
                (
                    "batch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lab_attendance",
                        to="batch.batchmodel",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="batch_lab_attendance",
                        to="students.student",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BatchTheoryAttendance",
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
                ("date", models.DateField(default=django.utils.timezone.now)),
                ("session", models.IntegerField()),
                ("entry_time", models.TimeField()),
                ("exit_time", models.TimeField()),
                (
                    "batch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Theory_attendance",
                        to="batch.batchmodel",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="batch_Theory_attendance",
                        to="students.student",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DailyAttendance",
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
                ("date", models.DateField(auto_now=True)),
                ("students", models.ManyToManyField(null=True, to="students.student")),
            ],
        ),
    ]