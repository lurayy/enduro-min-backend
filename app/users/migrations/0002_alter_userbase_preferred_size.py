# Generated by Django 4.2.5 on 2024-02-27 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbase',
            name='preferred_size',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
