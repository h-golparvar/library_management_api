from rest_framework.views import APIView
from accounts.models import User
from rest_framework.views import APIView
from .serializers import BookSerializer
from  rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import Book
from django.db.models import Q


class BooksListView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()

        if self.request.query_params.get('search') is not None:
            queryset = queryset.filter(
                Q(title__icontains=self.request.query_params.get('search')) |
                Q(description__icontains=self.request.query_params.get('search')))

        if self.request.query_params.get('max_price') is not None:
            queryset = queryset.filter(price__lte=self.request.query_params.get('max_price'))

        if self.request.query_params.get('min_price') is not None:
            queryset = queryset.filter(price__gte=self.request.query_params.get('min_price'))

        if self.request.query_params.get('genre') is not None:
            queryset = queryset.filter(genre_id=self.request.query_params.get('genre'))

        if self.request.query_params.get('city') is not None:
            queryset = queryset.filter(author__city=self.request.query_params.get('city'))

        if self.request.query_params.get('order_by') == 'ASC':
            queryset = queryset.order_by('price')
        elif self.request.query_params.get('order_by') == 'DESC':
            queryset = queryset.order_by('-price')

        return queryset


class BookEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookAddView(CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
