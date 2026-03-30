import pandas as pd

# Load the CSV
df = pd.read_csv(r"C:\Repositories\db_alenusa_mysql\seeds\fct_spectra_retailers.csv")

third = len(df) // 3
df.iloc[:third].to_csv(r'C:\Repositories\db_alenusa_mysql\seeds\fct_spectra_retailers_1.csv', index=False)
df.iloc[third:third*2].to_csv(r'C:\Repositories\db_alenusa_mysql\seeds\fct_spectra_retailers_2.csv', index=False)
df.iloc[third*2:].to_csv(r'C:\Repositories\db_alenusa_mysql\seeds\fct_spectra_retailers_3.csv', index=False)
print('Done:', len(df), 'rows split into three files')