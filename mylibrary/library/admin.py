from django.contrib import admin
from library.models import Book, Reader, BookRent

# Register your models here.

admin.site.register(Book)
admin.site.register(Reader)
admin.site.register(BookRent)

