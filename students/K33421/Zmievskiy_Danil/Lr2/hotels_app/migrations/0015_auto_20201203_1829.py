# Generated by Django 3.1.3 on 2020-12-03 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels_app', '0014_auto_20201203_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='end_date',
            field=models.DateField(null=True, verbose_name='EndDate'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start_date',
            field=models.DateField(null=True, verbose_name='StartDate'),
        ),
    ]
