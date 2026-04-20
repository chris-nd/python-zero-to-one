from datetime import datetime, timedelta
import time

# on obtient l'heure courante sous la forme d'un flottant
# qui représente le nombre de secondes depuis le 1er Janvier 1970
t_now = time.time()
print(t_now)

t_later = t_now + 3 * 3600
print(t_later)
print(type(t_later))

struct_later = time.gmtime(t_later)
print(struct_later)

print(f"heure UTC dans trois heures "
      f"{time.strftime('%Y-%m-%d %H:%M', struct_later)}")

dt_now = datetime.now()
dt_later = dt_now + timedelta(hours=3)
print("maintenant", dt_now)
print(f"dans trois heures {dt_later.strftime('%Y-%m-%d at %H:%M')}")

# on peut passer le format directement
print(f"dans trois heures {dt_later:%Y-%m-%d at %H:%M}")
