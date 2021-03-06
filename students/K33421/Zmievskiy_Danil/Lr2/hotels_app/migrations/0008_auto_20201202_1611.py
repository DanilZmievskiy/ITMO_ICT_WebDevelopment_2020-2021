# Generated by Django 3.1.3 on 2020-12-02 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels_app', '0007_guestsbase'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guestsbase',
            options={'verbose_name': 'Guests base', 'verbose_name_plural': 'Guests base'},
        ),
        migrations.AddField(
            model_name='guestsbase',
            name='room',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='hotels_app.room', verbose_name='Room'),
        ),
    ]
