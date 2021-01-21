from django.shortcuts import render, redirect
from perpustakaan.models import *
from perpustakaan.forms import *

# Create your views here.

def base(request):
    konteks = {
        'judul': 'Perpustakaan Online',
    }
    return render(request, 'base.html', konteks)

def tambah_status(request):
    if request.POST:
        form = FormStatus(request.POST)
        if form.is_valid():
            form.save()
            form = FormStatus()
            konteks = {
                'form': form,
            }
            return redirect('/tambah-status/', konteks)
    else:
        form = FormStatus

        konteks = {
            'form' : form,
        }
    
    return render(request, 'tambah_status.html', konteks)

def pengarang(request):
    user = pengarang.objects.all()

    konteks = {
        'pengarang': user,
    }

    return render(request, 'pengarang.html', konteks)

def tambah_pengarang(request):
    if request.POST:
        form = FormPengarang(request.POST)
        if form.is_valid():
            form.save()
            form = FormPengarang()
            konteks = {
                'form': form,
            }
            return redirect('/')
    else:
        form = FormPengarang

        konteks = {
            'form' : form,
        }
    
    return redirect('/')

def edit_pengarang(request):

    return render(request, 'edit_pengarang.html', konteks)

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

    return render(request, 'edit_buku.html', konteks)
