# Generated by Django 3.2.13 on 2022-06-21 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='pickup',
            field=models.BooleanField(default=False),
        ),
    ]
