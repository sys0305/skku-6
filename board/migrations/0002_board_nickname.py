# Generated by Django 5.1 on 2024-09-02 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="board",
            name="nickname",
            field=models.CharField(default="", max_length=50),
            preserve_default=False,
        ),
    ]
