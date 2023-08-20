from usecases.reservition.cost_usecase import CostCalculator
from usecases.reservition.duration_validator_usecase import DurationValidiator
from home.models import Reservation, Book
from django.shortcuts import get_object_or_404
from repositories.reservations_repository import MakeReservation


def ReservitionUsecase(user, book, duration):
    book = get_object_or_404(Book, id=book)
    if DurationValidiator(user, int(duration)) != 'vlaid':
        return duration

    cost = CostCalculator(user, duration)
    return MakeReservation(user, book, duration, cost)

