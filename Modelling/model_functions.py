
## GERAL LIBS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from fast_ml.model_development import train_valid_test_split
from sklearn.metrics import classification_report,confusion_matrix
import locale
locale.setlocale(locale.LC_ALL, '')  # Use '' for auto, or force e.g. to 'en_US.UTF-8'

## RANDOM FOREST LIBS
from sklearn.ensemble import RandomForestClassifier

## LOGISTIC REGRESSION LIBS
from sklearn.linear_model import LogisticRegression

## DECISION TREE LIBS
from sklearn.tree import DecisionTreeClassifier


def prep_timestamp_train_val_test(  df,
                                    target,
                                    time_col,
                                    ratio_split,
                                    normal):

    X_train, Y_train, X_valid, Y_valid, X_test, Y_test = train_valid_test_split(df,
                                                                                target = target, 
                                                                                method = 'sorted', 
                                                                                sort_by_col = time_col,
                                                                                train_size = ratio_split[0], 
                                                                                valid_size = ratio_split[1], 
                                                                                test_size = ratio_split[2])

    X_train_last = X_train[time_col].max()
    X_valid_last = X_valid[time_col].max()
    X_test_last = X_test[time_col].max()

    X_train_first = X_train[time_col].min()
    X_valid_first = X_valid[time_col].min()
    X_test_first = X_test[time_col].min()

    array_train = Y_train[target].values
    array_valid = Y_valid[target].values
    array_test = Y_test[target].values

    unique_train, counts_train = np.unique(array_train, return_counts=True)
    unique_valid, counts_valid = np.unique(array_valid, return_counts=True)
    unique_test, counts_test = np.unique(array_test, return_counts=True)

    result_train = np.column_stack((unique_train, counts_train)) 
    result_valid = np.column_stack((unique_valid, counts_valid)) 
    result_test = np.column_stack((unique_test, counts_test)) 

    print(f"Data splitted considering time forecasting.\nShape and {time_col} in:\nTrain: {X_train.shape} {Y_train.shape} ; {X_train_first} to {X_train_last}\n{target} description: {result_train[0]}{result_train[1]}\n\nValid: {X_valid.shape} {Y_valid.shape} ; {X_valid_first} to {X_valid_last}\n{target} description: {result_valid[0]}{result_valid[1]}\n\nTest:  {X_test.shape} {Y_test.shape} ; {X_test_first} to {X_test_last}\n{target} description: {result_test[0]}{result_test[1]}")

    X_train.drop([time_col], axis = 1, inplace = True)
    X_valid.drop([time_col], axis = 1, inplace = True)
    X_test.drop([time_col], axis = 1, inplace = True)

    if normal == 1:
        sd =  pd.DataFrame(columns = X_train.columns)
        mean = pd.DataFrame(columns = X_train.columns)

        for i in X_train.columns:
            sd[f'{i}'] = [X_train[f'{i}'].std()]
            mean[f'{i}'] = [X_train[f'{i}'].mean()]
            X_train[f'{i}'] = ((X_train[f'{i}']- mean[f'{i}'][0])/sd[f'{i}'][0])
            X_valid[f'{i}'] = ((X_valid[f'{i}']- mean[f'{i}'][0])/sd[f'{i}'][0])
            X_test[f'{i}'] = ((X_test[f'{i}']- mean[f'{i}'][0])/sd[f'{i}'][0])

        output =    {"X_train": X_train,
                    "Y_train": Y_train,
                    "X_valid": X_valid,
                    "Y_valid": Y_valid,
                    "X_test": X_test,
                    "Y_test": Y_test,
                    "sd" : sd,
                    "mean": mean}

    else:
        output =    {
                "X_train": X_train,
                "Y_train": Y_train,
                "X_valid": X_valid,
                "Y_valid": Y_valid,
                "X_test": X_test,
                "Y_test": Y_test}

    return(output)

def data_all_only_features(df,columns, removed):

    if removed != 0:
        
        df = df.drop(removed, axis = 1)
        
    else:
        pass
    
    data = df[columns]

    output =    {"all": df,
                "to_model": data}
    
    return(output)

def predicts(model,X):    
    predicts = model.predict(X)
    return(predicts)

def model_metrics(Y,Y_predicts,label):
    cm = confusion_matrix(Y,Y_predicts)

    a = cm[0]/np.sum(cm[0])
    b = cm[1]/np.sum(cm[1])

    cm_perc = np.stack([a,b])

    group_acc = ["{0:.2%}".format(value) for value in
                cm_perc.flatten()]

    group_counts = ["{:n}".format(value) for value in
                    cm.flatten()]

    group_percentages = ["{0:.2%}".format(value) for value in
                        cm.flatten()/np.sum(cm)]

    labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in
            zip(group_counts,group_acc,group_percentages)]

    labels = np.asarray(labels).reshape(2,2)

    ax = sns.heatmap(cm, annot=labels, fmt='', cmap='Blues')

    ax.set_title(f'Seaborn Confusion Matrix with labels\n{label}\n')
    ax.set_xlabel('\nPredicted Values')
    ax.set_ylabel('Actual Values ')

    ## Ticket labels - List must be in alphabetical order
    ax.xaxis.set_ticklabels(['False','True'])
    ax.yaxis.set_ticklabels(['False','True'])

    ## Display the visualization of the Confusion Matrix.
    plt.show()

    print(classification_report(Y,Y_predicts))
   


#############################################################################################   
######################################## RANDOM FOREST ######################################
#############################################################################################

def model_randomf(X_train,Y_train):
    randomf = RandomForestClassifier()
    randomf.fit(X_train,Y_train)
    return(randomf)

#############################################################################################   
######################################## LOGISTIC ###########################################
#############################################################################################


def do_logistic(data,target):
    X_train, X_test,Y_train,Y_test = train_test_split(data.drop(target, axis = 1),data[target],test_size = 0.3)
    logmodel = LogisticRegression( solver='lbfgs', max_iter=10000)
    logmodel.fit(X_train,Y_train )
    predictions = logmodel.predict(X_test)
    print(classification_report(Y_test,predictions))
    return(logmodel)



#############################################################################################   
######################################## DECISION TREE ######################################
#############################################################################################


def do_dtree(data,target):
    X_train, X_test,Y_train,Y_test = train_test_split(data.drop(target, axis = 1),data[target],test_size = 0.3)
    dtree = DecisionTreeClassifier()
    dtree.fit(X_train,Y_train )
    predictions = dtree.predict(X_test)
    print(classification_report(Y_test,predictions))
    print(confusion_matrix(Y_test,predictions))
    return(dtree)

