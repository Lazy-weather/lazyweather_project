from django.db import models
from django.urls import reverse


class User(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Информация")
    photo = models.ImageField(upload_to="photos/%y/%m/%d/", verbose_name="Фото")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
    is_published = models.BooleanField(default=True, verbose_name="Статус публикации")

    def __str__(self):
        return self.title

    # Добавление кнопки "Добавить запись" в админ-панели
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Пользователи сайта'
        verbose_name_plural = 'Пользователи сайта'
