import math

def roundMinMan(nb):
    return f"Au plafond {math.ceil(nb)} et au plancher {math.floor(nb)}"

print(roundMinMan(3.2))
print(roundMinMan(7.8))
print(roundMinMan(-2.5))