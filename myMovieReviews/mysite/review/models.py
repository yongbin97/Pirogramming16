from msilib.schema import Directory
from django.db import models

class Review(models.Model):
    action = '액션'
    drama = '드라마'
    fantasy = '판타지'
    comedy = '코미디'
    animation = '애니메이션'

    title = models.CharField(verbose_name='제목', max_length=100)
    year = models.CharField(verbose_name='개봉년도', max_length=10)
    GENRE_IN_CHOICES = (
        (action, '액션'),
        (drama, '드라마'),
        (fantasy, '판타지'),
        (comedy, '코미디'),
        (animation, '애니메이션')
    )

    genre = models.CharField(verbose_name='장르', max_length=10, choices=GENRE_IN_CHOICES, default=action)

    rate = models.FloatField(verbose_name='평점', max_length=10)
    time = models.CharField(verbose_name='러닝타임', max_length=10)
    content = models.TextField(verbose_name='내용')
    director = models.CharField(verbose_name='감독', max_length=20)
    actor = models.CharField(verbose_name='배우', max_length=20)

    photo = models.ImageField(verbose_name='사진', blank=True, null=True, upload_to="")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
