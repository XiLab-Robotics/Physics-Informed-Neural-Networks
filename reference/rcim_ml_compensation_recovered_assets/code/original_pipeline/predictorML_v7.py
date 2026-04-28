from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_validate
import copy
import pandas as pd
import os
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
from sklearn.multioutput import MultiOutputRegressor
from sklearn.multioutput import RegressorChain
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
from scipy.spatial import distance_matrix
import random
import numpy as np
import datetime
import datetime
import math
from onnxmltools import convert_xgboost, convert_lightgbm
from onnxmltools.convert.common.data_types import FloatTensorType as OXFloatTensorType
from xgboost.sklearn import  XGBRegressor
from lightgbm import LGBMRegressor


class MLModel:

    def __init__(self, model, name, method=''):
        self.model = model
        self.method = method
        self.name = type(model).__name__ + '_' + name

    def _train(self, X_train, Y_train):
        self.model.fit(X_train, Y_train)

    def _predict(self, X_test):
        return self.model.predict(X_test)

    def exportModel(self,modelName):
        initial_type = [('float_input', FloatTensorType([None, self.model.n_features_in_]))]
        onx = convert_sklearn(self.model, initial_types=initial_type)
        with open(modelName+".onnx", "wb") as f:
            f.write(onx.SerializeToString())

    def gridSearch(self,params):
        self.model = GridSearchCV(self.model, params, n_jobs=-1)

    # OLD DA AGGIORNARE
    # def predictorML_leaveOneOut(self, dfInput,files):
    #     dfInputOrig = copy.deepcopy(dfInput)
    #     out = {}
    #     for i in range(len(dfInput)):
    #         elem = dfInputOrig.iloc[i]
    #         dfInput = dfInputOrig.drop(i)
    #         X = dfInput[dfInput.columns[:2]]
    #         Y = dfInput[self.columnToPredict]
    #         X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[:2]]
    #         X_train = X
    #         #Y_test = pd.DataFrame(elem).T[self.columnToPredict]
    #         Y_train = Y
    #
    #         self._train(X_train,Y_train)
    #         pred = self._predict(X_test)
    #
    #         map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
    #         instanceName = [x for x, y in zip(files, map) if y == True]
    #         out[i] = {'name':instanceName[0],'prev_'+self.columnToPredict:pred[0]}
    #     dfOut = pd.DataFrame(out).T
    #     return dfOut

    def getAcronimMethod(self, fileName):

        acronims = {
            'DecisionTreeRegressor': 'DT',
            'ExtraTreeRegressor': 'ET',
            'ExtraTreesRegressor': 'ERT',
            'RandomForestRegressor': 'RF',
            'GradientBoostingRegressor': 'GBM',
            'HistGradientBoostingRegressor': 'HGBM',
            'XGBRegressor': 'XGBM',
            'LGBMRegressor': 'LGBM',
            'SVR': 'SVM',
            'MLPRegressor': 'MLP',
            'MinimumDistance': 'MinDist'
        }

        method = ''

        for elem in acronims.keys():
            if elem in fileName:
                method = acronims[elem]

        return method
    def predictorMLCrossValidation(self, dfInput,testSetDimension):
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]
        if self.method == 'phase':
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]
        elif self.method == 'ampl':
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]
        else:
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]  # dfInput.columns[3:]
            Y = dfInput[cols]

        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=testSetDimension,random_state=0)
        # # X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[['rpm','tor']]]
        # X_train = X
        # # Y_test = pd.DataFrame(elem).T[self.columnToPredict]
        # Y_train = Y


        self._train(X_train, Y_train)

        errorsAcronims = {
            'test_neg_mean_squared_error' : 'MSE',
            'test_neg_root_mean_squared_error': 'RMSE',
            'test_neg_mean_absolute_error':'MAE',
            'test_neg_mean_absolute_percentage_error':'MAPE'
        }

        scores = cross_validate(self.model, X, Y, cv=10,scoring=['neg_mean_squared_error',
                                                                  'neg_root_mean_squared_error',
                                                                  'neg_mean_absolute_error',
                                                                  'neg_mean_absolute_percentage_error'],)

        errorKeys = list(errorsAcronims.keys())#[x for x in list(scores.keys()) if 'test' in x]
        crossValOut = {}

        crossValOut['0_method'] = self.getAcronimMethod(self.name)

        for el in errorKeys:
            crossValOut[errorsAcronims[el]] = abs(scores[el].mean())


        # for i in range(len(self.model.estimators_)):
        #     scores = cross_validate(self.model.estimators_[i], X, Y[Y.columns[i:i + 1]], cv=10,
        #                             scoring=['neg_mean_squared_error',
        #                                      'neg_root_mean_squared_error',
        #                                      'neg_mean_absolute_error',
        #                                      'neg_mean_absolute_percentage_error'])
        #
        #     errorKeys = list(errorsAcronims.keys())
        #     for el in errorKeys:
        #         component = list(Y.columns[i:i + 1])[-1].split('_')[-2:]
        #         crossValOut[str(component[0])+'_'+str(component[1])+'_'+errorsAcronims[el]] = abs(scores[el].mean())

        pred = self._predict(X_test)

        ## save scores for each model and for the aggregated
        outputFileSummary = 'output_prediction/summaryCrossValidation+_'+self.name.split('_')[-2:][0]\
                            +'_'+self.name.split('_')[-2:][1]+'.csv'
        finalOut = pd.DataFrame(crossValOut,index=[0])
        if os.path.isfile(outputFileSummary):
            # Se il file esiste già, carica il contenuto esistente in un DataFrame
            existing_df = pd.read_csv(outputFileSummary, sep=';', decimal=',')

            # Aggiungi il nuovo contenuto al DataFrame esistente
            finalOut = pd.concat([existing_df,finalOut])
            #finalOut = existing_df.append(pd.DataFrame(crossValOut,index=[0]), ignore_index=True)

            # Salva il DataFrame aggiornato nel file
        finalOut.to_csv(outputFileSummary, sep=';', decimal=',', index=False)

        for i in range(len(X_test)):
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            # map = [x.startswith(str(elem['rpm']) + 'rpm' + str(elem['tor']) + 'Torque') for x in files]
            # #map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
            # instanceName = [x for x, y in zip(files, map) if y == True]
            out[i] = namesParam
            for j in range(len(cols)):
                out[i]['prev_' + cols[j]] = pred[i][j]

        dfOut = pd.DataFrame(out).T
        return dfOut

class MLModelChainedMultipleOutput:

    def __init__(self, model, name, method=''):
        self.model = RegressorChain(model)
        self.method = method
        self.name = type(model).__name__ + '_' + name

    def _train(self, X_train, Y_train):
        self.model.fit(X_train, Y_train)

    def _predict(self, X_test):
        return self.model.predict(X_test)


    #Export del singolo modello da multiOutput
    def exportModel(self,modelName):
        initial_type = [('float_input', FloatTensorType([None, self.model.n_features_in_]))]
        for i in range(len(self.model.estimators_)):
            est = self.model.estimators_[i]
            onx = convert_sklearn(est, initial_types=initial_type)
            with open(modelName+'_'+str(i)+".onnx", "wb") as f:
                f.write(onx.SerializeToString())

    def predictorML_leaveOneOut(self, dfInput,files):
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        for i in range(len(dfInput)):
            elem = dfInputOrig.iloc[i]
            dfInput = dfInputOrig.drop(i)
            X = dfInput[dfInput.columns[:2]]
            if self.method == 'phase':
                cols = [x for x in dfInput.columns if 'phase' in x]
                Y = dfInput[cols]
            elif self.method == 'ampl':
                cols = [x for x in dfInput.columns if 'ampl' in x]
                Y = dfInput[cols]
            else:
                cols = dfInput.columns[3:]
                Y = dfInput[cols]

            X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[:2]]
            X_train = X
            #Y_test = pd.DataFrame(elem).T[self.columnToPredict]
            Y_train = Y

            self._train(X_train,Y_train)
            pred = self._predict(X_test)

            map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
            instanceName = [x for x, y in zip(files, map) if y == True]
            out[i] = {'name':instanceName[0]}
            for j in range(len(cols)):
                out[i]['prev_'+cols[j]] = pred[0][j]
        dfOut = pd.DataFrame(out).T
        return dfOut
class MLModelMultipleOutput:

    def __init__(self, model, name, method=''):
        self.model = MultiOutputRegressor(model)
        self.method = method
        self.name = type(model).__name__ + '_' + name

    def _train(self, X_train, Y_train):
        self.model.fit(X_train, Y_train)

    def _predict(self, X_test):
        return self.model.predict(X_test)

    #Export del singolo modello da multiOutput
    # def exportModel(self,modelName,colsToPredict):
    #     initial_type = [('float_input', FloatTensorType([None, self.model.n_features_in_]))]
    #     for i in range(len(self.model.estimators_)):
    #         est = self.model.estimators_[i]
    #         onx = convert_sklearn(est, initial_types=initial_type)
    #         with open("model_output_dir/"+modelName+'_'+colsToPredict[i]+".onnx", "wb") as f:
    #             f.write(onx.SerializeToString())
    def exportModel(self, modelName, colsToPredict):
        for i in range(len(self.model.estimators_)):
            est = self.model.estimators_[i]

            if isinstance(est, XGBRegressor):
                booster = est.get_booster()
                booster.feature_names = [f"f{i}" for i in range(est.n_features_in_)]

                initial_type = [('float_input', OXFloatTensorType([None, est.n_features_in_]))]
                onx = convert_xgboost(est, initial_types=initial_type, target_opset=12)
            
            elif isinstance(est, LGBMRegressor):
                initial_type = [("float_input", OXFloatTensorType([None, est.n_features_in_]))]
                onx = convert_lightgbm(est, initial_types=initial_type, target_opset=12)
            else:
                initial_type = [('float_input', FloatTensorType([None, est.n_features_in_]))]
                onx = convert_sklearn(est, initial_types=initial_type)

            with open("model_output_dir/" + modelName + "_" + colsToPredict[i] + ".onnx", "wb") as f:
                f.write(onx.SerializeToString())

    def predictorML_leaveOneOut(self, dfInput,files):
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        for i in range(len(dfInput)):
            elem = dfInputOrig.iloc[i]
            dfInput = dfInputOrig.drop(i)
            #X = dfInput[dfInput.columns[:2]]
            X = dfInput[['rpm','deg','tor']]
            if self.method == 'phase':
                cols = [x for x in dfInput.columns if 'phase' in x]
                Y = dfInput[cols]
            elif self.method == 'ampl':
                cols = [x for x in dfInput.columns if 'ampl' in x]
                Y = dfInput[cols]
            else:
                cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]#dfInput.columns[3:]
                Y = dfInput[cols]

            X_test = pd.DataFrame(elem).T[['rpm','deg','tor']]
            #X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[['rpm','tor']]]
            X_train = X
            #Y_test = pd.DataFrame(elem).T[self.columnToPredict]
            Y_train = Y

            self._train(X_train,Y_train)
            pred = self._predict(X_test)

            namesParam = {'rpm':elem['rpm'],'deg':elem['deg'],"tor":elem['tor']}
            # map = [x.startswith(str(elem['rpm']) + 'rpm' + str(elem['tor']) + 'Torque') for x in files]
            # #map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
            # instanceName = [x for x, y in zip(files, map) if y == True]
            out[i] = namesParam
            for j in range(len(cols)):
                out[i]['prev_'+cols[j]] = pred[0][j]
        dfOut = pd.DataFrame(out).T
        return dfOut


    def predictorML(self, dfInput,testSetDimension):
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]
        if self.method == 'phase':
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]
        elif self.method == 'ampl':
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]
        else:
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]  # dfInput.columns[3:]
            Y = dfInput[cols]

        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=testSetDimension,random_state=0)
        # # X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[['rpm','tor']]]
        # X_train = X
        # # Y_test = pd.DataFrame(elem).T[self.columnToPredict]
        # Y_train = Y


        self._train(X_train, Y_train)

        pred = self._predict(X_test)

        for i in range(len(X_test)):
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            # map = [x.startswith(str(elem['rpm']) + 'rpm' + str(elem['tor']) + 'Torque') for x in files]
            # #map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
            # instanceName = [x for x, y in zip(files, map) if y == True]
            out[i] = namesParam
            for j in range(len(cols)):
                out[i]['prev_' + cols[j]] = pred[i][j]

        dfOut = pd.DataFrame(out).T
        return dfOut

    def genera_numeri_uniformi_interi(self, n, minimo, massimo):
        numeri_uniformi = np.arange(minimo, massimo + 1, (massimo - minimo) // n)
        return numeri_uniformi[:n]

    def getParameterGridSearchCV(self,acronim):
        parameters = {}
        if acronim == 'DT':
            parameters['DT'] = {
                   'estimator__criterion': list(dict.fromkeys(list(['squared_error', 'absolute_error']) +
                                              [self.model.estimator.get_params()['criterion']])),
                   'estimator__max_depth': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,14,21)) +
                                              [self.model.estimator.get_params()['max_depth']])),
                   'estimator__max_leaf_nodes': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,23,28)) +
                                              [self.model.estimator.get_params()['max_leaf_nodes']])),
                   'estimator__min_samples_split': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,2,10)) +
                                              [self.model.estimator.get_params()['min_samples_split']]))
            }
        elif acronim == 'ET':
            parameters['ET']={'estimator__criterion' : list(dict.fromkeys(list(['squared_error', 'absolute_error']) +
                                              [self.model.estimator.get_params()['criterion']])),
                   'estimator__max_depth': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,14,21)) +
                                              [self.model.estimator.get_params()['max_depth']])),
                   'estimator__max_leaf_nodes': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,27,35)) +
                                              [self.model.estimator.get_params()['max_leaf_nodes']])),
                   'estimator__min_samples_split': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,2,10)) +
                                              [self.model.estimator.get_params()['min_samples_split']]))
            }
        elif acronim == 'ERT':
            parameters['ERT'] = {
                   'estimator__n_estimators':list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,20,100)) +
                                              [self.model.estimator.get_params()['n_estimators']])),
                   'estimator__criterion' : list(dict.fromkeys(list(['squared_error', 'absolute_error']) +
                                              [self.model.estimator.get_params()['criterion']])),
                   'estimator__max_depth': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,14,21)) +
                                              [self.model.estimator.get_params()['max_depth']])),
                   'estimator__max_leaf_nodes':  list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,27,35)) +
                                              [self.model.estimator.get_params()['max_leaf_nodes']])),
                   'estimator__min_samples_split': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,2,10)) +
                                              [self.model.estimator.get_params()['min_samples_split']]))
            }
        elif acronim == 'RF':
            parameters['RF'] = {
                   'estimator__n_estimators': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,20,100)) +
                                              [self.model.estimator.get_params()['n_estimators']])),
                   'estimator__criterion': list(dict.fromkeys(list(['squared_error', 'absolute_error']) +
                                              [self.model.estimator.get_params()['criterion']])),
                   'estimator__max_features': list(dict.fromkeys(list(["log2","sqrt"]) +
                                              [self.model.estimator.get_params()['max_features']])),
                   'estimator__max_depth': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,14,21)) +
                                              [self.model.estimator.get_params()['max_depth']])),
                   'estimator__min_samples_split': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,2,10)) +
                                              [self.model.estimator.get_params()['min_samples_split']])),
            }
        elif acronim == 'GBM':
            parameters['GBM'] = {
                'estimator__n_estimators': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,20,100)) +
                                              [self.model.estimator.get_params()['n_estimators']])),
                'estimator__criterion': list(dict.fromkeys(list(['squared_error', 'absolute_error']) +
                                              [self.model.estimator.get_params()['criterion']])),
                'estimator__max_features': list(dict.fromkeys(list(["log2", "sqrt"]) +
                                              [self.model.estimator.get_params()['max_features']])),
                'estimator__max_depth': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,14,21)) +
                                              [self.model.estimator.get_params()['max_depth']])),
                'estimator__min_samples_split': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,2,10)) +
                                              [self.model.estimator.get_params()['min_samples_split']])),
                'estimator__learning_rate':list(dict.fromkeys(list([0.0001, 0.001, 0.01, 0.1, 1.0]) +
                                              [self.model.estimator.get_params()['min_samples_split']])),
            }
        elif acronim == 'XGBM':
            parameters['XGBM'] = {
                'estimator__learning_rate': list(dict.fromkeys(list([0.01,0.2,0.5]) +
                                              [self.model.estimator.get_params()['learning_rate']])),
                'estimator__n_estimator': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,20,100)) +
                                              [self.model.estimator.get_params()['n_estimators']])),
                'estimator__max_depth': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,14,21)) +
                                              [self.model.estimator.get_params()['max_depth']])),
                'estimator__colsample_bytree': list(dict.fromkeys(list([0.3,0.5]) +
                                              [self.model.estimator.get_params()['colsample_bytree']])),
            }
        elif acronim ==  'HGBM':
            parameters['HGBM'] = {
                'estimator__max_iter': list(dict.fromkeys(list([10,100,1000]) +
                                              [self.model.estimator.get_params()['max_iter']])),
                'estimator__max_depth': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,14,21)) +
                                              [self.model.estimator.get_params()['max_depth']])),
                'estimator__learning_rate': list(dict.fromkeys(list([x/ 100 for x in self.genera_numeri_uniformi_interi(5,1,100)]) +
                                              [self.model.estimator.get_params()['learning_rate']])),
                'estimator__max_leaf_nodes':list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,27,35)) +
                                              [self.model.estimator.get_params()['max_leaf_nodes']])),
            }
        elif acronim == 'LGBM':
            parameters['LGBM'] = {
                'estimator__learning_rate': list(dict.fromkeys(list([x / 100 for x in self.genera_numeri_uniformi_interi(5, 1, 100)]) +
                                              [self.model.estimator.get_params()['learning_rate']])),
                 'estimator__max_depth': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5, 14, 21)) +
                                              [self.model.estimator.get_params()['max_depth']])),
                 'estimator__num_leaves': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,10,100)) +
                                              [self.model.estimator.get_params()['num_leaves']])),
                 'estimator__subsample': list(dict.fromkeys(list([0.1,0.3,0.5,0.8]) +
                                              [self.model.estimator.get_params()['subsample']])),
            }
        elif acronim == 'MLP':
            parameters['MLP'] = {
                    'estimator__hidden_layer_sizes': list(dict.fromkeys(list([(100,), (100, 50), (200,), (200, 50)]) +
                                              [self.model.estimator.get_params()['hidden_layer_sizes']])),
                    'estimator__activation': list(dict.fromkeys(list(['tanh', 'relu']) +
                                              [self.model.estimator.get_params()['activation']])),
                    'estimator__solver': list(dict.fromkeys(list(['sgd', 'adam']) +
                                              [self.model.estimator.get_params()['solver']])),
                    'estimator__alpha': list(dict.fromkeys(list([0.0001]) +
                                              [self.model.estimator.get_params()['alpha']])),
                    'estimator__learning_rate': list(dict.fromkeys(list(['adaptive']) +
                                              [self.model.estimator.get_params()['learning_rate']])),
                    'estimator__early_stopping': list(dict.fromkeys(list([True]) +
                                              [self.model.estimator.get_params()['early_stopping']])),
                    'estimator__tol': list(dict.fromkeys(list([1e-4]) +
                                              [self.model.estimator.get_params()['tol']])),
                    'estimator__max_iter': list(dict.fromkeys(list([600]) +
                                              [self.model.estimator.get_params()['max_iter']]))
            }
        elif acronim == 'SVM':
            parameters['SVM'] = {
                     'estimator__kernel':  list(dict.fromkeys(list(['rbf','linear'])+ 
                                               [self.model.estimator.get_params()['kernel']])),
                     'estimator__C':  list(dict.fromkeys(list([1,2,3,5,6,7]) +
                                              [self.model.estimator.get_params()['C']])),
                     'estimator__epsilon': list(dict.fromkeys(list([0.0001,0.00001,0.000001,0.0000001]))),
                     'estimator__gamma': list(dict.fromkeys(list([0.0000011]))),
            }

        return parameters[acronim]

    def getAcronimMethod(self, fileName):

        acronims = {
            'DecisionTreeRegressor': 'DT',
            'ExtraTreeRegressor': 'ET',
            'ExtraTreesRegressor': 'ERT',
            'RandomForestRegressor': 'RF',
            'GradientBoostingRegressor': 'GBM',
            'HistGradientBoostingRegressor': 'HGBM',
            'XGBRegressor': 'XGBM',
            'LGBMRegressor': 'LGBM',
            'SVR': 'SVM',
            'MLPRegressor': 'MLP',
            'MinimumDistance': 'MinDist'
        }

        method = ''

        for elem in acronims.keys():
            if elem in fileName:
                method = acronims[elem]

        return method

    def predictorMLEvalutationOnTrain(self, dfInput, testSetDimension):
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]
        if self.method == 'phase':
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]
        elif self.method == 'ampl':
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]
        else:
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]  # dfInput.columns[3:]
            Y = dfInput[cols]

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=testSetDimension, random_state=0)
        # # X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[['rpm','tor']]]
        # X_train = X
        # # Y_test = pd.DataFrame(elem).T[self.columnToPredict]
        # Y_train = Y

        # self.model = GridSearchCV(self.model, self.getParameterGridSearchCV(self.getAcronimMethod(self.name)),
        #                           n_jobs=-1)

        print("MODEL:", self.name)
        print("TRAINING START:", datetime.datetime.now())

        self._train(X_train, Y_train)

        print("TRAINING END:", datetime.datetime.now())

        pred = self._predict(X_test)

        errorsAcronims = {
            'test_neg_mean_squared_error': 'MSE',
            'test_neg_root_mean_squared_error': 'RMSE',
            'test_neg_mean_absolute_error': 'MAE',
            'test_neg_mean_absolute_percentage_error': 'MAPE'
        }

        # scores = cross_validate(self.model, X_train, Y_train, cv=10, scoring=['neg_mean_squared_error',
        #                                                           'neg_root_mean_squared_error',
        #                                                           'neg_mean_absolute_error',
        #                                                           'neg_mean_absolute_percentage_error'])

        errorKeys = list(errorsAcronims.keys())  # [x for x in list(scores.keys()) if 'test' in x]
        crossValOut = {}

        crossValOut['0_method'] = self.getAcronimMethod(self.name)

        # for el in errorKeys:
        #     crossValOut[errorsAcronims[el]] = abs(scores[el].mean())

        for i in range(len(self.model.estimators_)):
            for method in errorKeys:
                component = list(Y.columns[i:i + 1])[-1].split('_')[-2:]
                if errorsAcronims[method] == 'MSE':
                    crossValOut[str(component[0]) + '_' + str(component[1]) + '_' + errorsAcronims[method]] = \
                        mean_squared_error(Y_test[Y_test.columns[i]],pred[:,i:i+1])
                if errorsAcronims[method] == 'RMSE':
                    crossValOut[str(component[0]) + '_' + str(component[1]) + '_' + errorsAcronims[method]] = \
                        math.sqrt(mean_squared_error(Y_test[Y_test.columns[i]],pred[:,i:i+1]))
                if errorsAcronims[method] == 'MAE':
                    crossValOut[str(component[0]) + '_' + str(component[1]) + '_' + errorsAcronims[method]] = \
                        mean_absolute_error(Y_test[Y_test.columns[i]], pred[:, i:i + 1])
                if errorsAcronims[method] == 'MAPE':
                    crossValOut[str(component[0]) + '_' + str(component[1]) + '_' + errorsAcronims[method]] = \
                        mean_absolute_percentage_error(Y_test[Y_test.columns[i]], pred[:, i:i + 1])


        ## save scores for each model and for the aggregated
        outputFileSummary = 'output_prediction/summaryCrossValidation+_' + self.name.split('_')[-2:][0] \
                            + '_' + self.name.split('_')[-2:][1] + '.csv'
        finalOut = pd.DataFrame(crossValOut, index=[0])
        if os.path.isfile(outputFileSummary):
            # Se il file esiste già, carica il contenuto esistente in un DataFrame
            existing_df = pd.read_csv(outputFileSummary, sep=';', decimal=',')

            # Aggiungi il nuovo contenuto al DataFrame esistente
            finalOut = pd.concat([existing_df, finalOut])
            # finalOut = existing_df.append(pd.DataFrame(crossValOut,index=[0]), ignore_index=True)

            # Salva il DataFrame aggiornato nel file
        finalOut.to_csv(outputFileSummary, sep=';', decimal=',', index=False)

        # ## save best parameters for each model
        # outputFileParameter = 'output_prediction/summaryBestParameter+_' + self.name.split('_')[-2:][0] \
        #                       + '_' + self.name.split('_')[-2:][1] + '.csv'
        # paramOut = {'0_method': self.getAcronimMethod(self.name),
        #             'best_parameters': str(self.model.best_params_)}
        # paramOut = pd.DataFrame(paramOut, index=[0])
        # if os.path.isfile(outputFileParameter):
        #     # Se il file esiste già, carica il contenuto esistente in un DataFrame
        #     existing_df = pd.read_csv(outputFileParameter, sep=';', decimal=',')
        #
        #     # Aggiungi il nuovo contenuto al DataFrame esistente
        #     paramOut = pd.concat([existing_df, paramOut])
        #     # finalOut = existing_df.append(pd.DataFrame(crossValOut,index=[0]), ignore_index=True)
        #
        #     # Salva il DataFrame aggiornato nel file
        # paramOut.to_csv(outputFileParameter, sep=';', decimal=',', index=False)

        for i in range(len(X_test)):
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            # map = [x.startswith(str(elem['rpm']) + 'rpm' + str(elem['tor']) + 'Torque') for x in files]
            # #map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
            # instanceName = [x for x, y in zip(files, map) if y == True]
            out[i] = namesParam
            for j in range(len(cols)):
                out[i]['prev_' + cols[j]] = pred[i][j]

        dfOut = pd.DataFrame(out).T
        return dfOut




    def predictorMLCrossValidationWithHyperparameter(self, dfInput,testSetDimension):
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]
        if self.method == 'phase':
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]
        elif self.method == 'ampl':
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]
        else:
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]  # dfInput.columns[3:]
            Y = dfInput[cols]

        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=testSetDimension,random_state=0)
        # # X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[['rpm','tor']]]
        # X_train = X
        # # Y_test = pd.DataFrame(elem).T[self.columnToPredict]
        # Y_train = Y


        self.model = GridSearchCV(self.model, self.getParameterGridSearchCV(self.getAcronimMethod(self.name)),n_jobs=-1)

        print("MODEL:",self.name)
        print("TRAINING START:",datetime.datetime.now())
        print(self.model.param_grid)

        self._train(X_train, Y_train)
       

        errorsAcronims = {
            'test_neg_mean_squared_error' : 'MSE',
            'test_neg_root_mean_squared_error': 'RMSE',
            'test_neg_mean_absolute_error':'MAE',
            'test_neg_mean_absolute_percentage_error':'MAPE'
        }

        scores = cross_validate(self.model, X, Y, cv=10,scoring=['neg_mean_squared_error',
                                                                  'neg_root_mean_squared_error',
                                                                  'neg_mean_absolute_error',
                                                                  'neg_mean_absolute_percentage_error'])


        errorKeys = list(errorsAcronims.keys())#[x for x in list(scores.keys()) if 'test' in x]
        crossValOut = {}

        crossValOut['0_method'] = self.getAcronimMethod(self.name)

        for el in errorKeys:
            crossValOut[errorsAcronims[el]] = abs(scores[el].mean())


        for i in range(len(self.model.best_estimator_.estimators_)):
            scores = cross_validate(self.model.best_estimator_.estimators_[i], X, Y[Y.columns[i:i + 1]], cv=10,
                                    scoring=['neg_mean_squared_error',
                                             'neg_root_mean_squared_error',
                                             'neg_mean_absolute_error',
                                             'neg_mean_absolute_percentage_error'])

            errorKeys = list(errorsAcronims.keys())
            for el in errorKeys:
                component = list(Y.columns[i:i + 1])[-1].split('_')[-2:]
                crossValOut[str(component[0])+'_'+str(component[1])+'_'+errorsAcronims[el]] = abs(scores[el].mean())

        print("TRAINING END:",datetime.datetime.now())
        print(self.model.best_params_)
        pred = self._predict(X_test)

        ## save scores for each model and for the aggregated
        outputFileSummary = 'output_prediction/summaryCrossValidation+_'+self.name.split('_')[-2:][0]\
                            +'_'+self.name.split('_')[-2:][1]+'.csv'
        finalOut = pd.DataFrame(crossValOut,index=[0])
        if os.path.isfile(outputFileSummary):
            # Se il file esiste già, carica il contenuto esistente in un DataFrame
            existing_df = pd.read_csv(outputFileSummary, sep=';', decimal=',')

            # Aggiungi il nuovo contenuto al DataFrame esistente
            finalOut = pd.concat([existing_df,finalOut])
            #finalOut = existing_df.append(pd.DataFrame(crossValOut,index=[0]), ignore_index=True)

            # Salva il DataFrame aggiornato nel file
        finalOut.to_csv(outputFileSummary, sep=';', decimal=',', index=False)

        ## save best parameters for each model
        outputFileParameter = 'output_prediction/summaryBestParameter+_'+self.name.split('_')[-2:][0]\
                            +'_'+self.name.split('_')[-2:][1]+'.csv'
        paramOut = {'0_method':self.getAcronimMethod(self.name),
                    'best_parameters':str(self.model.best_params_)}
        paramOut = pd.DataFrame(paramOut,index=[0])
        if os.path.isfile(outputFileParameter):
            # Se il file esiste già, carica il contenuto esistente in un DataFrame
            existing_df = pd.read_csv(outputFileParameter, sep=';', decimal=',')

            # Aggiungi il nuovo contenuto al DataFrame esistente
            paramOut = pd.concat([existing_df,paramOut])
            #finalOut = existing_df.append(pd.DataFrame(crossValOut,index=[0]), ignore_index=True)

            # Salva il DataFrame aggiornato nel file
        paramOut.to_csv(outputFileParameter, sep=';', decimal=',', index=False)


        for i in range(len(X_test)):
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            # map = [x.startswith(str(elem['rpm']) + 'rpm' + str(elem['tor']) + 'Torque') for x in files]
            # #map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
            # instanceName = [x for x, y in zip(files, map) if y == True]
            out[i] = namesParam
            for j in range(len(cols)):
                out[i]['prev_' + cols[j]] = pred[i][j]

        dfOut = pd.DataFrame(out).T
        return dfOut

    def predictorMLCrossValidation(self, dfInput,testSetDimension):
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]
        if self.method == 'phase':
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]
        elif self.method == 'ampl':
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]
        else:
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]  # dfInput.columns[3:]
            Y = dfInput[cols]

        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=testSetDimension,random_state=0)
        # # X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[['rpm','tor']]]
        # X_train = X
        # # Y_test = pd.DataFrame(elem).T[self.columnToPredict]
        # Y_train = Y


        self._train(X_train, Y_train)

        errorsAcronims = {
            'test_neg_mean_squared_error' : 'MSE',
            'test_neg_root_mean_squared_error': 'RMSE',
            'test_neg_mean_absolute_error':'MAE',
            'test_neg_mean_absolute_percentage_error':'MAPE'
        }

        scores = cross_validate(self.model, X, Y, cv=10,scoring=['neg_mean_squared_error',
                                                                  'neg_root_mean_squared_error',
                                                                  'neg_mean_absolute_error',
                                                                  'neg_mean_absolute_percentage_error'])


        errorKeys = list(errorsAcronims.keys())#[x for x in list(scores.keys()) if 'test' in x]
        crossValOut = {}

        crossValOut['0_method'] = self.getAcronimMethod(self.name)

        for el in errorKeys:
            crossValOut[errorsAcronims[el]] = abs(scores[el].mean())


        for i in range(len(self.model.estimators_)):
            scores = cross_validate(self.model.estimators_[i], X, Y[Y.columns[i:i + 1]], cv=10,
                                    scoring=['neg_mean_squared_error',
                                             'neg_root_mean_squared_error',
                                             'neg_mean_absolute_error',
                                             'neg_mean_absolute_percentage_error'])

            errorKeys = list(errorsAcronims.keys())
            for el in errorKeys:
                component = list(Y.columns[i:i + 1])[-1].split('_')[-2:]
                crossValOut[str(component[0])+'_'+str(component[1])+'_'+errorsAcronims[el]] = abs(scores[el].mean())

        pred = self._predict(X_test)

        ## save scores for each model and for the aggregated
        outputFileSummary = 'output_prediction/summaryCrossValidation+_'+self.name.split('_')[-2:][0]\
                            +'_'+self.name.split('_')[-2:][1]+'.csv'
        finalOut = pd.DataFrame(crossValOut,index=[0])
        if os.path.isfile(outputFileSummary):
            # Se il file esiste già, carica il contenuto esistente in un DataFrame
            existing_df = pd.read_csv(outputFileSummary, sep=';', decimal=',')

            # Aggiungi il nuovo contenuto al DataFrame esistente
            finalOut = pd.concat([existing_df,finalOut])
            #finalOut = existing_df.append(pd.DataFrame(crossValOut,index=[0]), ignore_index=True)

            # Salva il DataFrame aggiornato nel file
        finalOut.to_csv(outputFileSummary, sep=';', decimal=',', index=False)

        for i in range(len(X_test)):
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            # map = [x.startswith(str(elem['rpm']) + 'rpm' + str(elem['tor']) + 'Torque') for x in files]
            # #map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
            # instanceName = [x for x, y in zip(files, map) if y == True]
            out[i] = namesParam
            for j in range(len(cols)):
                out[i]['prev_' + cols[j]] = pred[i][j]

        dfOut = pd.DataFrame(out).T
        return dfOut

    def predictorML_allForExport(self, dfInput):
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]
        if self.method == 'phase':
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]
        elif self.method == 'ampl':
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]
        else:
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]  # dfInput.columns[3:]
            Y = dfInput[cols]

        # X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[['rpm','tor']]]
        X_train = X
        # Y_test = pd.DataFrame(elem).T[self.columnToPredict]
        Y_train = Y

        print("MODEL:", self.name)
        print("TRAINING START:", datetime.datetime.now())
        self._train(X_train, Y_train)
        print("TRAINING END:", datetime.datetime.now())

        return pd.DataFrame()


    def predictorML_TestForExport(self, dfTest):
        xCols = [x for x in dfTest.columns if 'input' in x]
        x_test = dfTest[xCols]
        x_test.columns = ['tor','rpm','deg']
        cl_ok = ['rpm','deg','tor']
        x_test = x_test[cl_ok]

        dfOut = pd.DataFrame()
        for md in self.model.estimators_:
            pred_col = md.predict(x_test)
            dfOut = pd.concat([dfOut,pd.DataFrame(pred_col)],axis=1)
        #dfOut = self.model.predict(x_test)
        pd.concat([pd.DataFrame(dfOut),x_test],axis=1).to_csv('outputCOMB_SVR_GBR_T27_'+str(datetime.datetime.now().date())+'.csv',sep=';',decimal=',')
        #print(len(pd.DataFrame(dfOut).drop_duplicates()))
        return dfOut


    def predictorMLVariableTrain(self, dfInput, testSetDimension, trainSetDimansion=None):
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]
        if self.method == 'phase':
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]
        elif self.method == 'ampl':
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]
        else:
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]  # dfInput.columns[3:]
            Y = dfInput[cols]

        if trainSetDimansion == None:
            trainSetDimansion = 1-testSetDimension


        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=testSetDimension, random_state=0)

        X_train.reset_index(inplace=True,drop=True)
        X_test.reset_index(inplace=True,drop=True)
        Y_train.reset_index(inplace=True,drop=True)
        Y_test.reset_index(inplace=True,drop=True)

        random.seed(0)

        itemToDrop = random.sample(X_train.index.to_list(),len(X_train) - round(len(X)*trainSetDimansion))

        X_train = X_train.drop(itemToDrop)
        Y_train = Y_train.drop(itemToDrop)


        # # X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[['rpm','tor']]]
        # X_train = X
        # # Y_test = pd.DataFrame(elem).T[self.columnToPredict]
        # Y_train = Y

        self._train(X_train,Y_train)

        pred = self._predict(X_test.reset_index(drop=True))

        for i in range(len(X_test)):
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            # map = [x.startswith(str(elem['rpm']) + 'rpm' + str(elem['tor']) + 'Torque') for x in files]
            # #map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
            # instanceName = [x for x, y in zip(files, map) if y == True]
            out[i] = namesParam
            for j in range(len(cols)):
                out[i]['prev_' + cols[j]] = pred[i][j]

        dfOut = pd.DataFrame(out).T
        return dfOut


class MLModelMultiOutputCombined:

    def __init__(self, modelsList, name, method=''):
        self.model = MultiOutputRegressor(model)
        self.method = method
        self.name = name

    def _train(self, X_train, Y_train):
        self.model.fit(X_train, Y_train)

    def _predict(self, X_test):
        return self.model.predict(X_test)

    #Export del singolo modello da multiOutput
    def exportModel(self,modelName,colsToPredict):
        initial_type = [('float_input', FloatTensorType([None, self.model.n_features_in_]))]
        for i in range(len(self.model.estimators_)):
            est = self.model.estimators_[i]
            onx = convert_sklearn(est, initial_types=initial_type)
            with open(modelName+'_'+colsToPredict[i]+".onnx", "wb") as f:
                f.write(onx.SerializeToString())

    def predictorML_leaveOneOut(self, dfInput,files):
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        for i in range(len(dfInput)):
            elem = dfInputOrig.iloc[i]
            dfInput = dfInputOrig.drop(i)
            #X = dfInput[dfInput.columns[:2]]
            X = dfInput[['rpm','deg','tor']]
            if self.method == 'phase':
                cols = [x for x in dfInput.columns if 'phase' in x]
                Y = dfInput[cols]
            elif self.method == 'ampl':
                cols = [x for x in dfInput.columns if 'ampl' in x]
                Y = dfInput[cols]
            else:
                cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]#dfInput.columns[3:]
                Y = dfInput[cols]

            X_test = pd.DataFrame(elem).T[['rpm','deg','tor']]
            #X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[['rpm','tor']]]
            X_train = X
            #Y_test = pd.DataFrame(elem).T[self.columnToPredict]
            Y_train = Y

            self._train(X_train,Y_train)
            pred = self._predict(X_test)

            namesParam = {'rpm':elem['rpm'],'deg':elem['deg'],"tor":elem['tor']}
            # map = [x.startswith(str(elem['rpm']) + 'rpm' + str(elem['tor']) + 'Torque') for x in files]
            # #map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
            # instanceName = [x for x, y in zip(files, map) if y == True]
            out[i] = namesParam
            for j in range(len(cols)):
                out[i]['prev_'+cols[j]] = pred[0][j]
        dfOut = pd.DataFrame(out).T
        return dfOut


    def predictorML(self, dfInput,testSetDimension):
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]
        if self.method == 'phase':
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]
        elif self.method == 'ampl':
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]
        else:
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]  # dfInput.columns[3:]
            Y = dfInput[cols]

        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=testSetDimension,random_state=0)
        # # X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[['rpm','tor']]]
        # X_train = X
        # # Y_test = pd.DataFrame(elem).T[self.columnToPredict]
        # Y_train = Y


        self._train(X_train, Y_train)

        pred = self._predict(X_test)

        for i in range(len(X_test)):
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            # map = [x.startswith(str(elem['rpm']) + 'rpm' + str(elem['tor']) + 'Torque') for x in files]
            # #map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
            # instanceName = [x for x, y in zip(files, map) if y == True]
            out[i] = namesParam
            for j in range(len(cols)):
                out[i]['prev_' + cols[j]] = pred[i][j]

        dfOut = pd.DataFrame(out).T
        return dfOut

    def getAcronimMethod(self, fileName):

        acronims = {
            'DecisionTreeRegressor': 'DT',
            'ExtraTreeRegressor': 'ET',
            'ExtraTreesRegressor': 'ERT',
            'RandomForestRegressor': 'RF',
            'GradientBoostingRegressor': 'GBM',
            'HistGradientBoostingRegressor': 'HGBM',
            'XGBRegressor': 'XGBM',
            'LGBMRegressor': 'LGBM',
            'SVR': 'SVM',
            'MLPRegressor': 'MLP',
            'MinimumDistance': 'MinDist'
        }

        method = ''

        for elem in acronims.keys():
            if elem in fileName:
                method = acronims[elem]

        return method

    def predictorMLCrossValidation(self, dfInput,testSetDimension):
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]
        if self.method == 'phase':
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]
        elif self.method == 'ampl':
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]
        else:
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]  # dfInput.columns[3:]
            Y = dfInput[cols]

        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=testSetDimension,random_state=0)
        # # X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[['rpm','tor']]]
        # X_train = X
        # # Y_test = pd.DataFrame(elem).T[self.columnToPredict]
        # Y_train = Y


        self._train(X_train, Y_train)

        errorsAcronims = {
            'test_neg_mean_squared_error' : 'MSE',
            'test_neg_root_mean_squared_error': 'RMSE',
            'test_neg_mean_absolute_error':'MAE',
            'test_neg_mean_absolute_percentage_error':'MAPE'
        }

        scores = cross_validate(self.model, X, Y, cv=10,scoring=['neg_mean_squared_error',
                                                                  'neg_root_mean_squared_error',
                                                                  'neg_mean_absolute_error',
                                                                  'neg_mean_absolute_percentage_error'])


        errorKeys = list(errorsAcronims.keys())#[x for x in list(scores.keys()) if 'test' in x]
        crossValOut = {}

        crossValOut['0_method'] = self.getAcronimMethod(self.name)

        for el in errorKeys:
            crossValOut[errorsAcronims[el]] = abs(scores[el].mean())


        for i in range(len(self.model.estimators_)):
            scores = cross_validate(self.model.estimators_[i], X, Y[Y.columns[i:i + 1]], cv=10,
                                    scoring=['neg_mean_squared_error',
                                             'neg_root_mean_squared_error',
                                             'neg_mean_absolute_error',
                                             'neg_mean_absolute_percentage_error'])

            errorKeys = list(errorsAcronims.keys())
            for el in errorKeys:
                component = list(Y.columns[i:i + 1])[-1].split('_')[-2:]
                crossValOut[str(component[0])+'_'+str(component[1])+'_'+errorsAcronims[el]] = abs(scores[el].mean())

        pred = self._predict(X_test)

        ## save scores for each model and for the aggregated
        outputFileSummary = 'output_prediction/summaryCrossValidation+_'+self.name.split('_')[-2:][0]\
                            +'_'+self.name.split('_')[-2:][1]+'.csv'
        finalOut = pd.DataFrame(crossValOut,index=[0])
        if os.path.isfile(outputFileSummary):
            # Se il file esiste già, carica il contenuto esistente in un DataFrame
            existing_df = pd.read_csv(outputFileSummary, sep=';', decimal=',')

            # Aggiungi il nuovo contenuto al DataFrame esistente
            finalOut = pd.concat([existing_df,finalOut])
            #finalOut = existing_df.append(pd.DataFrame(crossValOut,index=[0]), ignore_index=True)

            # Salva il DataFrame aggiornato nel file
        finalOut.to_csv(outputFileSummary, sep=';', decimal=',', index=False)

        for i in range(len(X_test)):
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            # map = [x.startswith(str(elem['rpm']) + 'rpm' + str(elem['tor']) + 'Torque') for x in files]
            # #map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
            # instanceName = [x for x, y in zip(files, map) if y == True]
            out[i] = namesParam
            for j in range(len(cols)):
                out[i]['prev_' + cols[j]] = pred[i][j]

        dfOut = pd.DataFrame(out).T
        return dfOut


    def predictorML_allForExport(self, dfInput, files):
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]
        if self.method == 'phase':
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]
        elif self.method == 'ampl':
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]
        else:
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]  # dfInput.columns[3:]
            Y = dfInput[cols]

        # X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[['rpm','tor']]]
        X_train = X
        # Y_test = pd.DataFrame(elem).T[self.columnToPredict]
        Y_train = Y


        self._train(X_train, Y_train)

        return pd.DataFrame()

    def predictorMLVariableTrain(self, dfInput, testSetDimension, trainSetDimansion=None):
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]
        if self.method == 'phase':
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]
        elif self.method == 'ampl':
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]
        else:
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]  # dfInput.columns[3:]
            Y = dfInput[cols]

        if trainSetDimansion == None:
            trainSetDimansion = 1-testSetDimension


        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=testSetDimension, random_state=0)

        X_train.reset_index(inplace=True,drop=True)
        X_test.reset_index(inplace=True,drop=True)
        Y_train.reset_index(inplace=True,drop=True)
        Y_test.reset_index(inplace=True,drop=True)

        random.seed(0)

        itemToDrop = random.sample(X_train.index.to_list(),len(X_train) - round(len(X)*trainSetDimansion))

        X_train = X_train.drop(itemToDrop)
        Y_train = Y_train.drop(itemToDrop)


        # # X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[['rpm','tor']]]
        # X_train = X
        # # Y_test = pd.DataFrame(elem).T[self.columnToPredict]
        # Y_train = Y

        self._train(X_train,Y_train)

        pred = self._predict(X_test.reset_index(drop=True))

        for i in range(len(X_test)):
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            # map = [x.startswith(str(elem['rpm']) + 'rpm' + str(elem['tor']) + 'Torque') for x in files]
            # #map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
            # instanceName = [x for x, y in zip(files, map) if y == True]
            out[i] = namesParam
            for j in range(len(cols)):
                out[i]['prev_' + cols[j]] = pred[i][j]

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

    def exportModel(self,modelName):
        initial_type = [('float_input', FloatTensorType([None, self.model.n_features_in_]))]
        onx = convert_sklearn(self.model, initial_types=initial_type,
                              options={type(self.model): {'zipmap':False}}, target_opset=12)
        with open(modelName+".onnx", "wb") as f:
            f.write(onx.SerializeToString())
        return


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
#     def __init__(self, name):
#         #self.columnToPredict = columnToPredict
#         #self.model = Pipeline(steps=[('preprocess',StandardScaler()),('model',model)])
#         self.name = name

#     def predictorAutoML_leaveOneOut(self,dfInput,files):
#         dfInputOrig = copy.deepcopy(dfInput)
#         out = {}
#         for i in range(len(dfInput)):
#             elem = dfInputOrig.iloc[i]
#             dfInput = dfInputOrig.drop(i)
#             X = dfInput[dfInput.columns[:2]]
#             Y = dfInput[dfInput.columns[3:]]
#             #Y = dfInput[self.columnToPredict]
#             X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[:2]]
#             X_train = X
#             #Y_test = pd.DataFrame(elem).T[self.columnToPredict]
#             Y_train = Y
#             map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
#             instanceName = [x for x, y in zip(files, map) if y == True]

#             pikName = 'automlPik/' + instanceName[0] + '.pickle'
#             if os.path.exists(pikName):
#                 with open(pikName, 'rb') as f:
#                     autoMl = pickle.load(f)
#             else:
#                 autoMl = autosklearn.regression.AutoSklearnRegressor(
#                     time_left_for_this_task=120,
#                     per_run_time_limit=30,
#                     tmp_folder="/tmp/autosklearn_regression_example_tmp_" + instanceName[0],
#                     n_jobs=-1,
#                     ensemble_size=1,
#                     initial_configurations_via_metalearning=0
#                 )
#                 autoMl.fit(X_train, Y_train, dataset_name='ML-transmission-error')
#                 with open(pikName, 'wb') as f:
#                     pickle.dump(autoMl, f)


#             # autoMl = autosklearn.regression.AutoSklearnRegressor(
#             #     time_left_for_this_task=120,
#             #     per_run_time_limit=30,
#             #     tmp_folder="/tmp/autosklearn_regression_example_tmp_"+instanceName[0],
#             #     n_jobs=-1
#             # )
#             # autoMl.fit(X_train,Y_train,dataset_name='ML-transmission-error')
#             print(autoMl.leaderboard())
#             #pprint(autoMl.show_models(), indent=4)
#             #print(autoMl.show_models())
#             pred = autoMl.predict(X_test)
#             #self._train(X_train,Y_train)
#             #pred = self._predict(X_test)


#             out[i] = {'name':instanceName[0]}
#             for j in range(len(Y_train.columns)):
#                 out[i]['prev_'+Y_train.columns[j]] = pred[0][j]

#             # map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
#             # instanceName = [x for x, y in zip(files, map) if y == True]
#             # out[i] = {'name':instanceName[0],'prev_'+self.columnToPredict:pred[0]}
#         dfOut = pd.DataFrame(out).T
#         return dfOut


#     def predictorAutoML_leaveOneOut_mode(self,dfInput,files,mode):
#         dfInputOrig = copy.deepcopy(dfInput)
#         out = {}
#         for i in range(len(dfInput)):
#             elem = dfInputOrig.iloc[i]
#             dfInput = dfInputOrig.drop(i)
#             X = dfInput[dfInput.columns[:2]]
#             cols = [x for x in dfInput.columns if mode in x]
#             Y = dfInput[cols]
#             #Y = dfInput[self.columnToPredict]
#             X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[:2]]
#             X_train = X
#             #Y_test = pd.DataFrame(elem).T[self.columnToPredict]
#             Y_train = Y
#             map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
#             instanceName = [x for x, y in zip(files, map) if y == True]

#             pikName = 'automlPik/'+ mode+'_' + instanceName[0] + '.pickle'
#             if os.path.exists(pikName):
#                 with open(pikName, 'rb') as f:
#                     autoMl = pickle.load(f)
#             else:
#                 autoMl = autosklearn.regression.AutoSklearnRegressor(
#                     time_left_for_this_task=120,
#                     per_run_time_limit=30,
#                     tmp_folder="/tmp/autosklearn_regression_example_tmp_" + instanceName[0],
#                     n_jobs=-1,
#                 )
#                 autoMl.fit(X_train, Y_train, dataset_name='ML-transmission-error')
#                 with open(pikName, 'wb') as f:
#                     pickle.dump(autoMl, f)


#             # autoMl = autosklearn.regression.AutoSklearnRegressor(
#             #     time_left_for_this_task=120,
#             #     per_run_time_limit=30,
#             #     tmp_folder="/tmp/autosklearn_regression_example_tmp_"+instanceName[0],
#             #     n_jobs=-1
#             # )
#             # autoMl.fit(X_train,Y_train,dataset_name='ML-transmission-error')
#             print(autoMl.leaderboard())
#             #pprint(autoMl.show_models(), indent=4)
#             #print(autoMl.show_models())
#             pred = autoMl.predict(X_test)
#             #self._train(X_train,Y_train)
#             #pred = self._predict(X_test)


#             out[i] = {'name':instanceName[0]}
#             for j in range(len(Y_train.columns)):
#                 out[i]['prev_'+Y_train.columns[j]] = pred[0][j]

#             # map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
#             # instanceName = [x for x, y in zip(files, map) if y == True]
#             # out[i] = {'name':instanceName[0],'prev_'+self.columnToPredict:pred[0]}
#         dfOut = pd.DataFrame(out).T
#         return dfOut


class MinimumDistanceRegressor:
    def _calculateDistanceMatrix(self,X_train,X_test):
        return distance_matrix(X_train,X_test)
    def _getMinimum(self,distMatrix):
        # Inizializza una lista per i risultati
        risultati = []

        # Itera su ogni colonna della matrice
        for colonna in range(len(distMatrix[0])):
            # Trova il minimo per la colonna corrente
            minimo_colonna = float('inf')  # Imposta il minimo iniziale a infinito
            indice_minimo = None  # Indice della riga in cui si trova il minimo

            # Itera su ogni riga della colonna corrente
            for riga in range(len(distMatrix)):
                valore_attuale = distMatrix[riga][colonna]

                # Se il valore attuale è inferiore al minimo corrente, aggiorna il minimo e l'indice
                if valore_attuale < minimo_colonna:
                    minimo_colonna = valore_attuale
                    indice_minimo = riga

            # Aggiungi l'indice del minimo per questa colonna alla lista dei risultati
            risultati.append(indice_minimo)

        # Ritorna la lista degli indici dei minimi per ogni colonna
        return risultati

    def _predict(self,X_train,X_test,Y_train):
        distMatrix = self._calculateDistanceMatrix(X_train,X_test)
        mins = self._getMinimum(distMatrix)
        pred = []
        for i in mins:
            pred.append(Y_train.iloc[i])
        return pred


    def __init__(self, name, method=''):
        #self.columnToPredict = columnToPredict
        #self.model = Pipeline(steps=[('preprocess',StandardScaler()),('model',model)])
        self.name = name
        self.method = method

    def predictorML(self, dfInput, testSetDimension):
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]
        if self.method == 'phase':
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]
        elif self.method == 'ampl':
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]
        else:
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]  # dfInput.columns[3:]
            Y = dfInput[cols]

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=testSetDimension, random_state=0)
        # # X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[['rpm','tor']]]
        # X_train = X
        # # Y_test = pd.DataFrame(elem).T[self.columnToPredict]
        # Y_train = Y

        pred = self._predict(X_train.reset_index(drop=True),X_test.reset_index(drop=True),Y_train.reset_index(drop=True))

        for i in range(len(X_test)):
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            # map = [x.startswith(str(elem['rpm']) + 'rpm' + str(elem['tor']) + 'Torque') for x in files]
            # #map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
            # instanceName = [x for x, y in zip(files, map) if y == True]
            out[i] = namesParam
            for j in range(len(cols)):
                out[i]['prev_' + cols[j]] = pred[i][j]

        dfOut = pd.DataFrame(out).T
        return dfOut


