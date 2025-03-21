# Generated by Django 5.0.3 on 2025-03-12 07:01

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
                ('name', models.CharField(max_length=255)),
                ('barcode', models.CharField(max_length=50, unique=True)),
                ('eco_score', models.IntegerField()),
                ('recyclability', models.CharField(max_length=255)),
                ('alternative', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
