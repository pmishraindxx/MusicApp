# Generated by Django 2.2.7 on 2020-08-10 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_base', '0003_auto_20200810_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='mp3file',
            field=models.FileField(upload_to=''),
        ),
    ]