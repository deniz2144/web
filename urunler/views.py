from django.shortcuts import render, get_object_or_404
from .models import Urun, Mesaj
from .forms import MesajForm

def index(request):
    urunler = Urun.objects.all().order_by('?')[:3]
    return render(request, 'urunler/index.html', {'urunler': urunler})

def hakkimizda(request):
    return render(request, 'urunler/hakkimizda.html')

def urun_listesi(request):
    kategori = request.GET.get('kategori')
    if kategori == 'hindi':
        urunler = Urun.objects.filter(kategori='hindi')
    elif kategori == 'tavuk':
        urunler = Urun.objects.filter(kategori='tavuk')
    else:
        urunler = Urun.objects.all()
    return render(request, 'urunler/urun_listesi.html', {'urunler': urunler})

def urun_detay(request, pk):
    urun = get_object_or_404(Urun, pk=pk)
    return render(request, 'urunler/urun_detay.html', {'urun': urun})

def iletisim(request):
    if request.method == 'POST':
        form = MesajForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'urunler/iletisim_basarili.html')
    else:
        form = MesajForm()
    return render(request, 'urunler/iletisim.html', {'form': form})