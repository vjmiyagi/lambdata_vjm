import pandas as pd
from my_mod import enlarge


print("Hello")

print(enlarge(8))

df = pd.DataFrame({"state": ["CT", "CO", "CA", "TX"]})
print(df.head())
