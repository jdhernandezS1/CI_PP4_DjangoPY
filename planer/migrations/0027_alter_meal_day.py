# Generated by Django 3.2.15 on 2022-11-22 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planer', '0026_rename_day_title_day_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='day',
            field=models.CharField(choices=[('monday', 'monday'), ('tuesday', 'tuesday'), ('wednesday', 'wednesday'), ('thursday', 'thursday'), ('friday', 'friday'), ('saturday', 'saturday'), ('sunday', 'sunday')], default=0, max_length=20),
        ),
    ]
