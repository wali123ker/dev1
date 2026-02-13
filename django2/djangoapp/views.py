from django.shortcuts import render
from .models import Person, Book, Hobby

def home(request):
    person_list = Person.objects.all()
    return render(request, "djangoapp/home.html", {'persons': person_list})

def app_page(request):
    book_list = Book.objects.all()
    hobby_list = Hobby.objects.all()
    return render(request, "djangoapp/app_page.html", {
        'books': book_list,
        'hobbies': hobby_list
    })
