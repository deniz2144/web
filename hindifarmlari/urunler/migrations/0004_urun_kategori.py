# Generated by Django 5.1.4 on 2025-01-29 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0003_mesaj_telefon'),
    ]

    operations = [
        migrations.AddField(
            model_name='urun',
            name='kategori',
            field=models.CharField(choices=[('hindi', 'Hindi'), ('tavuk', 'Tavuk')], default='hindi', max_length=10),
            preserve_default=False,
        ),
    ]
