# Generated by Django 3.1.2 on 2020-10-09 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretballot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='vote',
            field=models.SmallIntegerField(choices=[(1, '+1'), (-1, '-1')]),
        ),
    ]
