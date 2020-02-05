from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # 统一规范，后面加/
    path('getRandomSport/', views.get_random_sport, name='get_random_sport'),
]