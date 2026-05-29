from django.urls import path
from . import views

app_name = "djangoapp"

urlpatterns = [
    path('', views.home, name='home'),
    path('app/', views.app_page, name='app_page'),
    path('products/', views.products_list, name='products_list'),
    path('<slug:slug>/', views.person, name='person'),
]