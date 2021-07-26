from django.urls import path, include
from words import views


urlpatterns = [
    path('words/', views.WordView.as_view()),
]
