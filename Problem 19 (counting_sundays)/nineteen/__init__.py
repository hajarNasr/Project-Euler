from datetime import date
def counting_sundays(first_year, last_year):
    sundays = 0
    for year in range(first_year, last_year+1):
        for month in range(1, 13):
            if date(year, month, day=1).weekday() == 6:
               sundays += 1
        
    return sundays          
            
