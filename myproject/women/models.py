from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Текст статті')
    photo = models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Час створення')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Час внесення змін')
    is_published = models.BooleanField(default=True, verbose_name='Публікація')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категорія')
    user = models.ForeignKey(User, verbose_name='Користувач', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Відомі жінки'
        verbose_name_plural = 'Відомі жінки'
        ordering = ['time_create', 'title']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категорія')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категорію'
        verbose_name_plural = 'Категорії'
        ordering = ['id']