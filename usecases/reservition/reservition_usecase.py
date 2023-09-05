from usecases.reservition.cost_usecase import cost_calculator_usecase
from usecases.reservition.duration_validator_usecase import duration_validiator_usecase
from repositories.reservations_repository import make_reservation
from repositories.book_repository import get_book


def ReservitionUsecase(user, book, duration):
    book = get_book(book)
    if book.is_available:
        version = book.version
        if duration_validiator_usecase(user, int(duration)) != 'valid':
            return duration
        cost = cost_calculator_usecase(user, duration)
        return make_reservation(user, book, duration, cost, version)
    else:
        return {'message': 'book is not available'}

