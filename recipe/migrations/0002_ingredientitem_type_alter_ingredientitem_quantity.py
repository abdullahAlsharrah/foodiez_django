# Generated by Django 4.1 on 2022-08-17 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ingredientitem",
            name="type",
            field=models.CharField(
                choices=[
                    ("Cup", "Cup"),
                    ("Gram", "Gram"),
                    ("Liter", "Liter"),
                    ("Piece", "Piece"),
                ],
                default="cup",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="ingredientitem",
            name="quantity",
            field=models.FloatField(),
        ),
    ]