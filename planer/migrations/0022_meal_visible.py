# Generated by Django 3.2.15 on 2022-11-22 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planer', '0021_auto_20221122_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
