# Generated by Django 3.2.13 on 2022-06-17 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_alter_order_track_sended'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='track_sended',
            field=models.BooleanField(null=True),
        ),
    ]
