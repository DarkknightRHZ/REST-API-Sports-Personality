# Generated by Django 3.0.8 on 2020-07-05 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sports_person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.IntegerField(default=-1)),
                ('name', models.CharField(default='John Doe', max_length=60)),
                ('sport', models.CharField(default='NR', max_length=60)),
            ],
        ),
    ]
