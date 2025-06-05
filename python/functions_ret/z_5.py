def day_in_words(date_str):
    day, month, year = date_str.split('.')
    month = int(month)
    
    months = [
        'января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
        'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'
    ]
    
    month_name = months[month - 1]
    return f"{day} {month_name} {year} года"