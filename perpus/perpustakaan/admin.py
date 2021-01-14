from django.contrib import admin
from perpustakaan.models import *

# Register your models here.


class BukuAdmin(admin.ModelAdmin):
    list_display = ['judul', 'pengarang_id', 'penerbit_id', 'Tahun']
    search_fields = ['judul', 'pengarang_id', 'penerbit_id']
    # list_filter = ('kelompok_id')
    list_per_page = 5

class AnggotaData(admin.ModelAdmin):
    list_display = ['nama', 'status_id']
    search_fields = ['nama', 'status_id']
    list_per_page = 5

admin.site.register(Kategori)
admin.site.register(status)
admin.site.register(Anggota, AnggotaData)
admin.site.register(pengarang)
admin.site.register(penerbit)
admin.site.register(Buku, BukuAdmin)
admin.site.register(waktu)
admin.site.register(peminjaman)



