from django.urls import path
from core import views


urlpatterns = [
    path('Senami/', views.index, name = 'index'),
    path('accounts/register/', views.signUp.as_view(), name = 'user_registration'),
    path('password_reset', views.password_reset_request, name = 'password_reset'),
    path('<str:room_name>/', views.room, name = 'room'),
    path('logout', views.logout, name = 'logout'),    
    ]