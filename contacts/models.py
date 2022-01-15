from django.db import models

# Create your models here.

class contact(models.Model):
    who = models.CharField(max_length=150)

    def __str__(self):
        return self.who
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'