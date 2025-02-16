import pandas as pd
import matplotlib.pyplot as plt

# ćwiczenia 1
data_fame = pd.read_csv('/Users/kingamazur/Downloads/data sets for ex1/data1.csv')
print(data_fame.head)
# Przesłuchać nagarnie i zrobić analogiczniedo tego co ona chce. 
print(data_fame['var'])
# Punkty 1 - usuwamy braujące dane 
data_frame_drop_na = data_fame.dropna()
print(data_frame_drop_na.head)
# Liczymy średnią i odchylenie standardowe 
data_frame_drop_na_mean = data_frame_drop_na.mean()
data_frame_drop_na_div_std = data_frame_drop_na.std()
print(f'Średnia: {data_frame_drop_na_mean}')
print(f'Odchylenie stdd {data_frame_drop_na_div_std}')

data_frame_drop_na['var'].hist(bins=10, edgecolor='black')
plt.xlabel('Wartości')
plt.ylabel('Liczność')
plt.title('Histogram wartości')
plt.savefig('/Users/kingamazur/Downloads//histogram_1.png', dpi=300, bbox_inches='tight')
plt.show()
