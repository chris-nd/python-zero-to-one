```python
import math

a = [1, 4, 18, 29, 13]

b = []

for i in a:
    b.append(math.log(i))

b = [math.log(i) for i in a]

a.append(-1)

b = [math.log(i) for i in a if i > 0]

prenom = ['Alice', 'evE', 'sonia', 'BOB']

prenom = [p.lower() for p in prenom] 