from datetime import date

def find_age(birthday):
    current_date = date.today()
    birth_date = date.fromisoformat(birthday)
    years = current_date.year - birth_date.year
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        years -= 1
    months = current_date.month - birth_date.month
    if current_date.day < birth_date.day:
        months -= 1
    if months < 0:
        months += 12
    days = current_date.day - birth_date.day
    if days < 0:
        from calendar import monthrange
        prev_month = current_date.month - 1 if current_date.month > 1 else 12
        prev_year = current_date.year if current_date.month > 1 else current_date.year - 1
        days_in_prev_month = monthrange(prev_year, prev_month)[1]
        days += days_in_prev_month
    
    return f"Votre âge est de: {years} ans, {months} mois et {days} jours"

print(find_age("2000-05-15"))

# 2 ème approche
# from datetime import date
# from dateutil.relativedelta import relativedelta

# def find_age(birthday):
#     current_date = date.today()
#     birth_date = date.fromisoformat(birthday)
    
#     # Calculer la différence
#     diff = relativedelta(current_date, birth_date)
    
#     return f"Votre âge est de: {diff.years} ans, {diff.months} mois et {diff.days} jours"

# print(find_age("2000-05-15"))