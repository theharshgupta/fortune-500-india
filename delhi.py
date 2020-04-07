import pandas as pd

df = pd.read_csv("mca_delhi.csv", encoding="utf-32", error_bad_lines=False)
print(df)
# df = df[df['REGISTERED_OFFICE_ADDRESS'].str.contains('meridien')]
