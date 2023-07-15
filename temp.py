import pandas as pd

before_the_parts = "Jindal Steels - Assistant Manager/Deputy Manager - Finance (1-2 yrs)"
parts = before_the_parts.split("(", 1)
T = parts[0].strip()
E = parts[1].strip(")")
print(E)

df = pd.DataFrame([E, ], columns = ['EXP'])

print(df)