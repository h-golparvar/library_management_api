from home.models import Reservation


def MakeReservation(user, book, duration, cost):
    if book.is_available:
        Reservation.objects.create(user=user, book=book, duration=duration, cost=cost)
        return {'message': 'reserved successfully'}
    else:
        return {'message': 'book is not available'}


def ReserviationFilter(book=None, user=None, ):
    if book:
        reserviation = Reservation.objects.filter(book=book)

    return reserviation

