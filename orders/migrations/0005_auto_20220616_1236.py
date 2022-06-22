# Generated by Django 3.2.13 on 2022-06-16 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20220608_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='track',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='total_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]