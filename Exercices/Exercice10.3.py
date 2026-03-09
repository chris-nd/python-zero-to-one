from datetime import datetime

def printDateTime():
    d = datetime.today()
    return d.ctime()

print(printDateTime())

# 2 ème approche
# def printDateTime():
#     d = datetime.now()
#     return d.strftime("%H:%M:%S %A %d %B %Y")

# print(printDateTime())