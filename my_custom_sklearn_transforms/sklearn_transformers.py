from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC
import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.utils import resample


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
    
    

class normalizarX(BaseEstimator, TransformerMixin):
    def __init__(self):
        1

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        col = [
        "HOURS_DATASCIENCE", "HOURS_BACKEND", "HOURS_FRONTEND",
        "NUM_COURSES_BEGINNER_DATASCIENCE", "NUM_COURSES_BEGINNER_BACKEND", "NUM_COURSES_BEGINNER_FRONTEND",
        "NUM_COURSES_ADVANCED_DATASCIENCE", "NUM_COURSES_ADVANCED_BACKEND", "NUM_COURSES_ADVANCED_FRONTEND",
        "AVG_SCORE_DATASCIENCE", "AVG_SCORE_BACKEND", "AVG_SCORE_FRONTEND","PROFILE"
                   ]
        # Primero copiamos el dataframe de datos de entrada 'X'
        data= X.copy()
        #xx=np.array(data)[:, :-1]
        #yy=np.array(data)[:, -1]
        scalar= MinMaxScaler()
        scalar.fit(data)
        X= scalar.transform(data)
    
    
#         scalar= MinMaxScaler()
#         scalar.fit(xx)
#         X= scalar.transform(xx)
#         arr=np.column_stack((X,yy))
#         datasetN = pd.DataFrame(data=arr,columns=col)
       
        return X
    
    
    
    
class Smo(BaseEstimator, TransformerMixin):
    def __init__(self):
        1

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        sm = SMOTE(random_state=42, sampling_strategy='minority')
        smote_x_train = sm.fit_resample(X)
       
        return smote_x_train
