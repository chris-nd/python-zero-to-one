def note(n):
    if n <= 100 and n >= 90:
        return "A"
    elif n <= 89 and n >= 80:
        return "B"
    elif n <= 79 and n >= 70:
        return "C"
    elif n <= 69 and n >= 60:
        return "D"
    elif n < 60:
        return "F"
    
print(note(95))
print(note(85))
print(note(75))
print(note(65))
print(note(55))