import datetime

def per_day_count_for_objects(qs, date_column='created_on', start_date=None, end_date=None):
    qs = qs.order_by(date_column).values('id', date_column)
    data = accumulate_by_key(qs, lambda u: u[date_column].date())
    data = _filter_by_date(data, start_date, end_date)
    if not start_date or not end_date:
        keys = data.keys()
        keys.sort()
        if not start_date:
            if keys:
                start_date = keys[0]
            else:
                start_date = datetime.date.today()
        if not end_date:
            if keys:
                end_date = keys[-1]
            else:
                end_date = datetime.date.today()
        keys = None
    sorted_data = []
    date = start_date - datetime.timedelta(days=1) #It's incremented before checking for data
    total = 0
    while date < end_date:
        date = date + datetime.timedelta(days=1)
        if date in data:
            sorted_data.append([date, data[date]])
            total += data[date]
        else:
            sorted_data.append([date, 0])
    return [sorted_data, total]

def accumulate_by_key(iterable, key_accessor=lambda x: x, value_accumulator=lambda x, before: (before+1)):
    """
    Keeps a running tally of values from an iterable by key.
    """
    l = {}
    for i in iterable:
        k = key_accessor(i)
        l[k] = value_accumulator(i, l.get(k, 0))
    return l

def _filter_by_date(data, start_date=None, end_date=None):
    if start_date or end_date:
        for key in data.keys():
            if start_date:
                if key < start_date:
                    del(data[key])
            if end_date:
                if key > end_date:
                    del(data[key])
    return data
