# Generated by Django 4.0.6 on 2022-07-20 07:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('voteApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='name',
            field=models.CharField(default=datetime.datetime(2022, 7, 20, 7, 11, 6, 271535, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='vote_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
