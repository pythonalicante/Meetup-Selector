# Generated by Django 3.1.2 on 2020-10-24 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0002_auto_20201016_1819'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LandingPageContent',
            new_name='Content',
        ),
    ]