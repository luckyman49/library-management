from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book, Transaction

# Register your models here
admin.site.register(Book)
admin.site.register(Transaction)
