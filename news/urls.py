# news/urls.py

# Імпорт функції path для створення маршрутів URL
from django.urls import path

# Імпорт наших переглядів з файлу views.py
from . import views

# ============================================================
# Тут створюємо список маршрутів URL для додатку "news"
# ============================================================
urlpatterns = [
    # URL головної сторінки новин
    # Коли користувач заходить на 'news/', викликається функція views.news_home
    path('', views.news_home, name='news_home'),

    # URL для створення нової статті
    # Коли користувач заходить на 'news/create/', викликається функція views.create
    path('create/', views.create, name='create'),

    # URL для перегляду детальної інформації про статтю
    # '<int:pk>/' означає, що у URL передається числовий id статті
    # Деталі відображаються через клас NewsDetailView
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),

    path('<int:pk>/redact/', views.redact, name='news-redact'),
    path('<int:pk>/delete/', views.NewsDeleteView.as_view(), name='news-delete'),

]
