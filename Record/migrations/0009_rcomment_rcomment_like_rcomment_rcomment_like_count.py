# Generated by Django 4.2.3 on 2023-08-15 08:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Record', '0008_alter_record_rlike'),
    ]

    operations = [
        migrations.AddField(
            model_name='rcomment',
            name='rcomment_like',
            field=models.ManyToManyField(blank=True, related_name='rcomment_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rcomment',
            name='rcomment_like_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
