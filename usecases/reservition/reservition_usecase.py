from usecases.reservition.cost_usecase import CostCalculatorUsecase
from usecases.reservition.duration_validator_usecase import DurationValidiatorUsecase
from repositories.reservations_repository import MakeReservation
from repositories.book_repository import GetBook


def ReservitionUsecase(user, book, duration):
    book = GetBook(book)
    if book.is_available:
        version = book.version
        if DurationValidiatorUsecase(user, int(duration)) != 'vlaid':
            return duration
        cost = CostCalculatorUsecase(user, duration)
        return MakeReservation(user, book, duration, cost, version)
    else:
        return {'message': 'book is not available'}

