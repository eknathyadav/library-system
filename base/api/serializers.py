from rest_framework import serializers
from base.models import Book


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
