from django.contrib import admin
from django.urls import path,include
from crud_app import views

urlpatterns = [

    path('createUser/', views.createUser, name = 'createUser'),
    path('delete/', views.deleteUser,name = 'deleteUser'),
    path('update/',views.updateUser,name = 'updateUser'),
    path('',views.viewAllUsers,name = 'viewAllUsers'),
]
