import datetime
from calendar import monthrange, month_name

date_today = datetime.date.today()

current_year = date_today.year
current_month = date_today.month
current_day = date_today.day

# current menu date
days_in_month_icon_dict = {
    28: 'Icons/Month_days_icons/twenty-eight.png',
    29: 'Icons/Month_days_icons/twenty-nine.png',
    30: 'Icons/Month_days_icons/thirty.png',
    31: 'Icons/Month_days_icons/thirty-one.png'
}

current_menu_date = date_today

current_menu_year = current_year
current_menu_month = current_month

days_in_current_menu_month = monthrange(current_menu_year, current_menu_month)[1]
current_menu_month_name = month_name[current_menu_month]

history_dict = None
Transaction_menu_in_last_date = None
