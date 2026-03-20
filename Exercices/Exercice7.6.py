def price_ticket(age):
    if age < 12:
        return 5
    elif 12 <= age <= 60:
        return 10
    else:
        return 7

print(price_ticket(5))
print(price_ticket(12))
print(price_ticket(18))
print(price_ticket(65))
print(price_ticket(70))