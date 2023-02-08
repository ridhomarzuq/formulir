from django.contrib import admin
from myapp.models import Formulir

# Register your models here.
class Adminformulir(admin.ModelAdmin):
    list_display =('Nama','Alamat','Jenis_Alat','kelas','KTP','CV','Foto','Ijazah','SuratPernyataan','Keterangan_Kerja')
    list_filter =('Nama','Jenis_Alat','kelas')
    search_fields = ('Nama','Jenis_Alat')
    list_per_page = 4

admin.site.register(Formulir,Adminformulir)