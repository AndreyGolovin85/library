from rest_framework.viewsets import ModelViewSet

from service.models import Author, Book, Readers
from service.serializer import AuthorSerializers, BookSerializers, ReadersSerializers


class AuthorsViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers


class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class ReadersViewSet(ModelViewSet):
    queryset = Readers.objects.all()
    serializer_class = ReadersSerializers
