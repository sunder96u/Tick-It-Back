# Generated by Django 4.2.3 on 2023-07-19 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('capacity', models.IntegerField(default=0)),
                ('type', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('venue_photo', models.TextField()),
            ],
        ),
    ]
