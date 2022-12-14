# Generated by Django 2.2.4 on 2021-02-13 09:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('contact_id', models.CharField(max_length=50)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('contact', models.CharField(blank=True, max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('subject', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(default='unseen', max_length=50, validators=[django.core.validators.RegexValidator])),
                ('trash', models.BooleanField(default=False)),
            ],
        ),
    ]
