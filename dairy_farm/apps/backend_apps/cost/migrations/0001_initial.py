# Generated by Django 2.2.4 on 2021-02-08 13:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('access', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('cost_id', models.CharField(max_length=50)),
                ('field', models.CharField(max_length=250)),
                ('amount', models.DecimalField(blank=True, decimal_places=3, max_digits=10)),
                ('remark', models.TextField(blank=True)),
                ('status', models.CharField(default='active', max_length=50, validators=[django.core.validators.RegexValidator])),
                ('trash', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cost_user_id', to='access.User')),
            ],
        ),
    ]
