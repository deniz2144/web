from django.contrib import admin
from .models import Urun, Mesaj

@admin.register(Urun)
class UrunAdmin(admin.ModelAdmin):
    list_display = ('isim', 'kategori')  # 'stok_adedi' kaldırıldı
    fields = ('isim', 'aciklama', 'resim', 'kategori')  # 'stok_adedi' kaldırıldı

@admin.register(Mesaj)
class MesajAdmin(admin.ModelAdmin):
    list_display = ('ad', 'email', 'telefon', 'olusturma_tarihi')