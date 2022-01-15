from django.db import models

# Create your models here.

class logo(models.Model):
    logo = models.ImageField(upload_to='logos', verbose_name='Изображение логотипа')
    def __str__(self):
        return self.logo
    class Meta:
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотипы'

class otzyv(models.Model):
    who = models.CharField(max_length=50, verbose_name='Кто оставил отзыв')
    time = models.DateTimeField(verbose_name='Время написания')
    data = models.TextField(max_length=300, verbose_name='Текст отзыва')
    showed = models.BooleanField(verbose_name='Показать на сайте')
    def __str__(self):
        return self.who
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class uslugi(models.Model):
    header = models.CharField(max_length=100, verbose_name='Заголовок карточки')
    data = models.TextField(max_length=320, verbose_name='Текст карточки')
    showed = models.BooleanField(verbose_name='Показать на сайте')
    type = models.CharField(max_length=50, verbose_name='Расположение карточки ("прав ниж", "лев ниж", "сред сред", "лев верх", "прав верх")')
    topcard = models.CharField(max_length=30, verbose_name='Надпись на лицевой стороне')
    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class news(models.Model):
    header = models.CharField(max_length=100, verbose_name='Заголовок новости')
    data = models.TextField(verbose_name='Описание новости')

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class questions(models.Model):
    question = models.TextField(max_length=250, verbose_name='Вопрос')
    answer = models.TextField(max_length=1500, verbose_name='Ответ')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос-ответ'
        verbose_name_plural = 'Вопросы-ответы'

class documents(models.Model):
    header = models.CharField(max_length=100, verbose_name='Заголовок')
    data = models.TextField(verbose_name='Текст (описать документы)')

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
