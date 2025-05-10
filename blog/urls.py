from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # http://127.0.0.1:8000/
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # Detay sayfası
]
