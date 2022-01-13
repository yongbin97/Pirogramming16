from msilib.schema import Directory
from django.db import models

class Review(models.Model):
    title = models.CharField(verbose_name='제목', max_length=100)
    year = models.CharField(verbose_name='개봉년도', max_length=10)
    genre = models.CharField(verbose_name='장르', max_length=10)
    rate = models.CharField(verbose_name='평점', max_length=10)
    time = models.CharField(verbose_name='러닝타임', max_length=10)
    content = models.TextField(verbose_name='내용')
    director = models.CharField(verbose_name='감독', max_length=20)
    actor = models.CharField(verbose_name='배우', max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
