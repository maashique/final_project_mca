"""pricePrediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ppApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('adminHome', views.adminHome),
    path('adminProduct', views.adminProduct),
    path('adminUsers', views.adminUsers),
    path('adminFeedback', views.adminFeedback),
    path('registration', views.registration),
    path('login/', views.login),
    path('userHome', views.userHome),
    path('userApp', views.userApp),
    path('userRem', views.userRem),
    path('userProducts', views.userProducts),
    path('favourites', views.favourites),
    path('deleteFav', views.deleteFav),
    path('compareprod', views.compareprod),
    path('feedback', views.feedback),
    path('history', views.history),
    path('prodReview', views.prodReview),
    path('deleteHistory', views.deleteHistory),
    path('addToWish', views.addToWish),
    path('notification', views.notification),

]
