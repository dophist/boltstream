# Generated by Django 3.1.4 on 2020-12-08 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boltstream", "0004_user_uuid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
    ]
