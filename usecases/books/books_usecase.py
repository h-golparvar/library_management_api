from repositories.book_repository import GetBooks, AddBook, GetBook, DeleteBook
from home.serializers import BookSerializer


def BooksUsecase(query_params):
    query = query_params.get('query')
    max_price = query_params.get('max_price')
    min_price = query_params.get('min_price')
    author = query_params.get('author')
    genre = query_params.get('genre')
    city = query_params.get('city')
    ordering = query_params.get('ordering')

    queryset = GetBooks(
        query=query, max_price=max_price, min_price=min_price, author=author, genre=genre, city=city, ordering=ordering
    )
    return queryset


def AddBookUsecase(data):
    srz_data = BookSerializer(data=data)
    if srz_data.is_valid():
        srz_data.save()
        return srz_data.data
    else:
        return srz_data.errors


def EditBookUsecase(pk, data):
    book = GetBook(pk)
    srz_data = BookSerializer(data=data, instance=book, partial=True)
    if srz_data.is_valid():
        srz_data.save()
        return srz_data.data
    else:
        return srz_data.errors


def DeleteBookUsecase(id):
    return DeleteBook(id)