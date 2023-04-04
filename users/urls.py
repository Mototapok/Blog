"""определяет схемы URL для пользователей"""  

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # включить URL афторизации по умолчанию
    path('', include('django.contrib.auth.urls')),
    # cтраница регистрации
    path('register/', views.register, name='register'),
]
