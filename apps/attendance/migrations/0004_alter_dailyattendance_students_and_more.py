# Generated by Django 5.0.3 on 2024-03-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("attendance", "0003_staffdailyattendance"),
        ("staffs", "0002_alter_staff_staff_role"),
        ("students", "0004_alter_student_pincode"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailyattendance",
            name="students",
            field=models.ManyToManyField(to="students.student"),
        ),
        migrations.AlterField(
            model_name="staffdailyattendance",
            name="staffs",
            field=models.ManyToManyField(to="staffs.staff"),
        ),
    ]
