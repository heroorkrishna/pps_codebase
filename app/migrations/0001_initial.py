# Generated by Django 5.0.6 on 2024-06-06 08:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Invoice",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("emp_id", models.CharField(max_length=100)),
                ("emp_name", models.CharField(max_length=100)),
            ],
        ),
    ]
