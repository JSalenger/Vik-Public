# Generated by Django 2.1.7 on 2019-03-30 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190226_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]