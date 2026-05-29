from django.contrib import admin
from .models import Person, Hobby, Book, UserProfile, Product

admin.site.register(Person)
admin.site.register(Hobby)
admin.site.register(Book)
admin.site.register(UserProfile)
admin.site.register(Product)