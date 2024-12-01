from django.db import models
from django.urls import reverse


class Author(models.Model):
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, blank=True, verbose_name='Отчество')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    country = models.CharField(max_length=255, blank=True, verbose_name='Страна')

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    def get_absolute_url(self):
        return reverse('author', kwargs={'author_id': self.pk})

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    authors = models.ManyToManyField(Author, related_name='books', verbose_name='Авторы')
    publication_date = models.DateField(blank=True, null=True, verbose_name='Дата публикации')
    isbn = models.CharField(max_length=20, unique=True, blank=True, verbose_name='ISBN')
    genre = models.CharField(max_length=100, blank=True, verbose_name='Жанр')
    description = models.TextField(blank=True, verbose_name='Краткое описание')
    page_count = models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество страниц')
    publisher = models.CharField(max_length=255, blank=True, verbose_name='Издательство')
    language = models.CharField(max_length=50, blank=True, verbose_name='Язык')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book', kwargs={'book_id': self.pk})

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
