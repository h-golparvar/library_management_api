from home.documents import BookDocument
from home.serializers import BookDocumentSerializer
from elasticsearch_dsl.query import Q
from home.models import Book
from django.shortcuts import get_object_or_404


def get_book(id):
    return get_object_or_404(Book, id=id)


def get_books(query=None, max_price=None, min_price=None, author=None, genre=None, city=None, ordering=None):
    if query is not None:
        books = BookDocument.search().query('multi_match', query=query, fields=['title','description'])
    else:
        books = BookDocument.search().query('match_all')

    books = books.filter('range', price={'gt':min_price, 'lt':max_price})
    if author is not None:
        query = Q('nested', path='author', query=Q('term', **{'author.id':author}))
        books = books.query(query)

    if genre is not None:
        query = Q('nested', path='genre', query=Q('term', **{'genre.id':genre}))
        books = books.query(query)

    if city is not None:
        query = Q('nested', path='author',query=Q('term', **{'author.city_id':city}))
        books = books.query(query)

    if ordering == 'asc':
        books = books.sort({'price' : {'order' : 'asc'}})
    elif ordering == 'desc':
        books = books.sort({'price' : {'order' : 'desc'}})

    data = []
    for book in books:
        data.append( {
                "id": book.meta.id,
                "title": book.title,
                "description": book.description,
                "price": book.price,
                "genre": book.genre.id,
                "author": [
                    book.author[0]['id']
                ]
                })

    return books.to_queryset()


def delete_book(id):
    book = get_book(id)
    if book:
        book.delete()
        return {'message': 'book deleted'}
    else:
        return {'message': 'book not found'}


def add_book(title, description, author, genre, price, publication=None, shabak=None):
    book = Book.objects.create(
        title=title,
        description=description,
        author=author,
        genre=genre,
        publication=publication,
        shabak=shabak,
        price=price)


