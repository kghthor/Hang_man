# Generated by Django 2.2.7 on 2020-07-16 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hangMansApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='letterKnows',
            field=models.CharField(default='', max_length=255, verbose_name='Letter Knows'),
        ),
    ]
