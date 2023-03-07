from rest_framework import serializers

from service.models import Book, Author, Readers


class PhoneValidator:
    def __call__(self, value):
        if len(str(value)) != 11:
            raise serializers.ValidationError("Номер телефона должен состоять из 11 цифр")
        if str(value)[0] != "7":
            raise serializers.ValidationError("Номер телефона должен начинаться с 7")


class BookPagesValidator:
    def __call__(self, value):
        if value < 0:
            raise serializers.ValidationError("Количество страниц должно быть положительное число")


class CountBookValidator:
    def __call__(self, value):
        if value <= 0:
            raise serializers.ValidationError("Невозможно добавить книгу")


# class ReadersCountActiveBook:
#     def __call__(self, value):
#         if len(value["active_books"]) > 3:
#             raise serializers.ValidationError("Невозможно добавить более 3 книг")
#         return value


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializers(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field="last_name")
    pages = serializers.IntegerField(validators=[BookPagesValidator()])
    quantity_book = serializers.IntegerField(validators=[CountBookValidator()])

    class Meta:
        model = Book
        fields = "__all__"


class ReadersSerializers(serializers.ModelSerializer):
    active_books = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field="title", many=True)
    phone_number = serializers.IntegerField(validators=[PhoneValidator()])

    class Meta:
        model = Readers
        fields = "__all__"
