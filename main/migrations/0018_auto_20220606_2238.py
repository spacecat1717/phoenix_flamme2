# Generated by Django 3.2.13 on 2022-06-06 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20220606_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='photo1',
            field=models.ImageField(upload_to='media/main/static/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='photo2',
            field=models.ImageField(upload_to='media/main/static/'),
        ),
    ]
