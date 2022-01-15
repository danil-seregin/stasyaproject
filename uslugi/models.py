from django.db import models

# Create your models here.

class sootvet1(models.Model):
    slide1_header = models.CharField(max_length=100, verbose_name='Заголовок 1 слайда')
    slide1 = models.TextField(max_length=500, verbose_name='Текст 1 слайда')

    slide2_header = models.CharField(max_length=100, verbose_name='Заголовок 2 слайда')
    slide2 = models.TextField(max_length=500, verbose_name='Текст 2 слайда')

    slide3_header = models.CharField(max_length=100, verbose_name='Заголовок 3 слайда')
    slide3 = models.TextField(max_length=500, verbose_name='Текст 3 слайда')

    heading1_header = models.CharField(max_length=50, verbose_name='Заголовок содержания 1')
    heading1 = models.CharField(max_length=250, verbose_name='Описание содержания 1')

    heading2_header = models.CharField(max_length=50, verbose_name='Заголовок содержания 2')
    heading2 = models.CharField(max_length=250, verbose_name='Описание содержания 2')

    heading3_header = models.CharField(max_length=50, verbose_name='Заголовок содержания 3')
    heading3 = models.CharField(max_length=250, verbose_name='Описание содержания 3')

    featuret1_heading = models.CharField(max_length=100, verbose_name='Заголовок полного описания 1')
    featuret1 = models.TextField(max_length=600, verbose_name='Текст полного описания 1')
    featuret1_image = models.ImageField(upload_to='uslugi/f1', verbose_name='Изображение описания 1')

    featuret2_heading = models.CharField(max_length=100, verbose_name='Заголовок полного описания 2')
    featuret2 = models.TextField(max_length=600, verbose_name='Текст полного описания 2')
    featuret2_image = models.ImageField(upload_to='uslugi/f2', verbose_name='Изображение описания 2')

    featuret3_heading = models.CharField(max_length=100, verbose_name='Заголовок полного описания 3')
    featuret3 = models.TextField(max_length=600, verbose_name='Текст полного описания 3')
    featuret3_image = models.ImageField(upload_to='uslugi/f3', verbose_name='Изображение описания 3')

    def __str__(self):
        return 'Соответствие'

    class Meta:
        verbose_name = 'Сертификат подтверждения соответствия продукции'
        verbose_name_plural = 'Сертификаты подтверждения соответствия продукции'

class rad1(models.Model):
    slide1_header = models.CharField(max_length=100, verbose_name='Заголовок 1 слайда')
    slide1 = models.TextField(max_length=500, verbose_name='Текст 1 слайда')

    slide2_header = models.CharField(max_length=100, verbose_name='Заголовок 2 слайда')
    slide2 = models.TextField(max_length=500, verbose_name='Текст 2 слайда')

    slide3_header = models.CharField(max_length=100, verbose_name='Заголовок 3 слайда')
    slide3 = models.TextField(max_length=500, verbose_name='Текст 3 слайда')

    heading1_header = models.CharField(max_length=50, verbose_name='Заголовок содержания 1')
    heading1 = models.CharField(max_length=250, verbose_name='Описание содержания 1')

    heading2_header = models.CharField(max_length=50, verbose_name='Заголовок содержания 2')
    heading2 = models.CharField(max_length=250, verbose_name='Описание содержания 2')

    heading3_header = models.CharField(max_length=50, verbose_name='Заголовок содержания 3')
    heading3 = models.CharField(max_length=250, verbose_name='Описание содержания 3')

    featuret1_heading = models.CharField(max_length=100, verbose_name='Заголовок полного описания 1')
    featuret1 = models.TextField(max_length=600, verbose_name='Текст полного описания 1')
    featuret1_image = models.ImageField(upload_to='uslugi/f1', verbose_name='Изображение описания 1')

    featuret2_heading = models.CharField(max_length=100, verbose_name='Заголовок полного описания 2')
    featuret2 = models.TextField(max_length=600, verbose_name='Текст полного описания 2')
    featuret2_image = models.ImageField(upload_to='uslugi/f2', verbose_name='Изображение описания 2')

    featuret3_heading = models.CharField(max_length=100, verbose_name='Заголовок полного описания 3')
    featuret3 = models.TextField(max_length=600, verbose_name='Текст полного описания 3')
    featuret3_image = models.ImageField(upload_to='uslugi/f3', verbose_name='Изображение описания 3')

    def __str__(self):
        return 'Радиационная обстановка'

    class Meta:
        verbose_name = 'Сертификат контроля радиационной обстановки'
        verbose_name_plural = 'Сертификаты контроля радиационной обстановки'

class prombez1(models.Model):
    slide1_header = models.CharField(max_length=100, verbose_name='Заголовок 1 слайда')
    slide1 = models.TextField(max_length=500, verbose_name='Текст 1 слайда')

    slide2_header = models.CharField(max_length=100, verbose_name='Заголовок 2 слайда')
    slide2 = models.TextField(max_length=500, verbose_name='Текст 2 слайда')

    slide3_header = models.CharField(max_length=100, verbose_name='Заголовок 3 слайда')
    slide3 = models.TextField(max_length=500, verbose_name='Текст 3 слайда')

    heading1_header = models.CharField(max_length=50, verbose_name='Заголовок содержания 1')
    heading1 = models.CharField(max_length=250, verbose_name='Описание содержания 1')

    heading2_header = models.CharField(max_length=50, verbose_name='Заголовок содержания 2')
    heading2 = models.CharField(max_length=250, verbose_name='Описание содержания 2')

    heading3_header = models.CharField(max_length=50, verbose_name='Заголовок содержания 3')
    heading3 = models.CharField(max_length=250, verbose_name='Описание содержания 3')

    featuret1_heading = models.CharField(max_length=100, verbose_name='Заголовок полного описания 1')
    featuret1 = models.TextField(max_length=600, verbose_name='Текст полного описания 1')
    featuret1_image = models.ImageField(upload_to='uslugi/f1', verbose_name='Изображение описания 1')

    featuret2_heading = models.CharField(max_length=100, verbose_name='Заголовок полного описания 2')
    featuret2 = models.TextField(max_length=600, verbose_name='Текст полного описания 2')
    featuret2_image = models.ImageField(upload_to='uslugi/f2', verbose_name='Изображение описания 2')

    featuret3_heading = models.CharField(max_length=100, verbose_name='Заголовок полного описания 3')
    featuret3 = models.TextField(max_length=600, verbose_name='Текст полного описания 3')
    featuret3_image = models.ImageField(upload_to='uslugi/f3', verbose_name='Изображение описания 3')

    def __str__(self):
        return 'Промбезопасность'

    class Meta:
        verbose_name = 'Сертификат промышленной безопасности'
        verbose_name_plural = 'Сертификаты промышленной безопасности '


class ispyt1(models.Model):
    slide1_header = models.CharField(max_length=100, verbose_name='Заголовок 1 слайда')
    slide1 = models.TextField(max_length=500, verbose_name='Текст 1 слайда')

    slide2_header = models.CharField(max_length=100, verbose_name='Заголовок 2 слайда')
    slide2 = models.TextField(max_length=500, verbose_name='Текст 2 слайда')

    slide3_header = models.CharField(max_length=100, verbose_name='Заголовок 3 слайда')
    slide3 = models.TextField(max_length=500, verbose_name='Текст 3 слайда')

    heading1_header = models.CharField(max_length=50, verbose_name='Заголовок содержания 1')
    heading1 = models.CharField(max_length=250, verbose_name='Описание содержания 1')

    heading2_header = models.CharField(max_length=50, verbose_name='Заголовок содержания 2')
    heading2 = models.CharField(max_length=250, verbose_name='Описание содержания 2')

    heading3_header = models.CharField(max_length=50, verbose_name='Заголовок содержания 3')
    heading3 = models.CharField(max_length=250, verbose_name='Описание содержания 3')

    featuret1_heading = models.CharField(max_length=100, verbose_name='Заголовок полного описания 1')
    featuret1 = models.TextField(max_length=600, verbose_name='Текст полного описания 1')
    featuret1_image = models.ImageField(upload_to='uslugi/f1', verbose_name='Изображение описания 1')

    featuret2_heading = models.CharField(max_length=100, verbose_name='Заголовок полного описания 2')
    featuret2 = models.TextField(max_length=600, verbose_name='Текст полного описания 2')
    featuret2_image = models.ImageField(upload_to='uslugi/f2', verbose_name='Изображение описания 2')

    featuret3_heading = models.CharField(max_length=100, verbose_name='Заголовок полного описания 3')
    featuret3 = models.TextField(max_length=600, verbose_name='Текст полного описания 3')
    featuret3_image = models.ImageField(upload_to='uslugi/f3', verbose_name='Изображение описания 3')

    def __str__(self):
        return 'Испытание продукции'

    class Meta:
        verbose_name = 'Сертификат испытания продукции'
        verbose_name_plural = 'Сертификаты испытания продукции'

class iso1(models.Model):
    slide1_header = models.CharField(max_length=100, verbose_name='Заголовок 1 слайда')
    slide1 = models.TextField(max_length=500, verbose_name='Текст 1 слайда')

    slide2_header = models.CharField(max_length=100, verbose_name='Заголовок 2 слайда')
    slide2 = models.TextField(max_length=500, verbose_name='Текст 2 слайда')

    slide3_header = models.CharField(max_length=100, verbose_name='Заголовок 3 слайда')
    slide3 = models.TextField(max_length=500, verbose_name='Текст 3 слайда')

    heading1_header = models.CharField(max_length=50, verbose_name='Заголовок содержания 1')
    heading1 = models.CharField(max_length=250, verbose_name='Описание содержания 1')

    heading2_header = models.CharField(max_length=50, verbose_name='Заголовок содержания 2')
    heading2 = models.CharField(max_length=250, verbose_name='Описание содержания 2')

    heading3_header = models.CharField(max_length=50, verbose_name='Заголовок содержания 3')
    heading3 = models.CharField(max_length=250, verbose_name='Описание содержания 3')

    featuret1_heading = models.CharField(max_length=100, verbose_name='Заголовок полного описания 1')
    featuret1 = models.TextField(max_length=600, verbose_name='Текст полного описания 1')
    featuret1_image = models.ImageField(upload_to='uslugi/f1', verbose_name='Изображение описания 1')

    featuret2_heading = models.CharField(max_length=100, verbose_name='Заголовок полного описания 2')
    featuret2 = models.TextField(max_length=600, verbose_name='Текст полного описания 2')
    featuret2_image = models.ImageField(upload_to='uslugi/f2', verbose_name='Изображение описания 2')

    featuret3_heading = models.CharField(max_length=100, verbose_name='Заголовок полного описания 3')
    featuret3 = models.TextField(max_length=600, verbose_name='Текст полного описания 3')
    featuret3_image = models.ImageField(upload_to='uslugi/f3', verbose_name='Изображение описания 3')

    def __str__(self):
        return 'Сертификат ISO'

    class Meta:
        verbose_name = 'Сертификат ISO'
        verbose_name_plural = 'Сертификаты ISO'

class ates1(models.Model):
    slide1_header = models.CharField(max_length=100, verbose_name='Заголовок 1 слайда')
    slide1 = models.TextField(max_length=500, verbose_name='Текст 1 слайда')

    slide2_header = models.CharField(max_length=100, verbose_name='Заголовок 2 слайда')
    slide2 = models.TextField(max_length=500, verbose_name='Текст 2 слайда')

    slide3_header = models.CharField(max_length=100, verbose_name='Заголовок 3 слайда')
    slide3 = models.TextField(max_length=500, verbose_name='Текст 3 слайда')

    heading1_header = models.CharField(max_length=50, verbose_name='Заголовок содержания 1')
    heading1 = models.CharField(max_length=250, verbose_name='Описание содержания 1')

    heading2_header = models.CharField(max_length=50, verbose_name='Заголовок содержания 2')
    heading2 = models.CharField(max_length=250, verbose_name='Описание содержания 2')

    heading3_header = models.CharField(max_length=50, verbose_name='Заголовок содержания 3')
    heading3 = models.CharField(max_length=250, verbose_name='Описание содержания 3')

    featuret1_heading = models.CharField(max_length=100, verbose_name='Заголовок полного описания 1')
    featuret1 = models.TextField(max_length=600, verbose_name='Текст полного описания 1')
    featuret1_image = models.ImageField(upload_to='uslugi/f1', verbose_name='Изображение описания 1')

    featuret2_heading = models.CharField(max_length=100, verbose_name='Заголовок полного описания 2')
    featuret2 = models.TextField(max_length=600, verbose_name='Текст полного описания 2')
    featuret2_image = models.ImageField(upload_to='uslugi/f2', verbose_name='Изображение описания 2')

    featuret3_heading = models.CharField(max_length=100, verbose_name='Заголовок полного описания 3')
    featuret3 = models.TextField(max_length=600, verbose_name='Текст полного описания 3')
    featuret3_image = models.ImageField(upload_to='uslugi/f3', verbose_name='Изображение описания 3')

    def __str__(self):
        return 'Атестация продукции'

    class Meta:
        verbose_name = 'Сертификат атестации производственных объектов'
        verbose_name_plural = 'Сертификаты атестации производственных объектов'

class center1(models.Model):
    slide1_header = models.CharField(max_length=100, verbose_name='Заголовок 1 слайда')
    slide1 = models.TextField(max_length=500, verbose_name='Текст 1 слайда')

    slide2_header = models.CharField(max_length=100, verbose_name='Заголовок 2 слайда')
    slide2 = models.TextField(max_length=500, verbose_name='Текст 2 слайда')

    slide3_header = models.CharField(max_length=100, verbose_name='Заголовок 3 слайда')
    slide3 = models.TextField(max_length=500, verbose_name='Текст 3 слайда')

    heading1_header = models.CharField(max_length=50, verbose_name='Заголовок содержания 1')
    heading1 = models.CharField(max_length=250, verbose_name='Описание содержания 1')

    heading2_header = models.CharField(max_length=50, verbose_name='Заголовок содержания 2')
    heading2 = models.CharField(max_length=250, verbose_name='Описание содержания 2')

    heading3_header = models.CharField(max_length=50, verbose_name='Заголовок содержания 3')
    heading3 = models.CharField(max_length=250, verbose_name='Описание содержания 3')

    featuret1_heading = models.CharField(max_length=100, verbose_name='Заголовок полного описания 1')
    featuret1 = models.TextField(max_length=600, verbose_name='Текст полного описания 1')
    featuret1_image = models.ImageField(upload_to='uslugi/f1', verbose_name='Изображение описания 1')

    featuret2_heading = models.CharField(max_length=100, verbose_name='Заголовок полного описания 2')
    featuret2 = models.TextField(max_length=600, verbose_name='Текст полного описания 2')
    featuret2_image = models.ImageField(upload_to='uslugi/f2', verbose_name='Изображение описания 2')

    featuret3_heading = models.CharField(max_length=100, verbose_name='Заголовок полного описания 3')
    featuret3 = models.TextField(max_length=600, verbose_name='Текст полного описания 3')
    featuret3_image = models.ImageField(upload_to='uslugi/f3', verbose_name='Изображение описания 3')

    def __str__(self):
        return 'Испытательный центр'

    class Meta:
        verbose_name = 'Испытательный центр'
        verbose_name_plural = 'Испытательный центр'

class applications(models.Model):
    name = models.CharField(max_length=150, verbose_name='Кто оставил сообщение')
    contacts = models.CharField(max_length=150, verbose_name='Контакты')
    text = models.TextField(max_length=1500, verbose_name='Текст сообщения')
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
