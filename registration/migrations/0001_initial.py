# Generated by Django 3.0.2 on 2020-02-25 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(blank=True, max_length=100)),
                ('starts_on', models.DateTimeField()),
                ('action', models.BooleanField(default=True)),
            ],
        ),
    ]
