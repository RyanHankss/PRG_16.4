class Time(object):

    """
    Represents the time of day.
    attributes: hour, minute, second
    """


def increment(time, seconds):
    t = Time()
    t.second += seconds
    t.minute += t.second//60
    t.hour += t.minute//60
    t.second %= 60
    t.minute %= 60
    t.hour %= 24

    return t

print increment('11', '49')
