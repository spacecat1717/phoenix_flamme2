# Generated by Django 3.2.13 on 2022-06-07 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20220606_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.BooleanField(default=False),
        ),
    ]