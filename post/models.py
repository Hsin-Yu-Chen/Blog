from django.db import models

# Create your models here.
class Post(models.Model):
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
    title = models.CharField('標題', max_length=20, )
    content = models.CharField('內容', max_length=200)