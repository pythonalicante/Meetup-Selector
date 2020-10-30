# Generated by Django 3.1.2 on 2020-10-30 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0009_collaborator_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborator',
            name='profile',
            field=models.CharField(blank=True, default='', help_text='Collaborator profile', max_length=250, null=True),
        ),
    ]