from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser

from service.models import Author, Book, Readers
from service.serializer import AuthorSerializers, BookSerializers, ReadersSerializers
from service.permissions import PermissionPolicyMixin, PermissionReader


class AuthorsViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    permission_classes_per_method = {
        'list': [AllowAny],
        'create': [IsAdminUser],
        'update': [IsAdminUser],
        'destroy': [IsAdminUser],
        'retrieve': [AllowAny]
    }


class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes_per_method = {
        'list': [AllowAny],
        'create': [IsAdminUser],
        'update': [IsAdminUser],
        'destroy': [IsAdminUser],
        'retrieve': [AllowAny]
    }


class ReadersViewSet(ModelViewSet):
    queryset = Readers.objects.all()
    serializer_class = ReadersSerializers
    permission_classes_per_method = {
        'list': [IsAdminUser],
        'create': [AllowAny],
        'update': [PermissionReader],
        'destroy': [PermissionReader],
        'retrieve': [PermissionReader]
    }
