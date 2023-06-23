from django.contrib import admin
from .models import Seller, SalesTransaction

# Register your models here.
admin.site.register(Seller)
admin.site.register(SalesTransaction)
