from django.contrib import admin

from service.models import Readers, Book, Author

admin.site.register(Readers)
admin.site.register(Book)
admin.site.register(Author)
