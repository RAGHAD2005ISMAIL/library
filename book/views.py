from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def books(request):
 books=[
  
    {"id": 1, "title": "Django Basics", "author": "Ali", "year": 2024},
    {"id": 2, "title": "Python Web Development", "author": "Sara", "year": 2025},
    {"id": 3, "title": "Learning APIs", "author": "Omar", "year": 2023},

  ]
 return render (request,'book/book.html',{"books":books})

def dashboard(request):
 return render(request,'book/dashboard.html')


def details(request,id):
 for book in books:
  if(book["id"]==id):
    return render(request,'book/details.html',{"book":book})

def home(request):
 return render(request,'book/home.html')