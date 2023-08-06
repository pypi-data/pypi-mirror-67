from functools import singledispatch
from datetime import datetime

@singledispatch
def json_serialize(val):
    """Decorator used to add objects to serialization registry.
    Please see above documentation on how to use.
    """
    return str(val)

@json_serialize.register(datetime)
def json_datetime(val):
    if not val.tzinfo:
        from tzlocal import get_localzone
        tz = get_localzone()
        tz.localize(val)
    return { 'datetime': val.isoformat(), 'tz': val.tzinfo }

@singledispatch
def json_deserialize(val):
    """Decorator used to add objects to deserialization registry.
    Please see above documentation on how to use.
    """
    return val

@json_deserialize.register(datetime)
def json_datetime(val):
    from datetime import datetime
    import pytz
    dt = datetime.fromisoformat(val['datetime'])
    tz = pytz.timezone(val['tzinfo'])
    tz.localize(dt)
    return dt
