from zipline.utils.calendars import get_calendar,register_calendar
from .shsz_calendar import SHSZCalendar

register_calendar("SHSZ", SHSZCalendar(), force=True)

shsz_calendar = get_calendar("SHSZ")