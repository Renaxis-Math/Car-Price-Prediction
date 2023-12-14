import pandas as pd

def f(a):
    a.at[0] = -1
    return

a = pd.Series(data = [1, 2, 3, 4, 5])
print(a)
f(a)
print(a)