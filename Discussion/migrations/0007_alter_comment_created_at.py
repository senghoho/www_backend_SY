# Generated by Django 4.2.3 on 2023-08-11 15:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion', '0006_alter_comment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 12, 0, 7, 44, 742809)),
        ),
    ]
