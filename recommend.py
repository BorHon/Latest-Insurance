# # encoding:utf-8
# import pandas as pd
# import joblib
# import sqlite3
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import *
# conn = sqlite3.connect('data.db')
# cursor = conn.cursor()
# cursor.execute('select * from train__information')
# values = cursor.fetchall()
# cursor.close()
# conn.commit()
# conn.close()
# df=pd.DataFrame(values,columns=["ID","Age","Income","Height","Weight","Sex","Marriage","Deposit","Specific","Family_insured","Insurance"])
# pf_sex=pd.get_dummies(df[['Sex']])
# pf_marriage=pd.get_dummies(df[['Marriage']])
# df = pd.concat([df, pf_sex,pf_marriage], axis=1)
# y=df["Insurance"]
# df.drop(['Insurance'], axis=1, inplace=True)
# df.drop(['Sex'], axis=1, inplace=True)
# df.drop(["Marriage"], axis=1, inplace=True)
# df.drop(["ID"], axis=1, inplace=True)
# X_train, X_test, y_train, y_test = train_test_split(df,y, test_size=0.3,random_state=0)
# model = LogisticRegression(random_state=0, solver='sag',multi_class='ovr', verbose = 1)
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# joblib.dump(model,'recommend.model')
# print("The model  ok")
# import joblib
# RF=joblib.load('recommend.model')
# print(RF.predict([[5.90000e+01, 1.25520e+04, 1.47000e+02, 4.00000e+01,
#             1.12968e+05, 0.00000e+00, 0.00000e+00, 0.00000e+00, 0.00000e+00,
#        1.00000e+00, 0.00000e+00, 1.00000e+00, 0.00000e+00]]))


import joblib
import numpy as np
class recommned_model:
    def get_recommendation(age,Income,Weight,Height,Deposit,Specific,Insured,Sex,Marrige):
        model= joblib.load(r'F:\PycharmProject\Insurance-Recommend\sayhello\recommend.model')
        sex_dict={"Female":[1,0,0],"Male":[0,1,0],"UnKnown":[0, 0,1]}
        Marriage_dict = {"divorced": [1, 0, 0], "married": [0, 1, 0], "unmarried": [0, 0, 1]}
        variable=[age,Income,Height,Weight,Deposit,Specific,Insured]
        variable+=(sex_dict[Sex])
        variable+=(Marriage_dict[Marrige])
        print(variable)
        return(model.predict([variable]))
