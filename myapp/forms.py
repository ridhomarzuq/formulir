from django.forms import ModelForm
from django import forms
from myapp.models import *

class Formform(ModelForm):
    class Meta:
        model = Formulir
        fields = '__all__'
    
        widgets = {
            'Nama': forms.TextInput({'class':'form-control'}),
            'Alamat': forms.TextInput({'class':'form-control'}),
            'Asal_perusahaan':forms.TextInput({'class':'form-control'}),
            'Jenis_Alat': forms.Select({'class':'form-control'}),
            'kelas': forms.Select({'class':'form-control'}),
            'KTP':forms.FileInput({'class':'form-control'}),
            'CV':forms.FileInput({'class':'form-control'}),
            'Foto':forms.FileInput({'class':'form-control'}),
            'Ijazah':forms.Select({'class':'form-control'}),
            'SuratPernyataan': forms.FileInput({'class':'form-control'}),
            'Keterangan_Kerja':forms.FileInput({'class':'form-control'}),
        }