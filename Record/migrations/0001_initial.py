# Generated by Django 4.2.3 on 2023-08-16 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Record_Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='record_photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Upload_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(upload_to='record_photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('weather', models.CharField(max_length=50)),
                ('date', models.DateField(blank=True, default=None, null=True)),
                ('body', models.TextField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('views', models.PositiveSmallIntegerField(default=0)),
                ('rlike_count', models.PositiveIntegerField(default=0)),
                ('where', models.CharField(max_length=80)),
                ('what', models.CharField(max_length=100)),
                ('how', models.CharField(max_length=100)),
                ('tag_field', models.CharField(default=0, max_length=80, null=True)),
                ('card_photo_1', models.ImageField(null=True, upload_to='record_photos/')),
                ('card_photo_2', models.ImageField(null=True, upload_to='record_photos/')),
                ('card_photo_3', models.ImageField(null=True, upload_to='record_photos/')),
                ('card_scrap', models.ManyToManyField(blank=True, related_name='card_scraps', to=settings.AUTH_USER_MODEL)),
                ('photos', models.ManyToManyField(blank=True, related_name='Record_Photo', to='Record.record_photo')),
                ('record_scrap', models.ManyToManyField(blank=True, related_name='record_scraps', to=settings.AUTH_USER_MODEL)),
                ('rlike', models.ManyToManyField(blank=True, related_name='rlikes', to=settings.AUTH_USER_MODEL)),
                ('tag', models.ManyToManyField(blank=True, to='Record.tag')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('rcomment_like_count', models.PositiveIntegerField(default=0)),
                ('rcomment_like', models.ManyToManyField(blank=True, related_name='rcomment_likes', to=settings.AUTH_USER_MODEL)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rcomments', to='Record.record')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
