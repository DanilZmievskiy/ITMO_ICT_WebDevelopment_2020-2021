# Generated by Django 3.1.5 on 2021-01-22 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airport', '0002_auto_20210122_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reys',
            name='id_tranzita',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='airport.tranzit', verbose_name='ID транзита'),
        ),
    ]
