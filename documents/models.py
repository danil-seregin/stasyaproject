from django.db import models

# Create your models here.

class sertificates(models.Model):
    image = models.ImageField(upload_to='documents', verbose_name='Изображение')
    type = models.CharField(max_length=150, verbose_name='Тип сертификата (указывает вкладку для сертификатов)')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'