from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="Имя")
    last_name = models.CharField(max_length=20, verbose_name="Фамилия")
    photo = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return f"Автор: {self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=40, verbose_name="Название")
    description = models.CharField(max_length=200, verbose_name="Описание")
    pages = models.PositiveSmallIntegerField(verbose_name="Количество страниц")
    author = models.ForeignKey(Author, on_delete=models.PROTECT, verbose_name="Автор")
    quantity_book = models.PositiveSmallIntegerField(verbose_name="Количество книг")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return f"Книга: {self.title} {self.description}"


class Readers(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="Имя")
    last_name = models.CharField(max_length=20, verbose_name="Фамилия")
    phone_number = models.PositiveBigIntegerField(verbose_name="Телефон")
    status = models.BooleanField(default=True, verbose_name="Статус")
    active_books = models.ManyToManyField(Book, symmetrical=False, verbose_name="Активные книги", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"

    def __str__(self):
        return f"Читатель: {self.first_name} {self.last_name}"