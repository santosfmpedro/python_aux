import os
import datetime
import model_functions as ml
import pandas as pd

data = pd.read_csv(f"{os.getcwd()}/data.csv", sep=",")

removed = [ 'var_1_removed',
                        'var_2_removed',
                        'var_3_removed', ...]

target = ['target']

time_col = ['time_Col']

features_categ = [  'var_1_categ', 
                    'type_categ',...]
                    
features_continuos = [  'var_1_continuous',
                        'var_2_continuous',
                        'var_3_continuous', ...]

all_columns_to_model =  features_continuos + target + time_col + features_categ

data = ml.data_all_only_features(data,all_columns_to_model,0)

ratio_split = [0.8,0.1,0.1]
model_data = ml.prep_timestamp_train_val_test(  data['to_model'], 
                                                target,
                                                time_col[0],
                                                ratio_split,
                                                0)

randomf_model = ml.model_randomf(   model_data['X_train'], 
                                    model_data['Y_train'])

Y_pred_valid = ml.predicts(randomf_model, model_data['X_valid'])
Y_pred_test = ml.predicts(randomf_model, model_data['X_test'])

pred = pd.DataFrame({'Pred':Y_pred_valid.tolist()})

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from category_encoders import OneHotEncoder
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_validate
from sklearn.model_selection import GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import Normalizer, StandardScaler, MinMaxScaler, PowerTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline, Pipeline

num_pipe = make_pipeline(
    SimpleImputer(strategy='median'),
    StandardScaler()
)

cat_pipe = make_pipeline(
    SimpleImputer(strategy='constant', fill_value='N/A'),
    OneHotEncoder(handle_unknown='ignore')
)

preprocessor = ColumnTransformer(transformers=[
    ('num', num_pipe, features_continuos),
    ('cat', cat_pipe, features_categ)
])


model = Pipeline(steps=[
    ('scaler', preprocessor),
    ('tree', RandomForestClassifier())
])

o_model = model.fit(model_data['X_train'].reset_index(), 
                                    model_data['Y_train'].reset_index()['target'])

str(model.score(model_data['X_valid'], 
                                    model_data['Y_valid']))

pred_pipe = o_model.predict(model_data['X_valid'])


ml.model_metrics(model_data['Y_valid'],pred_pipe,'Validation Data')

data = pd.concat([model_data['X_valid'].reset_index(), pred],axis = 1)
data = pd.concat([data, model_data['Y_valid'].reset_index()],axis = 1)

data.loc[(data['target'] != data['Pred']) ]

ml.model_metrics(model_data['Y_valid'],Y_pred_valid,'Validation Data')