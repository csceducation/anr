# Generated by Django 5.0.3 on 2024-03-16 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("corecode", "0002_auto_20240314_1741"),
        ("students", "0002_alter_student_passport"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="class_time",
        ),
        migrations.AddField(
            model_name="student",
            name="class_time",
            field=models.ManyToManyField(
                blank=True, to="corecode.time", verbose_name="Class Timing"
            ),
        ),
    ]
