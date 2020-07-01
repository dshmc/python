"""Определяет схемы URL для Learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),

    # Страница со списком всех тем.
    path('topics/', views.topics, name='topics'),
]