# Generated by Django 4.2.3 on 2023-07-19 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickit', '0005_remove_band_show_id_show_band_id_alter_band_band_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='logo',
            field=models.ImageField(default='No Logo Provided', upload_to=''),
        ),
        migrations.AlterField(
            model_name='show',
            name='poster',
            field=models.ImageField(default='No Poster Provided', upload_to=''),
        ),
        migrations.AlterField(
            model_name='venue',
            name='venue_photo',
            field=models.ImageField(default='No photo available', upload_to=''),
        ),
    ]
