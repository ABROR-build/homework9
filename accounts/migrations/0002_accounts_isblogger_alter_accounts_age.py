# Generated by Django 5.0.6 on 2024-05-17 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='isblogger',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='age',
            field=models.IntegerField(default=18),
        ),
    ]
