# Generated by Django 5.2.3 on 2025-06-30 11:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="banner",
            field=models.ImageField(blank=True, default="fallback.png", upload_to=""),
        ),
    ]
