# Generated by Django 3.2.13 on 2022-07-07 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_remove_order_track_sended'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='size',
            new_name='oil',
        ),
    ]
