"""
Конфигурация Blogeng URL

Список `urlpatterns` направляет URL-адреса к представлениям. Для получения дополнительной информации, пожалуйста, смотрите:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Примеры:
Функциональные представления
    1. Добавить импорт: из представлений импорта my_app
    2. Добавьте URL в urlpatterns: путь ('', views.home, name = 'home')
Основанные на классе представления
    1. Добавить импорт: из other_app.views import Home
    2. Добавьте URL в urlpatterns: путь ('', Home.as_view (), name = 'home')
Включая другой URLconf
    1. Импортируйте функцию include (): из django.urls импортируйте include, путь
    2. Добавьте URL в urlpatterns: path ('blog /', include ('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # обращайемся к файлу URLS в приложении BLOG
    path('blog/', include('blog.urls')),
]
