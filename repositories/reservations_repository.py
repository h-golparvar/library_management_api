from home.models import Reservation


def make_reservation(user, book, duration, cost, version):
    if book.version == version:
        Reservation.objects.create(user=user, book=book, duration=duration, cost=cost)
        return {'message': 'reserved successfully'}
    else:
        return {'message': 'version mismatch'}



def reserviation_filter(book=None, user=None, ):
    if book:
        reserviation = Reservation.objects.filter(book=book)

    return reserviation

