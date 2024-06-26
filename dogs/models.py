from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Порода')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'порода'
        verbose_name_plural = 'породы'


class Dog(models.Model):
    name = models.CharField(max_length=200, verbose_name='Кличка')
    # category = models.CharField(max_length=200, verbose_name='Порода')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Порода', **NULLABLE)
    photo = models.ImageField(upload_to='dogs/', **NULLABLE, verbose_name='фото')
    birth_day = models.DateField(**NULLABLE, verbose_name='Дата рождения')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')
    is_pablic = models.BooleanField(default=False)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_likes')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'собака'
        verbose_name_plural = 'собаки'
