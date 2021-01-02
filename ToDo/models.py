from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


'''
COLORS = (
    ('#FFD180', 'orange'),
    ('#CFD8DC', 'grey'),
    ('#FF8A80', 'red'),
    ('#CCFF90', 'green'),
    ('#FFFF8D', 'yellow'),
    ('#FFFFFF', 'white'),
    ('#80D8FF', 'blue')
)
'''

class Card(models.Model):
    user = models.ForeignKey(User, related_name='Автор', on_delete=models.CASCADE)
    title = models.CharField('Заголовок карточки', max_length=148)
    text = models.TextField('Текст карточки')
    color = models.CharField('Цвет карточки', max_length=10, blank=True)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)
    edited = models.BooleanField(default=False)
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.title[:30]