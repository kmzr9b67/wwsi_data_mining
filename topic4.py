from os import getenv
from dotenv import load_dotenv

import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

load_dotenv()
URL = f'{getenv("FILE_URL")}/seeds.csv'
df = pd.read_csv(URL)
df = df.sample(frac=1)

df_test = df.iloc[0:30]
test_set = df_test.iloc[:,0:7]
test_class =df_test.iloc[:,7:]

df_training = df.iloc[30:]
training_set = df_training.iloc[:,0:7]
training_class =df_training.iloc[:,7:]

K = 4

knn = KNeighborsClassifier(n_neighbors=K)
knn.fit(training_set, training_class)
result_knn = knn.predict(test_set)
list_test_class = []

for i in np.array(test_class):
    list_test_class.append(i[0])

confusion_matrix_test = confusion_matrix(test_class,result_knn)
error_rate = np.mean(np.array(result_knn) != np.array(list_test_class))
print("Result matrix:")
print(confusion_matrix_test)
print("Error:")
print(error_rate)

print(df.head())
NFOLDS = 10
folds = pd.cut(np.arange(1, len(df) + 1), bins=NFOLDS, labels=False)
df['fold'] = folds
print(df.head())
K = [1,4]

for k in K:
    average_error_rate = 0
    print("K")
    print(k)
    for i in range(10):
        df_test = df[df["fold"] == i]
        test_set = df_test.iloc[:,0:7]
        test_class = df_test.iloc[:,7:8]

        df_training = df[df["fold"] != i]
        training_set = df_training.iloc[:,0:7]
        training_class = df_training.iloc[:,7:8]

        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(training_set, training_class)
        result_knn = knn.predict(test_set)

        list_test_class = []
        for i in np.array(test_class):
            list_test_class.append(i[0])
        # print(test_class)
        # print(result_knn)
        confusion_matrix_test = confusion_matrix(test_class,result_knn)
        error_rate = np.mean(np.array(result_knn) != np.array(list_test_class))
        # print(confusion_matrix_test)
        # print(error_rate)
        average_error_rate += error_rate
    
    print('average_error_rate')
    print(average_error_rate/NFOLDS)
