from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login',views.login, name='login'),
    path('signup',views.signup, name='signup'),
    path('mainpage',views.mainpage, name='mainpage'),
    path('logout/',views.Logoutpage, name='logout'),
    path('add-todo',views.add_todo, name='add-todo'),
    path('delete-no/<int:no>',views.delete_todo, name='delete_todo'),
    path('edit-no/<int:no>',views.edit, name='edit'),








#    path('home/',views.home, name='home'),

]

