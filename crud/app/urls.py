from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('getdetails/', views.getdetails),
    path('update/<int:id>', views.update),
]
