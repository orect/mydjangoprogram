# news/views.py

# ============================================================
# Імпорти необхідних модулів
# ============================================================
from django.shortcuts import render, redirect  # render — для відображення шаблонів, redirect — для перенаправлення
from .models import Articles  # Імпорт моделі статей
from .forms import ArticleForm  # Імпорт форми для створення статей
from django.views.generic import DetailView, UpdateView, DeleteView  # Клас для перегляду деталей статті
from django.shortcuts import render, get_object_or_404, redirect


# ============================================================
# Відображення головної сторінки новин
# ============================================================
def news_home(request):
    """
    Функція обробляє запит на сторінку всіх новин.
    Параметри:
    request — об'єкт HttpRequest

    Повертає:
    render — HTML-сторінку news_home.html з переданими новинами
    """
    # Отримуємо всі статті з бази даних
    news = Articles.objects.all().order_by('-date')


    # Передаємо список статей у шаблон
    return render(request, 'news/news_home.html', {'news': news})


# ============================================================
# Відображення деталей однієї статті за допомогою класу DetailView
# ============================================================
class NewsDetailView(DetailView):
    """
    Клас для відображення детальної інформації про статтю.
    Використовує шаблон details_view.html
    """
    model = Articles  # Вказуємо модель, з якої брати дані
    template_name = 'news/details_view.html'  # Шаблон для відображення
    context_object_name = 'article'  # Ім'я змінної, яка буде доступна в шаблоні

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/redact.html'

    form_class = ArticleForm


# ============================================================
# Створення нової статті
# ============================================================
def create(request):
    """
    Функція для створення нової статті через форму.
    Параметри:
    request — об'єкт HttpRequest

    Повертає:
    render — шаблон create.html з формою і повідомленням про помилку
    """
    error = ''  # Змінна для зберігання повідомлення про помилку

    # Якщо форма відправлена методом POST
    if request.method == "POST":
        form = ArticleForm(request.POST)  # Створюємо об'єкт форми з POST-даними

        # Перевіряємо валідність форми
        if form.is_valid():
            form.save()  # Зберігаємо нову статтю у базу даних
            return redirect(news_home)  # Після успішного створення перенаправляємо на сторінку новин
        else:
            error = "форма не правильна"  # Якщо форма не валідна, записуємо помилку

    # Якщо GET-запит або форма невалідна, створюємо порожню форму
    form = ArticleForm()

    # Формуємо словник з даними для шаблону
    data = {
        'form': form,
        'error': error,
    }

    # Відображаємо шаблон create.html з формою та повідомленням про помилку
    return render(request, 'news/create.html', data)

def redact(request, pk):
    """
    Функція для створення нової статті через форму.
    Параметри:
    request — об'єкт HttpRequest

    Повертає:
    render — шаблон create.html з формою і повідомленням про помилку
    """
    error = ''  # Змінна для зберігання повідомлення про помилку
    article = get_object_or_404(Articles, id=pk)

    # Якщо форма відправлена методом POST
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)  # Створюємо об'єкт форми з POST-даними

        # Перевіряємо валідність форми
        if form.is_valid():
            form.save()  # Зберігаємо нову статтю у базу даних
            return redirect(news_home)  # Після успішного створення перенаправляємо на сторінку новин
        else:
            error = "форма не правильна"  # Якщо форма не валідна, записуємо помилку
    else:
    # Якщо GET-запит або форма невалідна, створюємо порожню форму
        form = ArticleForm(instance=article)

    # Формуємо словник з даними для шаблону
    data = {
        'form': form,
        'error': error,
    }

    # Відображаємо шаблон create.html з формою та повідомленням про помилку
    return render(request, 'news/redact.html', data)



class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'

