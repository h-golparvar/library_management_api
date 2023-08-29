from repositories.throttling_repository import GetLogs, AddLog, GetLastLog


def ThrottlingUsecase(ip, user_id=None, caller=''):
    last_log = GetLastLog(ip, user_id)
    if last_log and last_log.is_throttled():
        return False

    history = GetLogs(user_id=user_id, ip=ip, period='min')
    if history.count() >= 5:
        last_log = history[history.count() - 1]
        last_log.set_throttled(300)
        return False

    history = GetLogs(user_id=user_id, ip=ip, period='hour')
    if history.count() >= 10:
        last_log = history[history.count()-1]
        last_log.set_throttled(3600)
        return False

    AddLog(ip, user_id, caller)
    return True


def GetIP(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
        print(x_forwarded_for)
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
