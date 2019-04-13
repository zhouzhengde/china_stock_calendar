from datetime import time
from pytz import timezone
from zipline.utils.calendars import TradingCalendar
from trading_calendars.trading_calendar import HolidayCalendar
from china_stock_calendar.data import holiday_set


class SHSZCalendar(TradingCalendar):
    open_times = (
        (None, time(0)),
    )
    close_times = (
        (None, time(23, 59)),
    )

    @property
    def name(self):
        return "SHSZ"

    @property
    def tz(self):
        return timezone("Asia/Shanghai")

    @property
    def regular_holidays(self):
        return HolidayCalendar(holiday_set)


if __name__ == '__main__':
    SHSZCalendar()
