# Generated by Django 5.0 on 2024-02-03 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_login", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userinfo",
            name="id",
        ),
        migrations.AddField(
            model_name="userinfo",
            name="uid",
            field=models.CharField(
                default=0, max_length=16, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="msg",
            name="context",
            field=models.CharField(max_length=3, unique=True),
        ),
    ]
