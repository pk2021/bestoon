from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path(r'submit/expense/', views.submit_expense, name='submit_expense'),
]
