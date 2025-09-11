from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text'] # поля записані в models.py

        widgets = {
            "title": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Title",
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Anons"
            }),

            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Full Text",

            })
        }
