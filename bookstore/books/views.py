from django.shortcuts import render
from .models import Book
from django.views import generic
from django.db.models import Q
from cart.models import Cart

def home(request):
    num = Cart.objects.all().count()
    search_query =request.GET.get('search1', '')

    if search_query:
        books = Book.objects.filter(Q(name__icontains=search_query) | Q(content__icontains=search_query))
    else:
        books = Book.objects.all()
    return render(request, 'homme.html', {'books':books, 'num':num})

def adventure(request):
    title = "Adventure"
    books = Book.objects.filter(category__name="Adventure")
    return render(request, 'home.html', {'books':books, 'title':title})

def action(request):
    title = "Action"
    books = Book.objects.filter(category__name="Action")
    return render(request, 'home.html', {'books':books, 'title':title})

def drama(request):
    title = "Drama"
    books = Book.objects.filter(category__name="Drama")
    return render(request, 'home.html', {'books':books, 'title':title})

def romance(request):
    title = "Romance"
    books = Book.objects.filter(category__name="Romance")
    return render(request, 'home.html', {'books':books, 'title':title})

def horror(request):
    title = "Horror"
    books = Book.objects.filter(category__name="Horror")
    return render(request, 'home.html', {'books':books, 'title':title})

def mystery(request):
    title = "Mystery"
    books = Book.objects.filter(category__name="Mystery")
    return render(request, 'home.html', {'books': books, 'title':title})

def thriller(request):
    title = "Thriller"
    books = Book.objects.filter(category__name="Thriller")
    return render(request, 'home.html', {'books': books, 'title':title})

def fantasy(request):
    title = "Fantasy"
    books = Book.objects.filter(category__name="Fantasy")
    return render(request, 'home.html', {'books': books, 'title':title})

class detail(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'