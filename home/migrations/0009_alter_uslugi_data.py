# Generated by Django 3.2.8 on 2021-11-08 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_uslugi_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uslugi',
            name='data',
            field=models.TextField(max_length=320),
        ),
    ]