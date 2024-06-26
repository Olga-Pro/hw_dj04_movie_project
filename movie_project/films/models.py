from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField('Нзавание', max_length=200)
    description = models.TextField('Описание')
    review = models.TextField('Рецензия')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'