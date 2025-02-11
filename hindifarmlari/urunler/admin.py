from django.contrib import admin
from .models import Urun, Mesaj

@admin.register(Urun)
class UrunAdmin(admin.ModelAdmin):
    list_display = ('isim', 'fiyat', 'stok_adedi')

@admin.register(Mesaj)
class MesajAdmin(admin.ModelAdmin):
    list_display = ('ad', 'email', 'telefon', 'olusturma_tarihi')  # Telefon alanı eklendi