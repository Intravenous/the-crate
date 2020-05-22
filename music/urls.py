# 'Register' all views for the app in here
# Import the type of view if not already imported and then then add the URL Pattern

from django.urls import path
from .views import ListView, DetailView

urlpatterns = [
    path('', ListView.as_view()),
    path('<int:pk>/', DetailView.as_view()),
]
