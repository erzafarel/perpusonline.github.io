from django.shortcuts import render, redirect
from perpustakaan.models import *
from perpustakaan.forms import *


# Create your views here.


def base(request):
    konteks = {
        'judul': 'Perpustakaan Online',
    }
    return render(request, 'base.html', konteks)

# --------------------------------- Table Status --------------------------------------


def status_anggota(request):
    statuss = status.objects.all()
    konteks = {
        'position': statuss,
    }

    return render(request, 'status.html', konteks)


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
            'form': form,
        }

    return render(request, 'tambah_status.html', konteks)


def ubah_status(request, id_status):
    statuss = status.objects.get(id=id_status)
    template = 'ubah_status.html'
    if request.POST:
        form = FormStatus(request.POST, instance=statuss)
        if form.is_valid():
            form.save()
            return redirect('ubah-status/', id_status=id_status)
    else:
        form = FormStatus(instance=statuss)
        konteks = {
            'form': form,
            'statuss': statuss,
        }
    return render(request, template, konteks)


def hapus_status(request, id_status):
    statuss = status.objects.filter(id=id_status)
    statuss.delete()
    return redirect('/status/')

# --------------------------------- Table Anggota --------------------------------------


def data_anggota(request):
    member = anggota.objects.all()

    konteks = {
        'member': member,
    }

    return render(request, 'anggota.html', konteks)


def tambah_anggota(request):
    if request.POST:
        form = FormAnggota(request.POST)
        if form.is_valid():
            form.save()
            form = FormAnggota()
            konteks = {
                'form': form,
            }
            return redirect('/tambah-anggota/', konteks)
    else:
        form = FormAnggota

        konteks = {
            'form': form,
        }

    return render(request, 'tambah_anggota.html', konteks)


# -------------------------------- Table Pengarang --------------------------------------


def data_pengarang(request):
    cipta = pengarang.objects.all()

    konteks = {
        'cipta': cipta,
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
            return redirect('/tambah-pengarang/', konteks)
    else:
        form = FormPengarang

        konteks = {
            'form': form,
        }

    return render(request, 'tambah_pengarang.html', konteks)


def edit_pengarang(request):

    return render(request, 'edit_pengarang.html', konteks)

# ------------------------------- Table Penerbit --------------------------------------


def data_penerbit(request):
    cetaks = penerbit.objects.all()

    konteks = {
        'cetak': cetaks,
    }

    return render(request, 'penerbit.html', konteks)


def tambah_penerbit(request):
    if request.POST:
        form = FormPenerbit(request.POST)
        if form.is_valid():
            form.save()
            form = FormPenerbit()
            konteks = {
                'form': form,
            }
            return redirect('/tambah-penerbit/', konteks)
    else:
        form = FormPenerbit

        konteks = {
            'form': form,
        }

    return render(request, 'tambah_penerbit.html', konteks)


# ----------------------------------- Table Buku --------------------------------------

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
