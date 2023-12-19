import calendar

def showCalendar(yyyy, mm, special):
    cal = calendar.monthcalendar(yyyy, mm)

    # Wyświetlanie nagłówka kalendarza
    result = f"{calendar.month_name[mm]} {yyyy}<br>Mo Tu We Th Fr Sa Su<br>"

    # Wyświetlanie kalendarza z uwzględnieniem kwadratowych nawiasów
    for week in cal:
        for day in week:
            if day == 0:
                result += "<br>" + " "
            elif day in special:
                result += f"[{day}]" + " "
            else:
                result += f"{day:2}" + " "
        result += "<br>"
    return result

# # Miesiąc i rok do wyświetlenia
# year = 2023
# month = 5

# # Lista dni do wyświetlenia w kwadratowych nawiasach
# highlighted_days = [3, 26]

# print(showCalendar(year, month, highlighted_days))





# Tworzenie kalendarza

