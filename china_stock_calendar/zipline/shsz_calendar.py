from datetime import time
from pytz import timezone
from trading_calendars import TradingCalendar
from pandas.tseries.holiday import (
    Holiday
)
from trading_calendars.trading_calendar import HolidayCalendar

Holiday_20150101 = Holiday("Holiday_20150101", month=1, day=1, year=2015)
Holiday_20150102 = Holiday("Holiday_20150102", month=1, day=2, year=2015)
Holiday_20150218 = Holiday("Holiday_20150218", month=2, day=18, year=2015)
Holiday_20150219 = Holiday("Holiday_20150219", month=2, day=19, year=2015)
Holiday_20150220 = Holiday("Holiday_20150220", month=2, day=20, year=2015)
Holiday_20150223 = Holiday("Holiday_20150223", month=2, day=23, year=2015)
Holiday_20150224 = Holiday("Holiday_20150224", month=2, day=24, year=2015)
Holiday_20150406 = Holiday("Holiday_20150406", month=4, day=6, year=2015)
Holiday_20150501 = Holiday("Holiday_20150501", month=5, day=1, year=2015)
Holiday_20150622 = Holiday("Holiday_20150622", month=6, day=22, year=2015)
Holiday_20150903 = Holiday("Holiday_20150903", month=9, day=3, year=2015)
Holiday_20150904 = Holiday("Holiday_20150904", month=9, day=4, year=2015)
Holiday_20151001 = Holiday("Holiday_20151001", month=10, day=1, year=2015)
Holiday_20151002 = Holiday("Holiday_20151002", month=10, day=2, year=2015)
Holiday_20151005 = Holiday("Holiday_20151005", month=10, day=5, year=2015)
Holiday_20151006 = Holiday("Holiday_20151006", month=10, day=6, year=2015)
Holiday_20151007 = Holiday("Holiday_20151007", month=10, day=7, year=2015)
Holiday_20160101 = Holiday("Holiday_20160101", month=1, day=1, year=2016)
Holiday_20160208 = Holiday("Holiday_20160208", month=2, day=8, year=2016)
Holiday_20160209 = Holiday("Holiday_20160209", month=2, day=9, year=2016)
Holiday_20160210 = Holiday("Holiday_20160210", month=2, day=10, year=2016)
Holiday_20160211 = Holiday("Holiday_20160211", month=2, day=11, year=2016)
Holiday_20160212 = Holiday("Holiday_20160212", month=2, day=12, year=2016)
Holiday_20160404 = Holiday("Holiday_20160404", month=4, day=4, year=2016)
Holiday_20160502 = Holiday("Holiday_20160502", month=5, day=2, year=2016)
Holiday_20160609 = Holiday("Holiday_20160609", month=6, day=9, year=2016)
Holiday_20160610 = Holiday("Holiday_20160610", month=6, day=10, year=2016)
Holiday_20160915 = Holiday("Holiday_20160915", month=9, day=15, year=2016)
Holiday_20160916 = Holiday("Holiday_20160916", month=9, day=16, year=2016)
Holiday_20161003 = Holiday("Holiday_20161003", month=10, day=3, year=2016)
Holiday_20161004 = Holiday("Holiday_20161004", month=10, day=4, year=2016)
Holiday_20161005 = Holiday("Holiday_20161005", month=10, day=5, year=2016)
Holiday_20161006 = Holiday("Holiday_20161006", month=10, day=6, year=2016)
Holiday_20161007 = Holiday("Holiday_20161007", month=10, day=7, year=2016)
Holiday_20170102 = Holiday("Holiday_20170102", month=1, day=2, year=2017)
Holiday_20170127 = Holiday("Holiday_20170127", month=1, day=27, year=2017)
Holiday_20170130 = Holiday("Holiday_20170130", month=1, day=30, year=2017)
Holiday_20170131 = Holiday("Holiday_20170131", month=1, day=31, year=2017)
Holiday_20170201 = Holiday("Holiday_20170201", month=2, day=1, year=2017)
Holiday_20170202 = Holiday("Holiday_20170202", month=2, day=2, year=2017)
Holiday_20170403 = Holiday("Holiday_20170403", month=4, day=3, year=2017)
Holiday_20170404 = Holiday("Holiday_20170404", month=4, day=4, year=2017)
Holiday_20170501 = Holiday("Holiday_20170501", month=5, day=1, year=2017)
Holiday_20170529 = Holiday("Holiday_20170529", month=5, day=29, year=2017)
Holiday_20170530 = Holiday("Holiday_20170530", month=5, day=30, year=2017)
Holiday_20171002 = Holiday("Holiday_20171002", month=10, day=2, year=2017)
Holiday_20171003 = Holiday("Holiday_20171003", month=10, day=3, year=2017)
Holiday_20171004 = Holiday("Holiday_20171004", month=10, day=4, year=2017)
Holiday_20171005 = Holiday("Holiday_20171005", month=10, day=5, year=2017)
Holiday_20171006 = Holiday("Holiday_20171006", month=10, day=6, year=2017)
Holiday_20180101 = Holiday("Holiday_20180101", month=1, day=1, year=2018)
Holiday_20180215 = Holiday("Holiday_20180215", month=2, day=15, year=2018)
Holiday_20180216 = Holiday("Holiday_20180216", month=2, day=16, year=2018)
Holiday_20180219 = Holiday("Holiday_20180219", month=2, day=19, year=2018)
Holiday_20180220 = Holiday("Holiday_20180220", month=2, day=20, year=2018)
Holiday_20180221 = Holiday("Holiday_20180221", month=2, day=21, year=2018)
Holiday_20180405 = Holiday("Holiday_20180405", month=4, day=5, year=2018)
Holiday_20180406 = Holiday("Holiday_20180406", month=4, day=6, year=2018)
Holiday_20180430 = Holiday("Holiday_20180430", month=4, day=30, year=2018)
Holiday_20180501 = Holiday("Holiday_20180501", month=5, day=1, year=2018)
Holiday_20180618 = Holiday("Holiday_20180618", month=6, day=18, year=2018)
Holiday_20180924 = Holiday("Holiday_20180924", month=9, day=24, year=2018)
Holiday_20181001 = Holiday("Holiday_20181001", month=10, day=1, year=2018)
Holiday_20181002 = Holiday("Holiday_20181002", month=10, day=2, year=2018)
Holiday_20181003 = Holiday("Holiday_20181003", month=10, day=3, year=2018)
Holiday_20181004 = Holiday("Holiday_20181004", month=10, day=4, year=2018)
Holiday_20181005 = Holiday("Holiday_20181005", month=10, day=5, year=2018)
Holiday_20181231 = Holiday("Holiday_20181231", month=12, day=31, year=2018)
Holiday_20190101 = Holiday("Holiday_20190101", month=1, day=1, year=2019)
Holiday_20190204 = Holiday("Holiday_20190204", month=2, day=4, year=2019)
Holiday_20190205 = Holiday("Holiday_20190205", month=2, day=5, year=2019)
Holiday_20190206 = Holiday("Holiday_20190206", month=2, day=6, year=2019)
Holiday_20190207 = Holiday("Holiday_20190207", month=2, day=7, year=2019)
Holiday_20190208 = Holiday("Holiday_20190208", month=2, day=8, year=2019)
Holiday_20190405 = Holiday("Holiday_20190405", month=4, day=5, year=2019)

class SHSZCalendar(TradingCalendar):
    @property
    def name(self):
        return "SH"

    @property
    def tz(self):
        return timezone("Asia/Shanghai")

    @property
    def open_time(self):
        return time(9, 30)

    @property
    def close_time(self):
        return time(15)

    @property
    def regular_holidays(self):
        return HolidayCalendar([
            Holiday_20150101,
            Holiday_20150102,
            Holiday_20150218,
            Holiday_20150219,
            Holiday_20150220,
            Holiday_20150223,
            Holiday_20150224,
            Holiday_20150406,
            Holiday_20150501,
            Holiday_20150622,
            Holiday_20150903,
            Holiday_20150904,
            Holiday_20151001,
            Holiday_20151002,
            Holiday_20151005,
            Holiday_20151006,
            Holiday_20151007,
            Holiday_20160101,
            Holiday_20160208,
            Holiday_20160209,
            Holiday_20160210,
            Holiday_20160211,
            Holiday_20160212,
            Holiday_20160404,
            Holiday_20160502,
            Holiday_20160609,
            Holiday_20160610,
            Holiday_20160915,
            Holiday_20160916,
            Holiday_20161003,
            Holiday_20161004,
            Holiday_20161005,
            Holiday_20161006,
            Holiday_20161007,
            Holiday_20170102,
            Holiday_20170127,
            Holiday_20170130,
            Holiday_20170131,
            Holiday_20170201,
            Holiday_20170202,
            Holiday_20170403,
            Holiday_20170404,
            Holiday_20170501,
            Holiday_20170529,
            Holiday_20170530,
            Holiday_20171002,
            Holiday_20171003,
            Holiday_20171004,
            Holiday_20171005,
            Holiday_20171006,
            Holiday_20180101,
            Holiday_20180215,
            Holiday_20180216,
            Holiday_20180219,
            Holiday_20180220,
            Holiday_20180221,
            Holiday_20180405,
            Holiday_20180406,
            Holiday_20180430,
            Holiday_20180501,
            Holiday_20180618,
            Holiday_20180924,
            Holiday_20181001,
            Holiday_20181002,
            Holiday_20181003,
            Holiday_20181004,
            Holiday_20181005,
            Holiday_20181231,
            Holiday_20190101,
            Holiday_20190204,
            Holiday_20190205,
            Holiday_20190206,
            Holiday_20190207,
            Holiday_20190208,
            Holiday_20190405,
        ])

if __name__ == '__main__':
    SHSZCalendar()