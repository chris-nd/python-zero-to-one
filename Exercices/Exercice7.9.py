def check_password(pwd: str):
    if len(pwd) < 8:
        return "Trop court (minimum 8 caractères)"
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_symbol = any(not c.isalnum() for c in pwd)
    if all([has_upper, has_lower, has_digit, has_symbol]):
        return "Mot de passe validé"
    manquants = []
    if not has_upper:
        manquants.append("majuscule")
    if not has_lower:
        manquants.append("minuscule")
    if not has_digit:
        manquants.append("chiffre")
    if not has_symbol:
        manquants.append("symbole")
    return f"Invalide - Manque : {', '.join(manquants)}"


print(check_password("Pass123"))
print(check_password("password"))
print(check_password("P@ssw0rd"))
print(check_password("Ab1!"))
