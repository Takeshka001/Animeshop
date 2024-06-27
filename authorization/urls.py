from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'auth'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='authorization/login.html'), name='login'),
    path('register/', views.register, name='register'),  # Новый путь для регистрации
]