# Generated by Django 3.0.7 on 2020-11-13 23:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genea_viewer', '0003_lifeevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='BirthEvent',
            fields=[
                ('lifeevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='genea_viewer.LifeEvent')),
                ('date', models.DateTimeField(default=datetime.datetime(1, 1, 1, 0, 0))),
            ],
            bases=('genea_viewer.lifeevent',),
        ),
    ]