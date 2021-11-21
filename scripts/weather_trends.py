import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/dataset.csv")

# Amsterdam Temperature Change
city_name = "Amsterdam"
df_ams = df.loc[df['city'] == city_name]
year = df_ams['year']
global_temp_ma =  df_ams['avg_temp_global'].rolling(7).mean()
ams_temp_ma =  df_ams['avg_temp_city'].rolling(7).mean()
df_ams = df_ams.assign(ma_global = global_temp_ma.values, ma_amsterdam = ams_temp_ma.values)

# Istanbul Temperature Change
city_name = "Istanbul"
df_istanbul = df.loc[df['city'] == city_name]
year = df_istanbul['year']
global_temp_ma = df_istanbul['avg_temp_global'].rolling(7).mean()
istanbul_temp_ma = df_istanbul['avg_temp_city'].rolling(7).mean()
df_istanbul = df_istanbul.assign(ma_global = global_temp_ma.values, ma_istanbul = istanbul_temp_ma.values)

# Paris Temperature Change
city_name = "Paris"
df_paris = df.loc[df['city'] == city_name]
year = df_paris['year']
global_temp_ma =  df_paris['avg_temp_global'].rolling(7).mean()
paris_temp_ma =  df_paris['avg_temp_city'].rolling(7).mean()
df_paris =df_paris.assign(ma_global = global_temp_ma.values, ma_paris = paris_temp_ma.values)

# Berlin Temperature Change
city_name = "Berlin"
df_berlin = df.loc[df['city'] == city_name]
year = df_berlin['year']
global_temp_ma =  df_berlin['avg_temp_global'].rolling(7).mean()
berlin_temp_ma =  df_berlin['avg_temp_city'].rolling(7).mean()
df_berlin = df_berlin.assign(ma_global = global_temp_ma.values, ma_berlin = berlin_temp_ma.values)

plt.plot(year, global_temp_ma, label="Global", color="darkorange")
plt.plot(year, istanbul_temp_ma, label="Istanbul", color="red")
plt.plot(year, berlin_temp_ma, label="Berlin", color="blue")
plt.plot(year, ams_temp_ma, label="Amsterdam", color="purple")
plt.plot(year, paris_temp_ma, label="Paris", color="green")
plt.legend()
plt.title( 'Comparison of Temperature Changes')
plt.xlabel ('Year')
plt.ylabel('Moving Average in °C')
plt.show()