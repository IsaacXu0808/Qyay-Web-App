# Generated by Django 5.0 on 2024-02-04 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_login", "0002_remove_userinfo_id_userinfo_uid_alter_msg_context"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("uid", models.CharField(max_length=20)),
                ("uname", models.CharField(max_length=14)),
                ("ename", models.CharField(max_length=30)),
                ("ediscription", models.CharField(max_length=200)),
                ("edate", models.DateField(max_length=20)),
                ("etime", models.TimeField(max_length=20)),
                ("invcode", models.CharField(max_length=6, unique=True)),
            ],
        ),
    ]
