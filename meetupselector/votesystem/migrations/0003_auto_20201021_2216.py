# Generated by Django 3.1.2 on 2020-10-21 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votesystem', '0002_auto_20201010_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProposedMeetUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(2020, '2020'), (2021, '2021')], default=2020)),
                ('month', models.IntegerField(choices=[(1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'), (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'), (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')], default=10)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('topic_proposal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='votesystem.topicproposal')),
            ],
            options={
                'ordering': ['-year', '-month'],
            },
        ),
        migrations.AddIndex(
            model_name='proposedmeetup',
            index=models.Index(fields=['year', 'month'], name='votesystem__year_ed6624_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='proposedmeetup',
            unique_together={('year', 'month')},
        ),
    ]
