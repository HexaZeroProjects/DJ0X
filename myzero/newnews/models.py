from django.db import models
from django.contrib.auth.models import User

class Lows_post(models.Model):
    title = models.CharField('Название новости', max_length=50)
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)  # Автоматически заполняется текущей датой
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор новости', related_name='news_posts')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
