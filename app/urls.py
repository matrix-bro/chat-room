from django.urls import path
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index-page'),
    path('signup/', views.signup, name='signup-page'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login-page'),
]
