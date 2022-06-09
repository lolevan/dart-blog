from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    author = models.CharField(max_length=100, verbose_name='Автор')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликованно')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Фото', blank=True)
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name='Тэг')

    class Meta:
        verbose_name = 'Публикацию'
        verbose_name_plural = 'Публикации'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})
