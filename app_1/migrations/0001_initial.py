# Generated by Django 2.2.3 on 2019-07-28 03:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('calories', models.FloatField(default=0.0)),
                ('tot_fat', models.FloatField(default=0.0)),
                ('tot_protein', models.FloatField(default=0.0)),
                ('sugar', models.FloatField(default=0.0)),
                ('tot_carbs', models.FloatField(default=0.0)),
                ('fat_saturated', models.FloatField(default=0.0)),
                ('fiber', models.FloatField(default=0.0)),
                ('sodium', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('date_birth', models.DateField(null=True)),
                ('country', models.CharField(max_length=30, null=True)),
                ('city', models.CharField(max_length=30, null=True)),
                ('cp', models.IntegerField(null=True)),
                ('tags', models.CharField(max_length=180, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories_obj', models.IntegerField()),
                ('carbs_obj', models.IntegerField()),
                ('protein_obj', models.IntegerField()),
                ('fat_obj', models.IntegerField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('amount', models.CharField(max_length=15)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.Item')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_consumed', models.DateField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.Item')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.Profile')),
            ],
        ),
    ]
