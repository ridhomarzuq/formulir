from django.db import models

# Create your models here.
class Formulir(models.Model):
    jenis =[('Forklift','Forklift'),('Crane','Crane'),('Gondola','Gondola'),('Alat Berat','Alat Berat'),('Passenger Hoist','Passenger Hoist'),('Conveyor','Conveyor')]
    kelas_alat =[('None','None'),('1','1'),('2','2'),('3','3')]
    lulus = [('Sekolah Menengah Pertama','SMP'),('Sekolah Menengah Atas','SMA'),('Diploma I','D1'),('Diploma II','D2'),('Diploma III','D3'),('Diploma IV','D4'),('Strata I','S1')]
    Nama = models.CharField(max_length=100)
    Alamat = models.CharField(max_length=100)
    Asal_perusahaan = models.CharField(max_length=100)
    Jenis_Alat = models.CharField(max_length=25,choices=jenis)
    kelas = models.CharField(max_length=25, choices=kelas_alat)
    KTP = models.ImageField(upload_to='ktp/',null=True)
    CV = models.FileField(upload_to='cv/',null=False)
    Foto = models.ImageField(upload_to='foto/',null=False)
    Ijazah = models.CharField(max_length=25, choices=lulus)
    SuratPernyataan = models.FileField(upload_to='surat_pernyataan/',null=False)
    Keterangan_Kerja = models.FileField(upload_to='keterangan_kerja/', null=False)

    def __str__(self):
        return self.Nama