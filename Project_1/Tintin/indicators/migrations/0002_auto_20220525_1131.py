# Generated by Django 3.2.13 on 2022-05-25 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MOVINGAVG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=25)),
                ('timeframe', models.CharField(max_length=25)),
                ('date', models.DateField()),
                ('value', models.FloatField()),
                ('moving_avg_length', models.CharField(max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='rsi',
            name='symbol',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='rsi',
            name='timeframe',
            field=models.CharField(max_length=25),
        ),
    ]
