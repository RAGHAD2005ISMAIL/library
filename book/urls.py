
from django.urls import path
from django.http import HttpResponse
from . import views



urlpatterns=[
 path('', views.books,name='books'),
    path('dashboard/',views.dashboard),
    path('details/<int:id>/',views.details,name='details'),
    path('home/',views.home),

]