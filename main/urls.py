# main/urls.py

# Імпортуємо функцію path для створення маршрутів URL
from django.urls import path

# Імпортуємо наші перегляди (views) з файлу views.py
from . import views

# Імпортуємо налаштування проєкту та функції для роботи зі статичними файлами
from django.conf import settings
from django.conf.urls.static import static

# ============================================================
# Список маршрутів URL для додатку "main"
# ============================================================
urlpatterns = [
    # Головна сторінка
    # Коли користувач заходить на '/', викликається функція views.index
    path('', views.index, name='home'),

    # Сторінка "Про нас"
    # Коли користувач заходить на '/about/', викликається функція views.about
    path('about/', views.about, name='about'),

    # Сторінка контактів
    # Коли користувач заходить на '/contacts/', викликається функція views.contacts
    path('contacts/', views.contacts, name='contacts'),
]

# ============================================================
# Додаємо маршрути для статичних файлів (CSS, JS, зображення)
# Це потрібно, щоб Django міг їх обслуговувати під час розробки
# settings.STATIC_URL — шлях, за яким будуть доступні статичні файли
# settings.STATIC_ROOT — фізична папка, де зберігаються статичні файли
# ============================================================
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
