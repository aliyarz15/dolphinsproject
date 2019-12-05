from django.shortcuts import render, redirect
from .models import Cart
from books.models import Book
from django.db.models import Sum

sums_of_cart = Cart.objects.aggregate(Sum('price'))

bools = [False, False, False]

def cart(request, pk):
    books = Book.objects.get(pk=pk)
#    or Cart.objects.count()!=0
    if Cart.objects.filter(name=books.name).exists():
        bools.append(True)
        return redirect('/')
    else:
        cart = Cart(name=books.name, image=books.image, price=books.price, content=books.content)
        cart.save()
        return redirect('home')

def yourcart(request):
    sums_of_cart = Cart.objects.aggregate(Sum('price'))
    carts = Cart.objects.all()
    return render(request, 'cart/cart.html', {'carts': carts, 'sum': sums_of_cart})

def payment(request):
    sums_of_cart = Cart.objects.aggregate(Sum('price'))
    return render(request, 'cart/payment.html', {'sum':sums_of_cart} )

def remove(request, pk):
    cart = Cart.objects.get(pk=pk).delete()
    return redirect('yourcart')

