# news/forms.py

# ============================================================
# Імпорт моделі Articles з файлу models.py
# ============================================================
from .models import Articles

# Імпорт необхідних класів для створення форм Django
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

# ============================================================
# Форма для створення та редагування статей
# ============================================================
class ArticleForm(ModelForm):
    """
    Форма на основі моделі Articles.
    Використовується для створення або редагування новин.
    """

    class Meta:
        # Вказуємо модель, на основі якої будується форма
        model = Articles

        # Поля моделі, які будуть доступні у формі
        fields = ['title', 'anons', 'full_text']

        # Вказуємо віджети для кожного поля форми
        # Віджети дозволяють налаштувати HTML-елементи форми
        widgets = {
            # Поле title буде текстовим інпутом з класом Bootstrap та підказкою
            "title": TextInput(attrs={
                'class': "form-control",      # CSS-клас для стилізації через Bootstrap
                'placeholder': "Title",       # Підказка у полі вводу
            }),

            # Поле anons також текстовий інпут
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Anons"
            }),

            # Поле full_text — textarea для довгого тексту
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Full Text",
            })
        }
