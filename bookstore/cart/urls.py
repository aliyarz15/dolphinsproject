
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>', views.cart, name='cart'),
    path('',views.yourcart, name='yourcart'),
    path('payment', views.payment, name='payment'),
    path('remove/<int:pk>', views.remove, name='remove'),
]