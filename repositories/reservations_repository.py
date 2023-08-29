from home.models import Reservation


def MakeReservation(user, book, duration, cost, version):
    if book.version == version:
        Reservation.objects.create(user=user, book=book, duration=duration, cost=cost)
        return {'message': 'reserved successfully'}
    else:
        return {'message': 'version mismatch'}



def ReserviationFilter(book=None, user=None, ):
    if book:
        reserviation = Reservation.objects.filter(book=book)

    return reserviation

