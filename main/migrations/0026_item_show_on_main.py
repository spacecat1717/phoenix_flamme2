# Generated by Django 3.2.13 on 2022-06-22 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_remove_item_pickup'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='show_on_main',
            field=models.BooleanField(default=False),
        ),
    ]
