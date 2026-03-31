import pandas as pd
from sklearn.datasets import load_wine

wine_data = load_wine()
df_wine = pd.DataFrame(data=wine_data.data, columns=wine_data.feature_names)

df_wine['target_class'] = wine_data.target

df_wine.to_excel('wine_dataset.xlsx', index=False)
print("File wine_dataset.xlsx berhasil dibuat!")