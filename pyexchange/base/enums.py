# coding: utf-8


class CalendarItemType(object):
    SINGLE = u'Single'
    OCCURRENCE = u'Occurrence'
    EXCEPTION = u'Exception'
    RECURRING_MASTER = u'RecurringMaster'

    occurrences = (OCCURRENCE, EXCEPTION)

