from rest_framework import serializers
from .models import Book
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import BookDocument


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields = '__all__'


class BookDocumentSerializer(DocumentSerializer):
    class Meta:
        document = BookDocument
        fields = '__all__'
