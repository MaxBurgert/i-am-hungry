# Generated by Django 2.1.7 on 2019-02-26 18:31

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("recipe_name", models.CharField(max_length=200)),
                ("recipe_ingredient", models.CharField(max_length=200)),
                ("recipe_source", models.CharField(max_length=200)),
            ],
        )
    ]