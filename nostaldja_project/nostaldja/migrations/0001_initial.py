# Generated by Django 4.2.7 on 2023-11-16 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Decade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_year', models.CharField(max_length=100)),
                ('end_year', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no fade name', max_length=100)),
                ('image_url', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(default='no description', max_length=100)),
                ('decade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fads', to='nostaldja.decade')),
            ],
        ),
    ]
