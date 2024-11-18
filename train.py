import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

# parameters

C = 1
n_splits = 5
output_file = f'model_C={C}.bin'

# data preparation

data = "https://raw.githubusercontent.com/bankymondial/Predicting-Gym-Class-Attendance/refs/heads/main/fitness_class_2212.csv"
df = pd.read_csv(data)

df.weight = df.weight.fillna(df.weight.median())
df.drop('booking_id', axis=1, inplace=True)
df.days_before = df.days_before.str.replace(r' days$', '', regex=True)
df.days_before = pd.to_numeric(df.days_before, errors='coerce').astype(int)
df.day_of_week = df.day_of_week.replace({'Wednesday': 'Wed', 'Monday': 'Mon'})
df.day_of_week = df.day_of_week.str.replace(r'Fri\.$', 'Fri', regex=True)
df.category = df.category.replace('-', 'Unknown')

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)

numerical = ['months_as_member', 'weight', 'days_before']
categorical = ['day_of_week', 'time', 'category']

# training

def train(df_train, y_train, C=1.0):
    dicts = df_train[categorical + numerical].to_dict(orient='records')
    
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)
    
    model = LogisticRegression(C=C, solver='liblinear', random_state=1, max_iter=1000)
    model.fit(X_train, y_train)

    return dv, model

def predict(df, dv, model):
    dicts = df[categorical + numerical].to_dict(orient='records')

    X = dv.transform(dicts)
    y_pred = model.predict_proba(X)[:, 1]

    return y_pred

# k-fold Cross-validation

print(f'doing validation with C={C}')

kfold = KFold(n_splits=n_splits, shuffle=True, random_state=1)
    
scores = []

fold = 0

for train_idx, val_idx in kfold.split(df_full_train):
    df_train = df_full_train.iloc[train_idx]
    df_val = df_full_train.iloc[val_idx]
    
    y_train = df_train.attended.values
    y_val = df_val.attended.values    
        
    dv, model = train(df_train, y_train, C=C)
    y_pred = predict(df_val, dv, model)
    
    auc = roc_auc_score(y_val, y_pred)
    scores.append(auc)
    
    print(f'auc on fold {fold} is {auc}')
    fold = fold + 1

print('validation results:')
print('C=%s %.3f +- %.3f' % (C, np.mean(scores), np.std(scores)))


# training the final model

print('training the final model')

dv, model = train(df_full_train, df_full_train.attended.values, C=1.0)
y_pred = predict(df_test, dv, model)

y_test = df_test.attended.values
auc = roc_auc_score(y_test, y_pred)
auc

print(f'auc={auc}')

# Save the model

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)
   
print(f'the model is saved to {output_file}')