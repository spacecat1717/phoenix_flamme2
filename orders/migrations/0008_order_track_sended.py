# Generated by Django 3.2.13 on 2022-06-17 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_remove_orderitem_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='track_sended',
            field=models.BooleanField(default=False),
        ),
    ]
