# Generated by Django 3.0.6 on 2020-08-11 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('ingredients', models.TextField()),
                ('label', models.CharField(max_length=100)),
                ('saturatedFat', models.CharField(max_length=100)),
                ('fat', models.CharField(max_length=100)),
                ('salt', models.CharField(max_length=100)),
                ('sugar', models.CharField(max_length=100)),
                ('allergen', models.TextField()),
                ('nutriscore', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('pictureUrl', models.URLField()),
                ('category', models.ManyToManyField(related_name='category', to='substitutesearch.Category')),
            ],
        ),
    ]