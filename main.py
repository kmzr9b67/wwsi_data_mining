import pandas as pd
import matplotlib.pyplot as plt

# ćwiczenia 1 dla zestawu 1
data_fame = pd.read_csv('/Users/kingamazur/Downloads/data sets for ex1/data1.csv')

# Punkty 1 - usuwamy braujące dane 
data_frame_drop_na = data_fame.dropna()

data_frame_drop_na_mean = data_frame_drop_na['var'].mean()
data_frame_drop_na_div_std = data_frame_drop_na['var'].std()

data_frame_drop_na['var'].hist(bins=10, edgecolor='black')
plt.xlabel('Wartości')
plt.ylabel('Liczność')
plt.title('Histogram wartości')
plt.savefig('/Users/kingamazur/Downloads//histogram_with_na.png', dpi=300, bbox_inches='tight')

# Punkt 2
data_fame = pd.read_csv('/Users/kingamazur/Downloads/data sets for ex1/data1.csv')
data_fame_filled_mean = data_fame['var'].fillna(value=data_frame_drop_na_mean).to_frame()
data_fame_filed_mean_mean = data_fame_filled_mean['var'].mean()
data_fame_filed_mean_std = data_fame_filled_mean['var'].std()

data_fame_filled_mean['var'].hist()
plt.xlabel('Wartości')
plt.ylabel('Liczność')
plt.title('Histogram wartości')
plt.savefig('/Users/kingamazur/Downloads/histogram_with_mean.png', dpi=300, bbox_inches='tight')

# Punkt 3
data_fame = pd.read_csv('/Users/kingamazur/Downloads/data sets for ex1/data1.csv')

print(data_frame_drop_na_mean, data_fame_filed_mean_mean)
print(data_frame_drop_na_div_std, data_fame_filed_mean_std)