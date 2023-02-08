from django.shortcuts import render,redirect
from myapp.models import *
from myapp.forms import *
from django.contrib import messages

def home(request):
    templates = 'home.html'
    konteks = {
        templates:'templates',
    }
    return render(request,'home.html',konteks)

def formulir(request):
    isi = Formulir.objects.all()
    konteks = {
        'isi':isi,
    }
    return render(request,'data.html',konteks)

def tambah_formulir(request):
    form = Formform(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        form = Formform()
        pesan ="Data Sudah Terkirim"

        konteks ={
            'form':form,
            'pesan':pesan
        }
        return render(request,'tambah-data.html',konteks)
    else:
        form = Formform()
        konteks ={
            'form':form,
        }
        return render(request,'tambah-data.html',konteks)

def hapus_form(request,id_form):
    isi = Formulir.objects.filter(id=id_form)
    isi.delete()

    messages.success(request,"Data berhasil di hapus")
    return redirect ('formulir')

def ubah_form(request,id_form):
    isi = Formulir.objects.get(id=id_form)
    template ='ubah-data.html'
    if request.POST:
        form = Formform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Di Ubah")
            return redirect('formulir',id_form=id_form)
    else:
        form = Formform(instance=isi)
        konteks={
            'form':form,
            'isi':isi
        }
    return render(request,template,konteks)