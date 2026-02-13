from django.contrib import admin
from .models import Person, Book, Hobby
from .models import UserProfile

admin.site.register(UserProfile)
admin.site.register(Person)
admin.site.register(Book)
admin.site.register(Hobby)
