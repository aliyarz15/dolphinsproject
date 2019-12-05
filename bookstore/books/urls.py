from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:pk>', views.detail.as_view(), name='detail'),
    path('adventure', views.adventure, name='adventure'),
    path('action', views.action, name='action'),
    path('drama', views.drama, name='drama'),
    path('romance', views.romance, name='romance'),
    path('horror', views.horror, name='horror'),
    path('mystery', views.mystery, name='mystery'),
    path('thriller', views.thriller, name='thriller'),
    path('fantasy', views.fantasy, name='fantasy'),
]