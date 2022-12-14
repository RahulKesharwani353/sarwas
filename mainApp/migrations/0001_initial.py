# Generated by Django 4.1.3 on 2022-11-24 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('asin', models.UUIDField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=2000)),
                ('partition', models.IntegerField(blank=True)),
                ('ccScore', models.DecimalField(blank=True, decimal_places=5, default=0, max_digits=7)),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
