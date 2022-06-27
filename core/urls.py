from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('accounts/register/', views.signUp.as_view(), name = 'user_registration'),
    path('password_reset', views.password_reset_request, name = 'password_reset'),
    path('<str:room_name>/', views.room, name = 'room'),
    path('logout', views.logout, name = 'logout'),    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)