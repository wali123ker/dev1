from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('<slug:room_name>/', views.game_play, name='game_play'),
    path('<slug:room_name>/delete/', views.game_delete, name='game_delete'),
]