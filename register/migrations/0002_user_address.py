# Generated by Django 3.2.5 on 2021-07-07 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
    ]
