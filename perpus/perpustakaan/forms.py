from django.forms import ModelForm
from django import forms
from perpustakaan.models import *


class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'

        widgets = {
            'judul': forms.TextInput({'class': 'form-control'}),
            'kategori_id': forms.Select({'class': 'form-control'}),
            'pengarang_id': forms.Select({'class': 'form-control'}),
            'penerbit_id': forms.Select({'class': 'form-control'}),
            'tahun': forms.Select({'class': 'form-control'}),
            'ISBN': forms.NumberInput({'class': 'form-control'}),
        }


class FormStatus(ModelForm):
    class Meta:
        model = status
        fields = '__all__'

        widgets = {
            'status': forms.TextInput({'class': 'form-control'}),
        }


class FormAnggota(ModelForm):
    class Meta:
        model = anggota
        fields = '__all__'

        widgets = {
            'nama': forms.TextInput({'class': 'form-control'}),
            'status_id': forms.Select({'class': 'form-control'}),
            'alamat': forms.TextInput({'class': 'form-control'}),
            'telp': forms.NumberInput({'class': 'form-control'}),
        }


class FormPengarang(ModelForm):
    class Meta:
        model = pengarang
        fields = '__all__'

        widgets = {
            'nama': forms.TextInput({'class': 'form-control'}),
            'alamat': forms.Textarea({'class': 'form-control'}),
            'telp': forms.NumberInput({'class': 'form-control'}),
        }


class FormPenerbit(ModelForm):
    class Meta:
        model = penerbit
        fields = '__all__'

        widgets = {
            'nama': forms.TextInput({'class': 'form-control'}),
            'alamat': forms.TextInput({'class': 'form-control'}),
            'telp': forms.NumberInput({'class': 'form-control'}),
        }
