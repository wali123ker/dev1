from django.shortcuts import render
def djangoapp(request):
 return render(request, 'djangoapp/home.html')
