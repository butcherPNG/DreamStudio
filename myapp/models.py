from django.db import models

class Request(models.Model):
    name = models.CharField(max_length=64, verbose_name='Имя', blank=False)
    phone = models.CharField(max_length=64, verbose_name='Номер телефона',blank=False)
    date = models.DateTimeField(max_length=11, verbose_name='Дата записи', blank=True)
    message = models.TextField(max_length=256, verbose_name='Сообщение',blank=False)

    def __str__(self):
        return 'Заявка от ' + self.name

class Comment(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя', blank=False)
    message = models.TextField(max_length=256, verbose_name='Отзыв', blank=False)
    date = models.CharField(max_length=11, verbose_name='Дата отправки', blank=True)

    def __str__(self):
        return 'Комментарий от ' + self.name + ', Дата: ' + self.date