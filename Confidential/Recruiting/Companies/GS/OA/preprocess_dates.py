import re

def format_date(x):
    expr = r'(\d+)\w+ (\w+) (\d+)'
    match = re.match(expr, x)
    
    months = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]
    
    day = match.group(1).zfill(2)
    month = str(months.index(match.group(2)) + 1).zfill(2)
    year = match.group(3)
    
    return '-'.join([year, month, day])

def preprocessDate(dates):
    formatted_dates = []

    for date in dates:
        formatted = format_date(date)
        formatted_dates.append(formatted)
        
    return formatted_dates