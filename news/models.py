from django.db import models

# Create your models here.
# вивід з БД інфрмації:

class Articles(models.Model):
    title = models.CharField('Назва', max_length=50, default="")
    anons = models.CharField('Анонс', max_length=250, default="")
    full_text = models.TextField('Стаття')


    def __str__(self): # цей метод допомгає красиво виводити з бази данних текст
        return f'Новина: {self.title}'


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'




