# Generated by Django 3.0.5 on 2020-05-08 05:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Seed', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)], verbose_name='seed')),
                ('HumanTheme', models.CharField(max_length=128)),
                ('WolfTheme', models.CharField(max_length=128)),
            ],
        ),
    ]