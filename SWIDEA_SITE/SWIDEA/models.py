from unicodedata import category
from django.db import models

# Create your models here.



class Develop(models.Model):
    title = models.CharField(verbose_name='툴 이름', max_length=50)
    cate = models.CharField(verbose_name='툴 종류', max_length=50)
    content = models.TextField(verbose_name='개발 툴 설명')
    
    def __str__(self):
        return self.title

class Idea(models.Model):
    title = models.CharField(verbose_name='아이디어 명', max_length=50)
    photo = models.ImageField(verbose_name='대표사진', blank=True, null=True, upload_to ='')
    content = models.TextField(verbose_name='아이디어 설명')
    rate = models.IntegerField(verbose_name='아이디어 관심도')
    develop = models.ForeignKey(Develop, on_delete=models.CASCADE)

    def __str__(self):
        return self.title