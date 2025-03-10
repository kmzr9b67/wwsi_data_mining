from os import getenv
from dotenv import load_dotenv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

load_dotenv()
URL = f'{getenv("FILE_URL")}/cars 1.csv'
df = pd.read_csv(URL)
columns_names = df.columns

# Rysune histogram dla wszystkich zmiennych 
counter = 0 
for i in columns_names:
    plt.clf()
    df[i].hist(edgecolor = 'Black', bins=20)
    plt.xlabel('Wartość')
    plt.ylabel('Liczebność')
    plt.title(f'Histogram wartości dla zmiennej {i}.')
    plt.savefig(f'{getenv("FILE_URL")}/rysunek{1+counter}.png',  dpi=300, bbox_inches='tight')
    counter += 1

    if i == 'acceleration':
        print(i)
        print(df[df[i] <  5])
        print(df[df[i] > 23])
    
    else: 
        print(i)
        print(df[df[i] > 600])

# Rysuje scatter plot 
plt.clf()
plt.scatter(df['engine.displacement'],df['acceleration'])
plt.title("Wykres Scatter acceleration w funkcji engine.displacement")
plt.xlabel("Oś engine.displacement")
plt.ylabel("Oś acceleration")
plt.savefig(f'{getenv("FILE_URL")}/sccater_1.png',  dpi=300, bbox_inches='tight')

#Z-score standardization  
for i in columns_names:
    df[f'{i}.standard'] = pd.DataFrame((df[i]-df[i].mean())/df[i].std())

for i in columns_names:
    print(df[df[f'{i}.standard'] > 3])
    print(df[df[f'{i}.standard'] < -3])

# Rozstępy międzykwartylowe.
engine_displacement = np.array(df['engine.displacement'])
acceleration = np.array(df['acceleration'])

q3_engine_displacement = np.quantile(engine_displacement, 0.75)
q1_engine_displacement = np.quantile(engine_displacement, 0.25)
iqr_engine_displacement = q3_engine_displacement- q1_engine_displacement

q3_acceleration = np.quantile(acceleration, 0.75)
q1_acceleration = np.quantile(acceleration, 0.25)
iqr_acceleration = q3_acceleration- q1_acceleration
print('Metoda IQR\n')
print(df[df['engine.displacement'] < q1_engine_displacement - iqr_engine_displacement*1.5])
print(df[df['engine.displacement'] > q3_engine_displacement + iqr_engine_displacement*1.5])
print('Acc')
print(iqr_acceleration)
print(q1_acceleration)
print(q3_acceleration)
print(df[df['acceleration'] < q1_acceleration - iqr_acceleration*1.5])
print(df[df['acceleration'] > q3_acceleration + iqr_acceleration*1.5])