# Generated by Django 5.1 on 2024-09-05 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0004_board_is_deleted_alter_board_content_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
    ]
