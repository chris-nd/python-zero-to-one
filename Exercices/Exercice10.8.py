import random
# from collections import Counter

def throwDice(value):
    dices = [random.randint(1, 6) for _ in range(value)]
    print(f"Distribution sur {value} lancers :")
    print(dices)
    for side in range(1, 7):
        count = dices.count(side)
        rate = (count*100)/value
        print(f"Face {side}: {count} fois pour {rate}%")
    
throwDice(1000)

# 2ème approche : Une découverte très intérésente
# def throwDice(value):
#     dices = [random.randint(1, 6) for _ in range(value)]
#     print(f"Distribution sur {value} lancers :")
#     print(dices)
#     for side in range(1, 7):
#         distribution = Counter(dices)
#         rate = (distribution[side]*100)/value
#         print(f"Face {side}: {distribution[side]} fois pour {rate}%")
    
# throwDice(1000)
        