# Generated by Django 2.0 on 2018-01-02 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoentity',
            name='photo_file',
            field=models.ImageField(help_text='Files cannot exceed 1.5MB.', upload_to='images/'),
        ),
    ]