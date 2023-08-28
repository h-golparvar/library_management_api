from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import Book


@registry.register_document
class BookDocument(Document):
    author = fields.NestedField(properties={
        'id': fields.IntegerField(),
        'city_id' : fields.IntegerField(),
    })

    genre = fields.NestedField(properties={
        'id': fields.TextField(),
    })

    class Index:
        name = 'books'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Book
        fields = ['title', 'description' , 'price' ]

