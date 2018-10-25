# coding: utf-8


class CalendarItemType(object):
    SINGLE = u'Single'
    OCCURRENCE = u'Occurrence'
    EXCEPTION = u'Exception'
    RECURRING_MASTER = u'RecurringMaster'

    occurrences = (OCCURRENCE, EXCEPTION)


class RecurrencePattern(object):
    ABSOLUTE_YEARLY = u'AbsoluteYearly'
    RELATIVE_YEARLY = u'RelativeYearly'
    ABSOLUTE_MONTHLY = u'AbsoluteMonthly'
    RELATIVE_MONTHLY = u'RelativeMonthly'
    WEEKLY = u'Weekly'
    DAILY = u'Daily'

    tags = {
        ABSOLUTE_YEARLY: u't:AbsoluteYearlyRecurrence',
        RELATIVE_YEARLY: u't:RelativeYearlyRecurrence',
        ABSOLUTE_MONTHLY: u't:AbsoluteMonthlyRecurrence',
        RELATIVE_MONTHLY: u't:RelativeMonthlyRecurrence',
        WEEKLY: u't:WeeklyRecurrence',
        DAILY: u't:DailyRecurrence',
    }


class RecurrenceBoundary(object):
    NO_END = u'NoEnd'  # only start date
    END_DATE = u'EndDate'  # start and end date
    NUMBERED = u'Numbered'  # start date and number of occurrences

    tags = {
        NO_END: u't:NoEndRecurrence',
        END_DATE: u't:EndDateRecurrence',
        NUMBERED: u't:NumberedRecurrence',
    }
