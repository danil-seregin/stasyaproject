# Generated by Django 3.2.8 on 2021-11-08 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_otzyv'),
    ]

    operations = [
        migrations.AddField(
            model_name='otzyv',
            name='showed',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
