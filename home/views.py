from rest_framework.views import APIView
from .serializers import BookSerializer
from  rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import Book
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from usecases.reservition.reservition_usecase import ReservitionUsecase
from rest_framework.response import Response
from repositories.book_repository import get_books
from usecases.books.books_usecase import BooksUsecase, AddBookUsecase, EditBookUsecase, DeleteBookUsecase


class BooksListView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return BooksUsecase(self.request.query_params)


class BookEditDeleteView(APIView):
    permission_classes = [IsAdminUser]

    def put(self, request, id):
        return Response(EditBookUsecase(pk=id, data=request.data))

    def delete(self,request, id):
        return Response(DeleteBookUsecase(id))



class BookAddView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        return Response(AddBookUsecase(request.POST))


class BookReservationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return  Response(
            ReservitionUsecase(user=request.user, book=request.POST['book_id'], duration=request.POST['duration'])
        )
