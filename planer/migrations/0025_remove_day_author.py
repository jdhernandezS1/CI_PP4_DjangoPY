# Generated by Django 3.2.15 on 2022-11-22 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planer', '0024_auto_20221122_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='author',
        ),
    ]
