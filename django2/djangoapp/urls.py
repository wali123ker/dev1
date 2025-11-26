from django.urls import path, include
from djangoapp.views import home, app_page

urlpatterns = [
    path('', home, name='home'),
    path('app/', app_page, name='app_page'),

    path("__reload__/", include("django_browser_reload.urls")),
]
