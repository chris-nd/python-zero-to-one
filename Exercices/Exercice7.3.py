def bisextil_year(year):
    if (year % 4 == 0  and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
print(bisextil_year(2020))
print(bisextil_year(2021))
print(bisextil_year(2000))
print(bisextil_year(1900))