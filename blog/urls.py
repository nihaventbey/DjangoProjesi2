from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='post_list'), name='logout'),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # views.index fonksiyonunu çağırıyor
]