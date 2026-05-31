from django.urls import path
from . import views

app_name = "djangoapp"

urlpatterns = [
    path('', views.home, name='home'),
    path('app/', views.app_page, name='app_page'),
    path('products/', views.products_list, name='products_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),      # NUEVO
    path('products/<int:pk>/comment/', views.add_comment, name='add_comment'),    # NUEVO
    path('<slug:slug>/', views.person, name='person'),
]