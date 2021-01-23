"""perpus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from perpustakaan.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base),

    path('status/', status_anggota),
    path('tambah-status/', tambah_status),
    path('ubah-status/<int:id_status>', ubah_status, name='ubah-status/'),
    path('hapus-status/<int:id_status>', hapus_status, name='hapus-status/'),

    path('anggota/', data_anggota),
    path('tambah-anggota/', tambah_anggota),

    path('pengarang/', data_pengarang),
    path('tambah-pengarang/', tambah_pengarang),
    path('edit-pengarang/', edit_pengarang),

    path('penerbit/', data_penerbit),
    path('tambah-penerbit/', tambah_penerbit),

    path('buku/', buku),
    path('tambah-buku/', tambah_buku),
    path('edit-buku/', edit_buku),
]
