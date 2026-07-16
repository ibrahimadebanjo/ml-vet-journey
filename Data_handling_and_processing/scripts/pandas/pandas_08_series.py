import pandas as pd
s = pd.Series([1,5,89,20,60,200])
print(s)
print(s.name)
print(s.dtype)
s.name = "numbers"
print(s.index)
print(s[: 3])
print(s.iloc[3])
print(s.iloc[[1,4,2,5]])