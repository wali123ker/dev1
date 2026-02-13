from django.contrib import admin
from .models import Person, Book, Hobby

admin.site.register(Person)
admin.site.register(Book)
admin.site.register(Hobby)
