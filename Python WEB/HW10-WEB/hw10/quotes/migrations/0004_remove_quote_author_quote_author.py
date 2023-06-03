# Generated by Django 4.2.1 on 2023-05-17 22:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quotes", "0003_rename_name_author_fullname"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="quote",
            name="author",
        ),
        migrations.AddField(
            model_name="quote",
            name="author",
            field=models.ManyToManyField(to="quotes.author"),
        ),
    ]