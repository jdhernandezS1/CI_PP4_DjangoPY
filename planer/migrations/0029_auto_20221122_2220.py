# Generated by Django 3.2.15 on 2022-11-22 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planer', '0028_meal_slugmeal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='visible',
        ),
        migrations.AlterField(
            model_name='meal',
            name='slugmeal',
            field=models.BooleanField(default=True),
        ),
    ]
