from django.shortcuts import render

def home(request):
    return render(request, "djangoapp/home.html")

def app_page(request):
    return render(request, "djangoapp/app_page.html")

