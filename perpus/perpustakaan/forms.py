from django.forms import ModelForm
from django import forms
from perpustakaan.models import *

class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'

        widgets = {
            'judul' : forms.TextInput({'class':'form-control'}),
            'kategori_id' : forms.Select({'class':'form-control'}),
            'pengarang_id' : forms.Select({'class':'form-control'}),
            'penerbit_id' : forms.Select({'class':'form-control'}),
            'Tahun' : forms.Select({'class':'form-control'}),
            'ISBN' : forms.NumberInput({'class':'form-control'}),
        }

class FormPengarang(ModelForm):
    class Meta:
        models = pengarang
        fields = '__all__'

        widgets = {
            'nama' : forms.TextInput({'class':'form-control'}),
        }