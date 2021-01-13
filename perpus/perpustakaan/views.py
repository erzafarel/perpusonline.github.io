from django.shortcuts import render, get_object_or_404
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
        form = FormBuku(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            form = FormBuku()
            pesan = "data Tersimpan"
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-buku.html', konteks)
        else:
            form = FormBuku()
            pesan = form.errors
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-buku.html', konteks)
    
    else:
        form = FormBuku()

        konteks = {
            'form': form,
        }
    
    return render(request, 'tambah-buku.html', konteks)

def edit_buku(request):

    return render(request, 'edit_buku.html', konteks)
