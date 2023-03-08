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


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializers(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field="last_name")
    pages = serializers.IntegerField(validators=[BookPagesValidator()])

    class Meta:
        model = Book
        fields = "__all__"


class ReadersSerializers(serializers.ModelSerializer):
    active_books = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field="title", many=True)
    phone_number = serializers.IntegerField(validators=[PhoneValidator()])

    def validate(self, data):
        books = data.get('active_books')
        for book in books:
            if book.quantity_book == 0:
                raise serializers.ValidationError(f"Книга '{book.title}' недоступна для добавления")
        return data

    def create(self, validated_data):
        books = validated_data.pop('active_books', [])
        reader = super().create(validated_data)
        for book in books:
            book.quantity_book -= 1
            book.save()
            reader.active_books.add(book)
        return reader

    class Meta:
        model = Readers
        fields = "__all__"
