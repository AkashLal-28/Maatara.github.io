from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('newsletter/',views.newsletter, name='newsletter'),
    path('cont/',views.contact, name='contact'),
    path('',views.single, name='single')
]

