app_name = "djangoapp"

from django.urls import path, include
from .views import home, app_page, person

app_name = "djangoapp"

urlpatterns = [
    path('', home, name='home'),
    path('app/', app_page, name='app_page'),
    path('<slug:slug>/', person, name='person'),
]
