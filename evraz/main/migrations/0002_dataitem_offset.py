# Generated by Django 4.1.7 on 2023-02-18 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataitem',
            name='offset',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
