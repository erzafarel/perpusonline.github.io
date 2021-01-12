from django.shortcuts import render
from perpustakaan.models import *
from perpustakaan.forms import *

# Create your views here.

def base(request):
    konteks = {
        'judul': 'Perpustakaan Online',
    }
    return render(request, 'base.html', konteks)

def buku(request):
    books = Buku.objects.all()

    konteks = {
        'books': books,
    }

    return render(request, 'buku.html', konteks)


def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            form = FormBuku()

            konteks = {
                'form': form,
            }
            return render(request, 'tambah-buku.html', konteks)
    
    else:
        form = FormBuku()
        
        konteks = {
            'form': form,
        }
    
    return render(request, 'tambah-buku.html', konteks)

def edit_buku(request):

    return render(request, 'edit_buku.html')