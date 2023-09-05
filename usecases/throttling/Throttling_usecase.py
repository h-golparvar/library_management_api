from repositories.throttling_repository import get_throttling_logs, add_throttling_log, get_last_user_throttling_log


def ThrottlingUsecase(ip, user_id=None, caller=''):
    last_log = get_last_user_throttling_log(ip, user_id)
    if last_log and last_log.is_throttled():
        return False

    history = get_throttling_logs(user_id=user_id, ip=ip, period='min')
    if history.count() >= 5:
        last_log = history[history.count() - 1]
        last_log.set_throttled(300)
        return False

    history = get_throttling_logs(user_id=user_id, ip=ip, period='hour')
    if history.count() >= 10:
        last_log = history[history.count()-1]
        last_log.set_throttled(3600)
        return False

    add_throttling_log(ip, user_id, caller)
    return True


def GetIP(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
        print(x_forwarded_for)
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
