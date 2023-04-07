# Generated by Django 4.2 on 2023-04-07 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=120)),
                ('price', models.PositiveIntegerField()),
                ('stock', models.PositiveBigIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]