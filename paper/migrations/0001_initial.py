# Generated by Django 3.1.6 on 2021-02-19 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('author', models.CharField(max_length=100)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField()),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish'), (2, 'Delete')], default=0)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
