# Generated by Django 2.2.7 on 2020-08-10 12:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('audio_base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.CharField(default=django.utils.timezone.now, max_length=4000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(max_length=4000),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=4000),
        ),
    ]
