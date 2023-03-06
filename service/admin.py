from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.db.models import QuerySet
from rest_framework import serializers

from service.models import Readers, Book, Author


class ReadersAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name_readers", "display_books", "phone_number", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ["first_name", "last_name"]
    actions = ["close_status", "delete_book"]

    @admin.action(description="Изменить статус")
    def close_status(self, request, queryset: QuerySet):
        count = queryset.update(status=False)
        self.message_user(request, f"Закрыто {count} читателей")

    @admin.action(description="Удаление книг")
    def delete_book(self, request, queryset: QuerySet):
        qs = queryset.objects.values_list('id', 'active_books')

        self.message_user(request, f"Здесь должны удаляться книги у читателя {qs} но я не придумал как")


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "pages", "author_link", "quantity_book", "created_at")
    list_filter = ("title", "pages", "author")
    search_fields = ["title", "author"]
    actions = ["close_status", "none_book"]

    def author_link(self, obj):
        auth = obj.author
        url = reverse("admin:service_author_changelist") + str(auth.pk)
        return format_html(f'<a href="{url}">{auth}</a>')

    @admin.action(description="Установить значение 0")
    def none_book(self, request, queryset: QuerySet):
        count = queryset.update(quantity_book=0)
        self.message_user(request, f"Изменено {count} книг")

    author_link.short_description = 'Автор'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "created_at")
    list_filter = ("first_name", "last_name", "created_at")
    search_fields = ["first_name", "last_name"]


admin.site.register(Readers, ReadersAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
