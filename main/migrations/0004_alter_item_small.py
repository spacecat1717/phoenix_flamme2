# Generated by Django 3.2.13 on 2022-06-01 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220601_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='small',
            field=models.CharField(max_length=20),
        ),
    ]