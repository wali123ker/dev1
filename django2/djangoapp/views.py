from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Person, Book, Hobby, UserProfile, Product
from .forms import UploadProduct
from comments.forms import CommentForm
from comments.models import Comment

@login_required(login_url="/users/login/")
def product_detail(request, pk):
    from .models import Product
    product = Product.objects.get(pk=pk)
    comments = product.comments.all().order_by('-created_at')
    form = CommentForm()
    return render(request, 'djangoapp/product_detail.html', {
        'product': product,
        'comments': comments,
        'form': form,
    })

@login_required(login_url="/users/login/")
def add_comment(request, pk):
    from .models import Product
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.product = product
            comment.save()
    return redirect('djangoapp:product_detail', pk=product.pk)

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
    
    product_list = Product.objects.all().order_by('-date_published')[:20]
    return render(request, 'djangoapp/products.html', {
        'product_list': product_list,
        'form': form
    })