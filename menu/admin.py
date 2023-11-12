from django.contrib import admin
from .models import Produk, Kategori


# Register your models here.
class ProdukAdmin(admin.ModelAdmin):
    list_display = ("Nama_produk", "harga",)

admin.site.register(Produk, ProdukAdmin)
admin.site.register(Kategori)