# Generated by Django 5.0 on 2024-02-10 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_login", "0006_question"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="eid",
            field=models.IntegerField(default=0),
        ),
    ]
