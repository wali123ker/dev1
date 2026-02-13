from django.shortcuts import render
from .models import Person, Book, Hobby, UserProfile

def home(request):
    person_list = Person.objects.all()
    return render(request, "djangoapp/home.html", {'persons': person_list})

def app_page(request):
    book_list = Book.objects.all()
    hobby_list = Hobby.objects.all()
    user_list = UserProfile.objects.all()
    return render(request, "djangoapp/app_page.html", {
        'books': book_list,
        'hobbies': hobby_list,
        'users': user_list
    })

def person(request, slug):
    my_person = Person.objects.get(slug=slug)
    return render(request, "djangoapp/person.html", {"person": my_person})
