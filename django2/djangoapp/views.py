from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Person, Book, Hobby, UserProfile, Product
from .forms import UploadProduct

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

@login_required(login_url="/users/login/")
def products_list(request):
    if request.method == 'POST':
        form = UploadProduct(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.user = request.user
            newpost.save()
            return redirect('djangoapp:products_list')
    else:
        form = UploadProduct()
    
    product_list = Product.objects.all()[:20]
    return render(request, 'djangoapp/products.html', {
        'product_list': product_list,
        'form': form
    })