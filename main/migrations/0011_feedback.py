# Generated by Django 3.2.13 on 2022-06-03 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_item_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('photo1', models.ImageField(upload_to='static/feedback')),
                ('photo2', models.ImageField(upload_to='static/feedback')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
