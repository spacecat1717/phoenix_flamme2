# Generated by Django 3.2.13 on 2022-06-08 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_contacts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='inst',
        ),
    ]
