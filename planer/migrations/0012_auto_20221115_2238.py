# Generated by Django 3.2.15 on 2022-11-15 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planer', '0011_auto_20221113_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='slug',
            field=models.SlugField(default=1, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meal',
            name='meal_number',
            field=models.IntegerField(choices=[(1, 'breakfast'), (2, 'lunch'), (3, 'dinner')], default=0),
        ),
    ]
