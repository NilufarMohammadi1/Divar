# Generated by Django 4.0.3 on 2022-05-03 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_title', models.CharField(max_length=100)),
                ('product_image', models.CharField(max_length=255)),
                ('product_description', models.TextField()),
                ('price', models.CharField(max_length=100)),
                ('lat_coordinate', models.FloatField()),
                ('long_coordinate', models.FloatField()),
                ('city', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=100)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_forced', models.BooleanField(default=False)),
                ('is_negotiable', models.BooleanField(default=True)),
                ('confirmation_date', models.DateTimeField(auto_now_add=True)),
                ('delete_date', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.users')),
            ],
        ),
    ]
