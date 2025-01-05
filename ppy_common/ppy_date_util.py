from datetime import date, datetime
from math import floor

from ppy_common.ppy_data import DateData, TimeData


class DateUtil:

    @staticmethod
    def string_date_to_date(string_date: str, date_format: str = "%d/%m/%Y"):
        date_time_data = datetime.strptime(string_date, date_format)
        if date_time_data:
            return date_time_data.date()
        return None

    @staticmethod
    def string_datetime_to_datetime(string_date: str, date_format: str = "%d/%m/%Y %H:%M:%S"):
        date_time_data = datetime.strptime(string_date, date_format)
        if date_time_data:
            return date_time_data
        return None

    @staticmethod
    def diff_min_hour_day_full(previous: datetime, current: datetime = None, str_format="%d %b %Y at %H:%M:%S", date_format_after=30, day="d", hour="h", min="m") -> str:
        date_time = "1" + min
        if not current:
            current = datetime.now()

        if previous:
            difference = current - previous
            seconds = difference.total_seconds()
            if not seconds or seconds <= 0:
                return ""

            days = floor(seconds / (60 * 60 * 24))
            if 0 < days <= date_format_after:
                return str(days) + day
            elif days > date_format_after:
                return previous.strftime(str_format)

            hours = floor(seconds / (60 * 60))
            if hours > 0:
                return str(hours) + hour

            minute = floor(seconds / 60)
            if minute > 0:
                return str(minute) + min
        return date_time

    @staticmethod
    def datetime_to_format_string(date_time, date_format: str = "%d/%m/%Y", datetime_format: str = "%d/%m/%Y %H:%M:%S", default=None):
        if not date_time:
            return default
        if type(date_time) is date:
            return DateUtil.date_to_string(date_data=date_time, date_format=date_format)
        elif type(date_time) is datetime:
            return DateUtil.datetime_to_string(datetime_data=date_time, datetime_format=datetime_format)
        return default

    @staticmethod
    def date_to_string(date_data, date_format: str = "%d/%m/%Y"):
        return date_data.strftime(date_format)

    @staticmethod
    def datetime_to_string(datetime_data, datetime_format: str = "%d/%m/%Y %H:%M:%S"):
        return datetime_data.strftime(datetime_format)

    @staticmethod
    def split_data_into(input_date: date = None) -> DateData:
        if not input_date:
            input_date = date.today()
        date_data = DateData()
        date_data.year = input_date.year
        date_data.month = input_date.month
        date_data.yearShort = input_date.strftime("%y")
        date_data.monthName = input_date.strftime("%B")
        date_data.monthShort = input_date.strftime("%b")
        date_data.day = input_date.day
        date_data.weekday = input_date.strftime("%A")
        date_data.dayOfYear = input_date.strftime("%j")
        date_data.weekOfYear = input_date.strftime("%W")
        return date_data

    @staticmethod
    def split_time_into(input_datetime: datetime = None) -> TimeData:
        if not input_datetime:
            input_datetime = datetime.now()
        time_data = TimeData()
        time_data.minute = input_datetime.minute
        time_data.second = input_datetime.second
        time_data.hour12 = input_datetime.strftime("%I")
        time_data.hour24 = input_datetime.strftime("%H")
        time_data.amPm = input_datetime.strftime("%p")
        return time_data
