# Generated by Django 3.1.3 on 2020-12-22 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favorites', '0002_auto_20201022_0257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorites',
            name='product',
        ),
    ]
