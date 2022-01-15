from django.db import models

# Create your models here.
class questionsbig(models.Model):
    question = models.TextField(max_length=250, verbose_name='Вопрос')
    answer = models.TextField(max_length=1500, verbose_name='Ответ')
    type = models.CharField(max_length=200, verbose_name='Тип вопросов (указывает блок вопрос-ответов)')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Вопрос-ответ'
        verbose_name_plural = 'Вопросы-ответы'
