# Generated by Django 5.0.3 on 2024-03-27 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0002_auto_20240326_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
