# Generated by Django 4.2.4 on 2023-09-01 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcodemain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode',
            name='scan_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='qrcode',
            name='url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
