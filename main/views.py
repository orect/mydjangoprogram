from django.shortcuts import render


def index(request):
    data = {
        'title': 'Головна сторінка',
        'values': ['Some', 'Hello', '123'], # можна доавляти на сервер списки
        'obj': {
            'car': 'BWM',
            'age': 17,
            'hobby': 'coding'
        }
    }
    return render(request, 'main/index.html', data) # дозвляє не просто вивести кусочок кода а вказати який саме html шаблон

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

