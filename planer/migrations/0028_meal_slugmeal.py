# Generated by Django 3.2.15 on 2022-11-22 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planer', '0027_alter_meal_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='slugmeal',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
