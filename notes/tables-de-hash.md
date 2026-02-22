```python
%timeit 'x' in range(100)
%timeit 'x' in range(10_000)
%timeit 'x' in range(1_000_000)
t = [1, 2]
t[0]
t = [18, 35]
t['alice'] = 35