# Generated by Django 3.2.8 on 2021-11-09 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_uslugi_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='uslugi',
            name='topcard',
            field=models.CharField(default='Название', max_length=30),
            preserve_default=False,
        ),
    ]