# Generated by Django 4.2.3 on 2023-08-18 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Companion", "0002_alter_companion_writer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cocomment",
            name="writer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
