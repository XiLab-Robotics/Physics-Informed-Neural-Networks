from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
import copy
import pandas as pd
#import autosklearn.regression


class MLModel:

    def __init__(self, model, name, columnToPredict):
        self.columnToPredict = columnToPredict
        self.model = model
        self.name = name

    def _train(self, X_train, Y_train):
        self.model.fit(X_train, Y_train)

    def _predict(self, X_test):
        return self.model.predict(X_test)


    def predictorML_leaveOneOut(self, dfInput,files):
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        for i in range(len(dfInput)):
            elem = dfInputOrig.iloc[i]
            dfInput = dfInputOrig.drop(i)
            X = dfInput[dfInput.columns[:2]]
            Y = dfInput[self.columnToPredict]
            X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[:2]]
            X_train = X
            #Y_test = pd.DataFrame(elem).T[self.columnToPredict]
            Y_train = Y

            self._train(X_train,Y_train)
            pred = self._predict(X_test)

            map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
            instanceName = [x for x, y in zip(files, map) if y == True]
            out[i] = {'name':instanceName[0],'prev_'+self.columnToPredict:pred[0]}
        dfOut = pd.DataFrame(out).T
        return dfOut


class MLPipeline:

    def __init__(self, model, name, columnToPredict):
        self.columnToPredict = columnToPredict
        self.model = Pipeline(steps=[('preprocess',StandardScaler()),('model',model)])
        self.name = name

    def _train(self, X_train, Y_train):
        self.model.fit(X_train, Y_train)

    def _predict(self, X_test):
        return self.model.predict(X_test)

    def gridSearch(self,params):
        self.model = GridSearchCV(self.model, params, n_jobs=-1)


    def predictorML_leaveOneOut(self, dfInput,files):
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        for i in range(len(dfInput)):
            elem = dfInputOrig.iloc[i]
            dfInput = dfInputOrig.drop(i)
            X = dfInput[dfInput.columns[:2]]
            Y = dfInput[self.columnToPredict]
            X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[:2]]
            X_train = X
            #Y_test = pd.DataFrame(elem).T[self.columnToPredict]
            Y_train = Y
            print(model)
            self._train(X_train,Y_train)
            pred = self._predict(X_test)

            map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
            instanceName = [x for x, y in zip(files, map) if y == True]
            out[i] = {'name':instanceName[0],'prev_'+self.columnToPredict:pred[0]}
        dfOut = pd.DataFrame(out).T
        return dfOut

    def predictorML_singleModel_leaveOneOut(self, dfInput,files):
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        for i in range(len(dfInput)):
            elem = dfInputOrig.iloc[i]
            dfInput = dfInputOrig.drop(i)
            x_columns = list(dfInput.columns[:2]) + list(dfInput.columns[3:])
            x_columns.remove(self.columnToPredict)
            X = dfInput[x_columns]
            Y = dfInput[self.columnToPredict]
            X_test = pd.DataFrame(elem).T[x_columns]
            X_train = X
            #Y_test = pd.DataFrame(elem).T[self.columnToPredict]
            Y_train = Y

            self._train(X_train,Y_train)
            pred = self._predict(X_test)

            map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
            instanceName = [x for x, y in zip(files, map) if y == True]
            out[i] = {'name':instanceName[0],'prev_'+self.columnToPredict:pred[0]}
        dfOut = pd.DataFrame(out).T
        return dfOut

# class MLAutoMLRegressor:
#     def __init__(self, name, columnToPredict):
#         self.columnToPredict = columnToPredict
#         #self.model = Pipeline(steps=[('preprocess',StandardScaler()),('model',model)])
#         self.name = name
#
#     def predictorAutoML_leaveOneOut(self,dfInput,files):
#         dfInputOrig = copy.deepcopy(dfInput)
#         out = {}
#         for i in range(len(dfInput)-1):
#             elem = dfInput.iloc[i]
#             dfInput = dfInputOrig.drop(i)
#             X = dfInput[dfInput.columns[:2]]
#             Y = dfInput[self.columnToPredict]
#             X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[:2]]
#             X_train = X
#             #Y_test = pd.DataFrame(elem).T[self.columnToPredict]
#             Y_train = Y
#
#             print(self.columnToPredict)
#
#             autoMl = autosklearn.regression.AutoSklearnRegressor(
#                 time_left_for_this_task=120,
#                 per_run_time_limit=30,
#                 ensemble_size=1)
#             autoMl.fit(X_train,Y_train,dataset_name='ML-transmission-error')
#             print(autoMl.leaderboard())
#             #print(autoMl.show_models())
#             pred = autoMl.predict(X_test)
#             #self._train(X_train,Y_train)
#             #pred = self._predict(X_test)
#
#             map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
#             instanceName = [x for x, y in zip(files, map) if y == True]
#             out[i] = {'name':instanceName[0],'prev_'+self.columnToPredict:pred[0]}
#         dfOut = pd.DataFrame(out).T
#         return dfOut