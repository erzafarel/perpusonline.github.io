import datetime
import calendar
from django.db import models
from django.utils import timezone

YEAR_CHOICES = [(r, r) for r in range(1900, datetime.date.today().year+1)]

# Create your models here.


class Identitas (models.Model):
    nama = models.CharField(max_length=50)
    class meta:
        abstract = True

class status (models.Model):
    status = models.CharField(max_length=30)
    def __str__(self):
        return self.status

class Anggota(Identitas):
    status_id = models.ForeignKey(
        status, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nama

class pengarang(Identitas):
    def __str__(self):
        return self.nama

class penerbit (Identitas):
    def __str__(self):
        return self.nama

class Kategori(models.Model):
    kategori = models.CharField(max_length=30)
    def __str__(self):
        return self.kategori

class Buku(models.Model):
    judul = models.CharField(max_length=50)
    kategori_id = models.ForeignKey(
        Kategori, on_delete=models.CASCADE, null=True)
    pengarang_id = models.ForeignKey(
        pengarang, on_delete=models.CASCADE, null=True)
    penerbit_id = models.ForeignKey(
        penerbit, on_delete=models.CASCADE, null=True)
    Tahun = models.CharField(choices=YEAR_CHOICES, max_length=5)
    ISBN  = models.IntegerField(null=True)

    def __str__(self):
        return self.judul

class waktu(models.Model):
    date = models.DateField()
    def __date__(self):
        return self.date 
    

class peminjaman(models.Model):
    waktu_id = models.ForeignKey(
        waktu, on_delete=models.CASCADE, null=True)
    anggota_id = models.ForeignKey(
        Anggota, on_delete=models.CASCADE, null=True)
    buku_id = models.ForeignKey(
        Buku, on_delete=models.CASCADE, null=True)
    jumlahpinjaman = models.IntegerField(null=True)
    def __str__(self):
        return self.jumlahpinjaman 