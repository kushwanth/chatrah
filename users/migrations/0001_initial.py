# Generated by Django 3.2 on 2021-04-09 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('name', models.CharField(default='STUDENT', max_length=200)),
                ('number', models.CharField(default='000000000', max_length=15, primary_key=True, serialize=False, unique=True)),
                ('YoA', models.PositiveIntegerField(default='0000')),
                ('year', models.IntegerField(choices=[(1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV')], default=1)),
                ('dept', models.IntegerField(choices=[(1, 'CSE'), (2, 'CIVIL'), (3, 'EEE'), (4, 'IT'), (5, 'ECE'), (6, 'MECH'), (7, 'EIE')], default=1)),
                ('section', models.IntegerField(choices=[(1, 'A'), (2, 'B'), (3, 'C')], default=1)),
                ('verified', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-number'],
            },
        ),
    ]
