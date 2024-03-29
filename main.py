import datetime

def get_days_from_today(date):
    try:
        date_datetime = datetime.datetime.strptime(date, "%Y-%m-%d")
        now = datetime.datetime.now()
        delta_date = now - date_datetime
        delta_in_days = delta_date.days
        print (delta_in_days)
    except ValueError:
        return "Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'."

get_days_from_today('2025-10-09')