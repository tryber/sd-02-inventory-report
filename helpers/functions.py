from datetime import datetime, timedelta


def get_extension(path):
    return path.split(".").pop()


def get_elements(data, field):
    return [each[field] for each in data]


def get_nearest_date(dates):
    current_date = datetime.today()
    no_expired_dates = [each_date for each_date in dates if datetime.strptime(
        each_date, '%Y-%m-%d') > current_date]
    return min(no_expired_dates, key=lambda each_date: datetime.strptime(each_date, '%Y-%m-%d') - current_date)
