# Generated by Django 3.0.2 on 2020-02-25 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('team', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('profilepic', models.ImageField(blank=True, upload_to='team-profilepics')),
                ('github', models.URLField(blank=True, max_length=1000)),
                ('linkedIn', models.URLField(blank=True, max_length=1000)),
                ('twitter', models.URLField(blank=True, max_length=1000)),
                ('dribble', models.URLField(blank=True, max_length=1000)),
            ],
        ),
    ]