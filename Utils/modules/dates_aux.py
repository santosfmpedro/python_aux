
from datetime import datetime
from dateutil import relativedelta

today = datetime.now().date() ## only date

now = datetime.now() ## date and hour and minute and seconds

yesterday = today - relativedelta.relativedelta(days=1)

this_year = today.replace(month = 1, day = 1)

def x_dates_dif(date,type,value,start):
    output = []
    if start == 1:
        if type ==  'months':
            output = (date + relativedelta.relativedelta(months = value)).replace( day = 1)
        else:
            if type == 'years':
                output = (date + relativedelta.relativedelta(years = value)).replace(day = 1)
            else:
                if type ==  'days':
                    output = (date + relativedelta.relativedelta(days = value)).replace( day = 1)
                else:
                    print(f'Type date {type} not find!')
    else:
        if type ==  'months':
            output = date + relativedelta.relativedelta(months = value)
        else:
            if type ==  'years':
                output = date + relativedelta.relativedelta(years = value)
            else:
                if type ==  'days':
                    output = date + relativedelta.relativedelta(days = value)
                else:
                    print(f'Type date {type} not find!')
    return output