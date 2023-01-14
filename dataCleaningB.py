import pandas as pd

df = pd.read_csv("data_merged.csv")
print(df.columns)

df.drop(['Unnamed: 0','Luminosity','Unnamed: 6','Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1'],axis = 1,inplace=True)

print(df)

final_data = df.dropna()
final_data.to_csv('main.csv')
final_data.info()