from unicodedata import name
from django.contrib import admin
from django.urls import path
from edu_home import views

urlpatterns = [
    path('', views.InsertPageView, name='insertpage'),
    path('insert/', views.InsertData, name='insert'),
    path('show/', views.ShowPage, name='show'),
    path('update/<int:pk>',views.UpdatePage, name="update"),
    path('updated/<int:pk>',views.UpdateData, name="updated"),
    path('delete/<int:pk>',views.DeleteData, name="delete"),
]