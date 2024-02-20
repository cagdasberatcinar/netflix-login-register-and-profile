from django.shortcuts import render
from appUser.models import *
from .models import *

def indexPage(request):
    context = {}
    return render(request, "index.html", context)

def browseindexPage(request):
    profile = Profile.objects.get(user=request.user, islogin=True)
    
    context = {
        "profile":profile
    }
    return render(request, "browse-index.html", context)

def kategori_resimleri(request, kategori):
    kategori_object = Category.objects.filter(titles=kategori).first()
    if kategori_object:
        resimler = Video.objects.filter(category=kategori_object)
    else:
        resimler = None
    context = {
        'kategori':kategori,
        'resimler':resimler
    }
    return render(request, 'browse-index.html', context)

def yeni_ve_populer(request):
    yeni_ve_populer = Video.objects.filter(isnew=True)
    context = {
        'yeni_ve_populer': 'Yeni ve Popüler',
        'resimler': yeni_ve_populer,
    }
    return render(request, 'browse-index.html', context)

