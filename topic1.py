import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np
from copy import deepcopy

# Punkt 1
data_frame = pd.read_csv('/Downloads/data sets for ex1/data1.csv')
data_frame_drop_na = data_frame.dropna()
data_frame_drop_na_mean = data_frame_drop_na['var'].mean()
data_frame_drop_na_div_std = data_frame_drop_na['var'].std()
plt.clf()
data_frame_drop_na['var'].hist(edgecolor='black')

plt.xlabel('Wartości')
plt.ylabel('Liczność')
plt.title('Histogram wartości')
plt.savefig('/Downloads//histogram_with_na.png', dpi=300, bbox_inches='tight')

# Punkt 2
data_frame = pd.read_csv('/Users/kingamazur/Downloads/data sets for ex1/data1.csv')
data_fame_filled_mean = data_frame['var'].fillna(value=data_frame_drop_na_mean).to_frame()
data_fame_filed_mean_mean = data_fame_filled_mean['var'].mean()
data_fame_filed_mean_std = data_fame_filled_mean['var'].std()
plt.clf()
data_fame_filled_mean['var'].hist(edgecolor='black')

plt.xlabel('Wartości')
plt.ylabel('Liczność')
plt.title('Histogram wartości')
plt.savefig('/Downloads/histogram_with_mean.png', dpi=300, bbox_inches='tight')

# Punkt 3
data_frame_3 = pd.read_csv('/Downloads/data sets for ex1/data1.csv')
data_frame_copy = deepcopy(data_frame_3)
counter = 0
for i in data_frame_copy['var']:
    if pd.isna(i):
        counter += 1
data_frame_copy= data_frame_copy.dropna()

missing_val = np.random.choice(a=data_frame_copy['var'],size=counter,replace=False)
missing_val = list(missing_val)
j = 0
for i in range(data_frame_3['var'].count()):
    if pd.isna(data_frame_3['var'][i]):
        data_frame_3['var'][i] = missing_val[j]
        j += 1

plt.clf()
data_frame_3['var'].hist(edgecolor='black')
plt.xlabel('Wartości')
plt.ylabel('Liczność')
plt.title('Histogram wartości')
plt.savefig('/Downloads/histogram_with_distribution.png', dpi=300, bbox_inches='tight')

# Results
print(data_frame_3.mean(), data_frame_3.std())
print(data_frame_drop_na_mean, data_fame_filed_mean_mean)
print(data_frame_drop_na_div_std, data_fame_filed_mean_std)

