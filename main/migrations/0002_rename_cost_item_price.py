# Generated by Django 4.0.4 on 2022-05-30 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='cost',
            new_name='price',
        ),
    ]