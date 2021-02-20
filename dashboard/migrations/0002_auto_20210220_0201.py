# Generated by Django 3.1.6 on 2021-02-19 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notify',
            options={'ordering': ['-time']},
        ),
        migrations.AddField(
            model_name='notify',
            name='dept',
            field=models.IntegerField(choices=[(1, 'CSE'), (2, 'CIVIL'), (3, 'EEE'), (4, 'IT'), (5, 'ECE'), (6, 'MECH'), (7, 'EIE'), (8, 'ALL')], default=8),
        ),
        migrations.AddField(
            model_name='notify',
            name='section',
            field=models.IntegerField(choices=[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'ALL')], default=4),
        ),
        migrations.AddField(
            model_name='notify',
            name='year',
            field=models.IntegerField(choices=[(1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'), (5, 'ALL')], default=5),
        ),
    ]
