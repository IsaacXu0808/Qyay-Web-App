# Generated by Django 5.0 on 2024-02-17 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_login", "0007_alter_question_eid"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="answered",
            field=models.BooleanField(default=False),
        ),
    ]