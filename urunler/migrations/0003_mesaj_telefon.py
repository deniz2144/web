# Generated by Django 5.1.4 on 2025-01-29 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0002_mesaj'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesaj',
            name='telefon',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
