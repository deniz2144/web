from django.db import models

class Urun(models.Model):
    KATEGORI_CHOICES = [
        ('hindi', 'Hindi'),
        ('tavuk', 'Tavuk'),
    ]
    isim = models.CharField(max_length=100)
    aciklama = models.TextField()
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)  # Fiyat alanı (gizlenecek)
    resim = models.ImageField(upload_to='urunler/', blank=True, null=True)
    kategori = models.CharField(max_length=10, choices=KATEGORI_CHOICES)

    def __str__(self):
        return self.isim

class Mesaj(models.Model):
    ad = models.CharField(max_length=100)
    email = models.EmailField()
    telefon = models.CharField(max_length=15, blank=True, null=True)
    mesaj = models.TextField()
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ad