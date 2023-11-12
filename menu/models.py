from django.db import models
from django.contrib import admin

# Create your models here.
class Kategori(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nama}"

    #admin.site.register(kategori)

class Produk(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    Nama_produk = models.CharField(max_length=100)
    harga = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.Nama_produk}"
    
#admin.site.register(produk)