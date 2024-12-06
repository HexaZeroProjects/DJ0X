"""
URL configuration for myzero project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
app_name = 'newnews'  # Пространство имен для приложения newnews

urlpatterns = [
    path('', views.home, name='news_home'),  # Главная страница
    path('create_news/', views.create_news, name='add_news'),  # Создание новости
    path('news/<int:news_id>/', views.view_news, name='view_news'),  # Страница для просмотра полной новости
    path('edit_news/<int:news_id>/', views.edit_news, name='edit_news'),  # Редактирование новости
    path('delete_news/<int:news_id>/', views.delete_news, name='delete_news'),  # Удаление новости
]

