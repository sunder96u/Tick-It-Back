# Generated by Django 4.2.3 on 2023-07-19 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickit', '0002_shows'),
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='show', to='tickit.venue')),
            ],
        ),
        migrations.DeleteModel(
            name='Shows',
        ),
    ]
