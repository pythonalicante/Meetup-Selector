# Generated by Django 3.1.2 on 2020-10-06 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TopicProposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(default='', help_text='Topic', max_length=250)),
                ('description', models.TextField(default='', help_text='Short description', max_length=250)),
                ('level', models.CharField(choices=[('BASIC', 'Basic'), ('INTERMEDIATE', 'Intermediate'), ('ADVANCED', 'Advanced')], default='BASIC', max_length=15)),
            ],
        ),
    ]
