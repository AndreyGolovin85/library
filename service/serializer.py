from rest_framework import serializers

from service.models import Book, Author, Readers


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class ReadersSerializers(serializers.ModelSerializer):
    active_books = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field="title", many=True)

    class Meta:
        model = Readers
        fields = "__all__"
