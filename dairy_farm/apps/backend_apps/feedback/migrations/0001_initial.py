# Generated by Django 2.2.4 on 2021-02-13 11:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('feedback_id', models.CharField(max_length=50)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('contact', models.CharField(blank=True, max_length=55)),
                ('email', models.CharField(blank=True, max_length=155)),
                ('description', models.TextField(blank=True)),
                ('rating', models.CharField(blank=True, max_length=15)),
                ('status', models.CharField(default='unseen', max_length=50, validators=[django.core.validators.RegexValidator])),
                ('trash', models.BooleanField(default=False)),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedback_product', to='product.Table')),
            ],
        ),
    ]
