""" Recovered original RCIM predictor helpers used by training and export. """

import os, copy, datetime
import math, random

import numpy as np
import pandas as pd
from lightgbm import LGBMRegressor
from onnxmltools import convert_lightgbm, convert_xgboost
from onnxmltools.convert.common.data_types import FloatTensorType as OXFloatTensorType
from scipy.spatial import distance_matrix
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error
from sklearn.model_selection import GridSearchCV, cross_validate, train_test_split
from sklearn.multioutput import MultiOutputRegressor, RegressorChain
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from xgboost.sklearn import XGBRegressor

class MLModel:

    """ Original single-estimator wrapper retained for completeness. """

    def __init__(self, model, name, method=''):

        # Keep the Original Wrapper Contract Intact.
        self.model = model
        self.method = method
        self.name = type(model).__name__ + '_' + name

    def _train(self, X_train, Y_train):
        self.model.fit(X_train, Y_train)

    def _predict(self, X_test):
        return self.model.predict(X_test)

    def exportModel(self,modelName):

        """ Export the original single estimator to ONNX format. """

        # Convert the Wrapped Estimator to ONNX With the Original Input Contract.
        initial_type = [('float_input', FloatTensorType([None, self.model.n_features_in_]))]
        onx = convert_sklearn(self.model, initial_types=initial_type)
        with open(modelName+".onnx", "wb") as f: f.write(onx.SerializeToString())

    def gridSearch(self,params):

        """ Wrap the original single estimator in a grid search. """

        # Replace the Estimator With the Historical Grid-Search Wrapper.
        self.model = GridSearchCV(self.model, params, n_jobs=-1)

    def getAcronimMethod(self, fileName):

        """ Map the estimator name to the original report acronym. """

        # Preserve the Original Family-Acronym Mapping Used by the Reports.
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

        # Start With an Empty Fallback Acronym.
        method = ''

        # Resolve the Acronym From the Class Name Fragment.
        for elem in acronims.keys():
            if elem in fileName: method = acronims[elem]

        return method

    def predictorMLCrossValidation(self, dfInput,testSetDimension):

        """ Run the original single-estimator cross-validation path. """

        #
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]

        # Select the Target Surface Exactly Like the Original Workflow.
        if self.method == 'phase': cols = [x for x in dfInput.columns if 'phase' in x]
        elif self.method == 'ampl': cols = [x for x in dfInput.columns if 'ampl' in x]
        else: cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]

        # Materialize the Original Target Dataframe.
        Y = dfInput[cols]

        # Keep the Original Held-Out Split Configuration.
        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=testSetDimension,random_state=0)
        self._train(X_train, Y_train)

        #
        errorsAcronims = {
            'test_neg_mean_squared_error' : 'MSE',
            'test_neg_root_mean_squared_error': 'RMSE',
            'test_neg_mean_absolute_error':'MAE',
            'test_neg_mean_absolute_percentage_error':'MAPE'
        }

        #
        scores = cross_validate(self.model, X, Y, cv=10,scoring=['neg_mean_squared_error',
                                                                  'neg_root_mean_squared_error',
                                                                  'neg_mean_absolute_error',
                                                                  'neg_mean_absolute_percentage_error'],)

        # Keep the Historical Metric Order Used by the CSV Summary.
        errorKeys = list(errorsAcronims.keys())
        crossValOut = {}

        #
        crossValOut['0_method'] = self.getAcronimMethod(self.name)

        # Collapse the Cross-Validation Means Into the Original Flat Summary Shape.
        for el in errorKeys: crossValOut[errorsAcronims[el]] = abs(scores[el].mean())

        #
        pred = self._predict(X_test)

        # Persist the Summary Exactly Where the Original Workflow Expects It.
        outputFileSummary = 'output_prediction/summaryCrossValidation+_' + self.name.split('_')[-2:][0] + '_' + self.name.split('_')[-2:][1] + '.csv'
        finalOut = pd.DataFrame(crossValOut,index=[0])

        if os.path.isfile(outputFileSummary):

            # Append to the Existing Summary File Instead of Overwriting It.
            existing_df = pd.read_csv(outputFileSummary, sep=';', decimal=',')
            finalOut = pd.concat([existing_df,finalOut])

        #
        finalOut.to_csv(outputFileSummary, sep=';', decimal=',', index=False)

        # Export the Held-Out Prediction Rows in the Paper-Era Table Shape.
        for i in range(len(X_test)):

            #
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            out[i] = namesParam

            #
            for j in range(len(cols)): out[i]['prev_' + cols[j]] = pred[i][j]

        dfOut = pd.DataFrame(out).T
        return dfOut

class MLModelChainedMultipleOutput:

    """ Original chained multi-output wrapper retained for completeness. """

    def __init__(self, model, name, method=''):

        # Keep the Chained Multi-Output Wrapper Contract Intact.
        self.model = RegressorChain(model)
        self.method = method
        self.name = type(model).__name__ + '_' + name

    def _train(self, X_train, Y_train):
        self.model.fit(X_train, Y_train)

    def _predict(self, X_test):
        return self.model.predict(X_test)

    def exportModel(self,modelName):

        """ Export Each Estimator in the Regressor Chain to ONNX Format. """

        #
        initial_type = [('float_input', FloatTensorType([None, self.model.n_features_in_]))]

        for i in range(len(self.model.estimators_)):

            #
            est = self.model.estimators_[i]
            onx = convert_sklearn(est, initial_types=initial_type)
            with open(modelName+'_'+str(i)+".onnx", "wb") as f: f.write(onx.SerializeToString())

    def predictorML_leaveOneOut(self, dfInput,files):

        """ Leave-One-Out Cross-Validation for the Chained Multi-Output Wrapper. """

        #
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}

        for i in range(len(dfInput)):

            #
            elem = dfInputOrig.iloc[i]
            dfInput = dfInputOrig.drop(i)
            X = dfInput[dfInput.columns[:2]]

            if self.method == 'phase':

                #
                cols = [x for x in dfInput.columns if 'phase' in x]
                Y = dfInput[cols]

            elif self.method == 'ampl':

                #
                cols = [x for x in dfInput.columns if 'ampl' in x]
                Y = dfInput[cols]

            else:

                #
                cols = dfInput.columns[3:]
                Y = dfInput[cols]

            #
            X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[:2]]
            X_train, Y_train = X, Y

            # Train and Predict the Held-Out Operating Condition.
            self._train(X_train,Y_train)
            pred = self._predict(X_test)

            # Recover the Legacy Instance Name Match for the Exported Row.
            map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
            instanceName = [x for x, y in zip(files, map) if y == True]
            out[i] = {'name':instanceName[0]}

            #
            for j in range(len(cols)): out[i]['prev_'+cols[j]] = pred[0][j]

        #
        dfOut = pd.DataFrame(out).T
        return dfOut

class MLModelMultipleOutput:

    """ Original multi-output wrapper used by the recovered training flows. """

    def __init__(self, model, name, method=''):
        
        # Keep the Wrapped Multi-Output Estimator Contract Intact.
        self.model = MultiOutputRegressor(model)
        self.method = method
        self.name = type(model).__name__ + '_' + name

    def _train(self, X_train, Y_train):
        self.model.fit(X_train, Y_train)

    def _predict(self, X_test):
        return self.model.predict(X_test)

    def exportModel(self, modelName, colsToPredict):

        """ Export Each Estimator in the Multi-Output Wrapper to ONNX Format. """

        # Export Each Wrapped Estimator Separately to Match the Original Surface.
        for i in range(len(self.model.estimators_)):

            #
            est = self.model.estimators_[i]

            # Use the Original Family-Specific ONNX Conversion Branches.
            if isinstance(est, XGBRegressor):

                #
                booster = est.get_booster()
                booster.feature_names = [f"f{i}" for i in range(est.n_features_in_)]

                #
                initial_type = [('float_input', OXFloatTensorType([None, est.n_features_in_]))]
                onx = convert_xgboost(est, initial_types=initial_type, target_opset=12)
            
            elif isinstance(est, LGBMRegressor):

                #
                initial_type = [("float_input", OXFloatTensorType([None, est.n_features_in_]))]
                onx = convert_lightgbm(est, initial_types=initial_type, target_opset=12)

            else:

                #
                initial_type = [('float_input', FloatTensorType([None, est.n_features_in_]))]
                onx = convert_sklearn(est, initial_types=initial_type)

            # Write Each Exported Model Into the Legacy Output Folder Contract.
            with open("model_output_dir/" + modelName + "_" + colsToPredict[i] + ".onnx", "wb") as f:
                f.write(onx.SerializeToString())

    def predictorML_leaveOneOut(self, dfInput,files):

        """ Leave-One-Out Cross-Validation for the Multi-Output Wrapper. """

        #
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        for i in range(len(dfInput)):

            # Remove One Row and Train on the Remaining Samples.
            elem = dfInputOrig.iloc[i]
            dfInput = dfInputOrig.drop(i)
            X = dfInput[['rpm','deg','tor']]

            if self.method == 'phase':

                #
                cols = [x for x in dfInput.columns if 'phase' in x]
                Y = dfInput[cols]

            elif self.method == 'ampl':

                #
                cols = [x for x in dfInput.columns if 'ampl' in x]
                Y = dfInput[cols]

            else:

                #
                cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]
                Y = dfInput[cols]

            #
            X_test = pd.DataFrame(elem).T[['rpm','deg','tor']]
            X_train, Y_train = X, Y

            # Train on the Remaining Rows and Predict the Held-Out Operating Point.
            self._train(X_train,Y_train)
            pred = self._predict(X_test)

            # Export the Legacy Prediction Row for the Held-Out Sample.
            namesParam = {'rpm':elem['rpm'],'deg':elem['deg'],"tor":elem['tor']}
            out[i] = namesParam

            #
            for j in range(len(cols)): out[i]['prev_'+cols[j]] = pred[0][j]

        #
        dfOut = pd.DataFrame(out).T
        return dfOut

    def predictorML(self, dfInput,testSetDimension):

        """ Original multi-output wrapper used by the recovered training flows. """

        #
        out = {}

        # Build the Original Three-Input Feature Matrix.
        X = dfInput[['rpm', 'deg', 'tor']]

        if self.method == 'phase':

            #
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]

        elif self.method == 'ampl':

            #
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]

        else:

            #
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]
            Y = dfInput[cols]

        # Keep the Original Held-Out Split Configuration.
        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=testSetDimension,random_state=0)

        #
        self._train(X_train, Y_train)
        pred = self._predict(X_test)

        # Export the Held-Out Prediction Rows in the Paper-Era Table Shape.
        for i in range(len(X_test)):

            #
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            out[i] = namesParam

            #
            for j in range(len(cols)): out[i]['prev_' + cols[j]] = pred[i][j]

        #
        dfOut = pd.DataFrame(out).T
        return dfOut

    def genera_numeri_uniformi_interi(self, n, minimo, massimo):

        """ Original multi-output wrapper used by the recovered training flows. """

        # Generate the Historical Integer Grid Used by the Search Space Builder.
        numeri_uniformi = np.arange(minimo, massimo + 1, (massimo - minimo) // n)
        return numeri_uniformi[:n]

    def getParameterGridSearchCV(self,acronim):

        """ Original multi-output wrapper used by the recovered training flows. """

        # Build the Family-Specific Hyperparameter Grid Exactly Like the Original Helper.
        parameters = {}

        if acronim == 'DT':

            #
            parameters['DT'] = {
                   'estimator__criterion': list(dict.fromkeys(list(['squared_error', 'absolute_error']) + [self.model.estimator.get_params()['criterion']])),
                   'estimator__max_depth': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,14,21)) + [self.model.estimator.get_params()['max_depth']])),
                   'estimator__max_leaf_nodes': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,23,28)) + [self.model.estimator.get_params()['max_leaf_nodes']])),
                   'estimator__min_samples_split': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,2,10)) + [self.model.estimator.get_params()['min_samples_split']]))
            }

        elif acronim == 'ET':

            #
            parameters['ET']={'estimator__criterion' : list(dict.fromkeys(list(['squared_error', 'absolute_error']) + [self.model.estimator.get_params()['criterion']])),
                   'estimator__max_depth': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,14,21)) + [self.model.estimator.get_params()['max_depth']])),
                   'estimator__max_leaf_nodes': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,27,35)) + [self.model.estimator.get_params()['max_leaf_nodes']])),
                   'estimator__min_samples_split': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,2,10)) + [self.model.estimator.get_params()['min_samples_split']]))
            }

        elif acronim == 'ERT':

            #
            parameters['ERT'] = {
                   'estimator__n_estimators':list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,20,100)) + [self.model.estimator.get_params()['n_estimators']])),
                   'estimator__criterion' : list(dict.fromkeys(list(['squared_error', 'absolute_error']) + [self.model.estimator.get_params()['criterion']])),
                   'estimator__max_depth': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,14,21)) + [self.model.estimator.get_params()['max_depth']])),
                   'estimator__max_leaf_nodes':  list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,27,35)) + [self.model.estimator.get_params()['max_leaf_nodes']])),
                   'estimator__min_samples_split': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,2,10)) + [self.model.estimator.get_params()['min_samples_split']]))
            }

        elif acronim == 'RF':

            #
            parameters['RF'] = {
                   'estimator__n_estimators': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,20,100)) + [self.model.estimator.get_params()['n_estimators']])),
                   'estimator__criterion': list(dict.fromkeys(list(['squared_error', 'absolute_error']) + [self.model.estimator.get_params()['criterion']])),
                   'estimator__max_features': list(dict.fromkeys(list(["log2","sqrt"]) + [self.model.estimator.get_params()['max_features']])),
                   'estimator__max_depth': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,14,21)) + [self.model.estimator.get_params()['max_depth']])),
                   'estimator__min_samples_split': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,2,10)) + [self.model.estimator.get_params()['min_samples_split']])),
            }

        elif acronim == 'GBM':

            #
            parameters['GBM'] = {
                'estimator__n_estimators': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,20,100)) + [self.model.estimator.get_params()['n_estimators']])),
                'estimator__criterion': list(dict.fromkeys(list(['squared_error', 'absolute_error']) + [self.model.estimator.get_params()['criterion']])),
                'estimator__max_features': list(dict.fromkeys(list(["log2", "sqrt"]) + [self.model.estimator.get_params()['max_features']])),
                'estimator__max_depth': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,14,21)) + [self.model.estimator.get_params()['max_depth']])),
                'estimator__min_samples_split': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,2,10)) + [self.model.estimator.get_params()['min_samples_split']])),
                'estimator__learning_rate':list(dict.fromkeys(list([0.0001, 0.001, 0.01, 0.1, 1.0]) + [self.model.estimator.get_params()['min_samples_split']])),
            }

        elif acronim == 'XGBM':

            #
            parameters['XGBM'] = {
                'estimator__learning_rate': list(dict.fromkeys(list([0.01,0.2,0.5]) + [self.model.estimator.get_params()['learning_rate']])),
                'estimator__n_estimator': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,20,100)) + [self.model.estimator.get_params()['n_estimators']])),
                'estimator__max_depth': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,14,21)) + [self.model.estimator.get_params()['max_depth']])),
                'estimator__colsample_bytree': list(dict.fromkeys(list([0.3,0.5]) + [self.model.estimator.get_params()['colsample_bytree']])),
            }

        elif acronim ==  'HGBM':

            #
            parameters['HGBM'] = {
                'estimator__max_iter': list(dict.fromkeys(list([10,100,1000]) + [self.model.estimator.get_params()['max_iter']])),
                'estimator__max_depth': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,14,21)) + [self.model.estimator.get_params()['max_depth']])),
                'estimator__learning_rate': list(dict.fromkeys(list([x/ 100 for x in self.genera_numeri_uniformi_interi(5,1,100)]) + [self.model.estimator.get_params()['learning_rate']])),
                'estimator__max_leaf_nodes':list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,27,35)) + [self.model.estimator.get_params()['max_leaf_nodes']])),
            }

        elif acronim == 'LGBM':

            #
            parameters['LGBM'] = {
                'estimator__learning_rate': list(dict.fromkeys(list([x / 100 for x in self.genera_numeri_uniformi_interi(5, 1, 100)]) + [self.model.estimator.get_params()['learning_rate']])),
                 'estimator__max_depth': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5, 14, 21)) + [self.model.estimator.get_params()['max_depth']])),
                 'estimator__num_leaves': list(dict.fromkeys(list(self.genera_numeri_uniformi_interi(5,10,100)) + [self.model.estimator.get_params()['num_leaves']])),
                 'estimator__subsample': list(dict.fromkeys(list([0.1,0.3,0.5,0.8]) + [self.model.estimator.get_params()['subsample']])),
            }

        elif acronim == 'MLP':

            #
            parameters['MLP'] = {
                    'estimator__hidden_layer_sizes': list(dict.fromkeys(list([(100,), (100, 50), (200,), (200, 50)]) + [self.model.estimator.get_params()['hidden_layer_sizes']])),
                    'estimator__activation': list(dict.fromkeys(list(['tanh', 'relu']) + [self.model.estimator.get_params()['activation']])),
                    'estimator__solver': list(dict.fromkeys(list(['sgd', 'adam']) + [self.model.estimator.get_params()['solver']])),
                    'estimator__alpha': list(dict.fromkeys(list([0.0001]) + [self.model.estimator.get_params()['alpha']])),
                    'estimator__learning_rate': list(dict.fromkeys(list(['adaptive']) + [self.model.estimator.get_params()['learning_rate']])),
                    'estimator__early_stopping': list(dict.fromkeys(list([True]) + [self.model.estimator.get_params()['early_stopping']])),
                    'estimator__tol': list(dict.fromkeys(list([1e-4]) + [self.model.estimator.get_params()['tol']])),
                    'estimator__max_iter': list(dict.fromkeys(list([600]) + [self.model.estimator.get_params()['max_iter']]))
            }

        elif acronim == 'SVM':

            #
            parameters['SVM'] = {
                     'estimator__kernel':  list(dict.fromkeys(list(['rbf','linear']) + [self.model.estimator.get_params()['kernel']])),
                     'estimator__C':  list(dict.fromkeys(list([1,2,3,5,6,7]) + [self.model.estimator.get_params()['C']])),
                     'estimator__epsilon': list(dict.fromkeys(list([0.0001,0.00001,0.000001,0.0000001]))),
                     'estimator__gamma': list(dict.fromkeys(list([0.0000011]))),
            }

        return parameters[acronim]

    def getAcronimMethod(self, fileName):

        """ Map the estimator name to the original report acronym. """

        #
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

        #
        for elem in acronims.keys():
            if elem in fileName: method = acronims[elem]

        return method

    def predictorMLEvalutationOnTrain(self, dfInput, testSetDimension):

        """ Original multi-output wrapper used by the recovered training flows. """

        #
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]

        if self.method == 'phase':

            #
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]

        elif self.method == 'ampl':

            #
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]

        else:

            #
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]
            Y = dfInput[cols]

        #
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=testSetDimension, random_state=0)
        print("MODEL:", self.name)
        print("TRAINING START:", datetime.datetime.now())

        #
        self._train(X_train, Y_train)
        print("TRAINING END:", datetime.datetime.now())

        #
        pred = self._predict(X_test)

        errorsAcronims = {
            'test_neg_mean_squared_error': 'MSE',
            'test_neg_root_mean_squared_error': 'RMSE',
            'test_neg_mean_absolute_error': 'MAE',
            'test_neg_mean_absolute_percentage_error': 'MAPE'
        }

        #
        errorKeys = list(errorsAcronims.keys())
        crossValOut = {}
        crossValOut['0_method'] = self.getAcronimMethod(self.name)

        for i in range(len(self.model.estimators_)):

            #
            for method in errorKeys:

                #
                component = list(Y.columns[i:i + 1])[-1].split('_')[-2:]
                if errorsAcronims[method] == 'MSE':  crossValOut[str(component[0]) + '_' + str(component[1]) + '_' + errorsAcronims[method]] = mean_squared_error(Y_test[Y_test.columns[i]],pred[:,i:i+1])
                if errorsAcronims[method] == 'RMSE': crossValOut[str(component[0]) + '_' + str(component[1]) + '_' + errorsAcronims[method]] = math.sqrt(mean_squared_error(Y_test[Y_test.columns[i]],pred[:,i:i+1]))
                if errorsAcronims[method] == 'MAE':  crossValOut[str(component[0]) + '_' + str(component[1]) + '_' + errorsAcronims[method]] = mean_absolute_error(Y_test[Y_test.columns[i]], pred[:, i:i + 1])
                if errorsAcronims[method] == 'MAPE': crossValOut[str(component[0]) + '_' + str(component[1]) + '_' + errorsAcronims[method]] = mean_absolute_percentage_error(Y_test[Y_test.columns[i]], pred[:, i:i + 1])

        # Persist the summary exactly where the original workflow expects it.
        outputFileSummary = 'output_prediction/summaryCrossValidation+_' + self.name.split('_')[-2:][0] + '_' + self.name.split('_')[-2:][1] + '.csv'
        finalOut = pd.DataFrame(crossValOut, index=[0])

        if os.path.isfile(outputFileSummary):

            #
            existing_df = pd.read_csv(outputFileSummary, sep=';', decimal=',')
            finalOut = pd.concat([existing_df, finalOut])

        #
        finalOut.to_csv(outputFileSummary, sep=';', decimal=',', index=False)

        for i in range(len(X_test)):

            #
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            out[i] = namesParam

            #
            for j in range(len(cols)): out[i]['prev_' + cols[j]] = pred[i][j]

        dfOut = pd.DataFrame(out).T
        return dfOut

    def predictorMLCrossValidationWithHyperparameter(self, dfInput,testSetDimension):

        """ Original multi-output wrapper used by the recovered training flows. """

        #
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]

        if self.method == 'phase':

            #
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]

        elif self.method == 'ampl':

            #
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]

        else:

            #
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]
            Y = dfInput[cols]

        #
        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=testSetDimension,random_state=0)

        # Wrap the original multi-output estimator in the historical grid-search path.
        self.model = GridSearchCV(self.model, self.getParameterGridSearchCV(self.getAcronimMethod(self.name)),n_jobs=-1)

        #
        print("MODEL:",self.name)
        print("TRAINING START:",datetime.datetime.now())
        print(self.model.param_grid)

        #
        self._train(X_train, Y_train)

        #
        errorsAcronims = {
            'test_neg_mean_squared_error' : 'MSE',
            'test_neg_root_mean_squared_error': 'RMSE',
            'test_neg_mean_absolute_error':'MAE',
            'test_neg_mean_absolute_percentage_error':'MAPE'
        }

        #
        scores = cross_validate(self.model, X, Y, cv=10,scoring=['neg_mean_squared_error',
                                                                  'neg_root_mean_squared_error',
                                                                  'neg_mean_absolute_error',
                                                                  'neg_mean_absolute_percentage_error'])

        #
        errorKeys = list(errorsAcronims.keys())
        crossValOut = {}
        crossValOut['0_method'] = self.getAcronimMethod(self.name)

        #
        for el in errorKeys: crossValOut[errorsAcronims[el]] = abs(scores[el].mean())

        #
        for i in range(len(self.model.best_estimator_.estimators_)):

            #
            scores = cross_validate(self.model.best_estimator_.estimators_[i], X, Y[Y.columns[i:i + 1]], cv=10,
                                    scoring=['neg_mean_squared_error',
                                             'neg_root_mean_squared_error',
                                             'neg_mean_absolute_error',
                                             'neg_mean_absolute_percentage_error'])

            #
            errorKeys = list(errorsAcronims.keys())

            for el in errorKeys:

                #
                component = list(Y.columns[i:i + 1])[-1].split('_')[-2:]
                crossValOut[str(component[0])+'_'+str(component[1])+'_'+errorsAcronims[el]] = abs(scores[el].mean())

        #
        print("TRAINING END:",datetime.datetime.now())
        print(self.model.best_params_)
        pred = self._predict(X_test)

        # Persist the cross-validation summary exactly where the original workflow expects it.
        outputFileSummary = 'output_prediction/summaryCrossValidation+_' + self.name.split('_')[-2:][0] + '_' + self.name.split('_')[-2:][1] + '.csv'
        finalOut = pd.DataFrame(crossValOut,index=[0])

        #
        if os.path.isfile(outputFileSummary):

            #
            existing_df = pd.read_csv(outputFileSummary, sep=';', decimal=',')
            finalOut = pd.concat([existing_df,finalOut])

        #
        finalOut.to_csv(outputFileSummary, sep=';', decimal=',', index=False)

        # Persist the best-parameter summary exactly where the original workflow expects it.
        outputFileParameter = 'output_prediction/summaryBestParameter+_' + self.name.split('_')[-2:][0] + '_' + self.name.split('_')[-2:][1] + '.csv'
        paramOut = {'0_method':self.getAcronimMethod(self.name), 'best_parameters':str(self.model.best_params_)}
        paramOut = pd.DataFrame(paramOut,index=[0])

        #
        if os.path.isfile(outputFileParameter):

            #
            existing_df = pd.read_csv(outputFileParameter, sep=';', decimal=',')
            paramOut = pd.concat([existing_df,paramOut])

        #
        paramOut.to_csv(outputFileParameter, sep=';', decimal=',', index=False)

        # Export the held-out prediction rows in the paper-era table shape.
        for i in range(len(X_test)):

            #
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            out[i] = namesParam

            #
            for j in range(len(cols)): out[i]['prev_' + cols[j]] = pred[i][j]

        #
        dfOut = pd.DataFrame(out).T
        return dfOut

    def predictorMLCrossValidation(self, dfInput,testSetDimension):

        """ Original multi-output wrapper used by the recovered training flows. """

        # Build the original three-input feature matrix.
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]

        if self.method == 'phase':

            #
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]

        elif self.method == 'ampl':

            #
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]

        else:

            #
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]
            Y = dfInput[cols]

        #
        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=testSetDimension,random_state=0)

        #
        self._train(X_train, Y_train)

        #
        errorsAcronims = {
            'test_neg_mean_squared_error' : 'MSE',
            'test_neg_root_mean_squared_error': 'RMSE',
            'test_neg_mean_absolute_error':'MAE',
            'test_neg_mean_absolute_percentage_error':'MAPE'
        }

        #
        scores = cross_validate(self.model, X, Y, cv=10,scoring=['neg_mean_squared_error',
                                                                  'neg_root_mean_squared_error',
                                                                  'neg_mean_absolute_error',
                                                                  'neg_mean_absolute_percentage_error'])

        #
        errorKeys = list(errorsAcronims.keys())#[x for x in list(scores.keys()) if 'test' in x]
        crossValOut = {}
        crossValOut['0_method'] = self.getAcronimMethod(self.name)

        #
        for el in errorKeys: crossValOut[errorsAcronims[el]] = abs(scores[el].mean())

        for i in range(len(self.model.estimators_)):

            #
            scores = cross_validate(self.model.estimators_[i], X, Y[Y.columns[i:i + 1]], cv=10,
                                    scoring=['neg_mean_squared_error',
                                             'neg_root_mean_squared_error',
                                             'neg_mean_absolute_error',
                                             'neg_mean_absolute_percentage_error'])

            #
            errorKeys = list(errorsAcronims.keys())

            for el in errorKeys:

                #
                component = list(Y.columns[i:i + 1])[-1].split('_')[-2:]
                crossValOut[str(component[0])+'_'+str(component[1])+'_'+errorsAcronims[el]] = abs(scores[el].mean())

        #
        pred = self._predict(X_test)

        # Persist the summary exactly where the original workflow expects it.
        outputFileSummary = 'output_prediction/summaryCrossValidation+_' + self.name.split('_')[-2:][0] + '_' + self.name.split('_')[-2:][1] + '.csv'
        finalOut = pd.DataFrame(crossValOut,index=[0])

        #
        if os.path.isfile(outputFileSummary):

            #
            existing_df = pd.read_csv(outputFileSummary, sep=';', decimal=',')
            finalOut = pd.concat([existing_df,finalOut])

        #
        finalOut.to_csv(outputFileSummary, sep=';', decimal=',', index=False)

        # Export the held-out prediction rows in the paper-era table shape.
        for i in range(len(X_test)):

            #
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            out[i] = namesParam

            #
            for j in range(len(cols)): out[i]['prev_' + cols[j]] = pred[i][j]

        #
        dfOut = pd.DataFrame(out).T
        return dfOut

    def predictorML_allForExport(self, dfInput, testSetDimension=None):

        """ Original multi-output wrapper used by the recovered training flows. """

        #
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]

        if self.method == 'phase':

            #
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]

        elif self.method == 'ampl':

            #
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]

        else:

            #
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]
            Y = dfInput[cols]

        #
        X_train, Y_train = X, Y

        #
        print("MODEL:", self.name)
        print("TRAINING START:", datetime.datetime.now())
        self._train(X_train, Y_train)
        print("TRAINING END:", datetime.datetime.now())

        return pd.DataFrame()

    def predictorML_TestForExport(self, dfTest):

        """ Run one already-trained export bank on one explicit test table. """

        #
        xCols = [x for x in dfTest.columns if 'input' in x]
        x_test = dfTest[xCols]
        x_test.columns = ['tor','rpm','deg']
        cl_ok = ['rpm','deg','tor']
        x_test = x_test[cl_ok]

        #
        dfOut = pd.DataFrame()

        for md in self.model.estimators_:

            #
            pred_col = md.predict(x_test)
            dfOut = pd.concat([dfOut,pd.DataFrame(pred_col)],axis=1)

        #
        pd.concat([pd.DataFrame(dfOut),x_test],axis=1).to_csv('outputCOMB_SVR_GBR_T27_'+str(datetime.datetime.now().date())+'.csv',sep=';',decimal=',')
        return dfOut

    def predictorMLVariableTrain(self, dfInput, testSetDimension, trainSetDimansion=None):

        """ Original multi-output wrapper used by the recovered training flows. """

        #
        out = {}

        # Build the original three-input feature matrix.
        X = dfInput[['rpm', 'deg', 'tor']]

        if self.method == 'phase':

            #
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]

        elif self.method == 'ampl':

            #
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]

        else:

            #
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]
            Y = dfInput[cols]

        #
        if trainSetDimansion == None: trainSetDimansion = 1 - testSetDimension

        #
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=testSetDimension, random_state=0)

        #
        X_train.reset_index(inplace=True,drop=True)
        X_test.reset_index(inplace=True,drop=True)
        Y_train.reset_index(inplace=True,drop=True)
        Y_test.reset_index(inplace=True,drop=True)

        #
        random.seed(0)

        #
        itemToDrop = random.sample(X_train.index.to_list(),len(X_train) - round(len(X)*trainSetDimansion))

        #
        X_train = X_train.drop(itemToDrop)
        Y_train = Y_train.drop(itemToDrop)

        #
        self._train(X_train,Y_train)

        #
        pred = self._predict(X_test.reset_index(drop=True))

        # Export the held-out prediction rows in the paper-era table shape.
        for i in range(len(X_test)):

            #
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            out[i] = namesParam

            #
            for j in range(len(cols)): out[i]['prev_' + cols[j]] = pred[i][j]

        #
        dfOut = pd.DataFrame(out).T
        return dfOut

class MLModelMultiOutputCombined:

    """ Original mixed multi-output wrapper retained for completeness. """

    def __init__(self, modelsList, name, method=''):

        #
        self.model = MultiOutputRegressor(model)
        self.method = method
        self.name = name

    def _train(self, X_train, Y_train):
        self.model.fit(X_train, Y_train)

    def _predict(self, X_test):
        return self.model.predict(X_test)

    def exportModel(self,modelName,colsToPredict):

        """ Export The Single Model From The Wrapped Multi-Output Estimator. """

        #
        initial_type = [('float_input', FloatTensorType([None, self.model.n_features_in_]))]

        for i in range(len(self.model.estimators_)):

            #
            est = self.model.estimators_[i]
            onx = convert_sklearn(est, initial_types=initial_type)

            #
            with open(modelName+'_'+colsToPredict[i]+".onnx", "wb") as f: f.write(onx.SerializeToString())

    def predictorML_leaveOneOut(self, dfInput,files):

        """ Original multi-output wrapper used by the recovered training flows. """

        #
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}

        for i in range(len(dfInput)):

            #
            elem = dfInputOrig.iloc[i]
            dfInput = dfInputOrig.drop(i)
            X = dfInput[['rpm','deg','tor']]

            if self.method == 'phase':

                #
                cols = [x for x in dfInput.columns if 'phase' in x]
                Y = dfInput[cols]

            elif self.method == 'ampl':

                #
                cols = [x for x in dfInput.columns if 'ampl' in x]
                Y = dfInput[cols]

            else:

                #
                cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]#dfInput.columns[3:]
                Y = dfInput[cols]

            #
            X_test = pd.DataFrame(elem).T[['rpm','deg','tor']]
            X_train, Y_train = X, Y

            #
            self._train(X_train,Y_train)
            pred = self._predict(X_test)

            #
            namesParam = {'rpm':elem['rpm'],'deg':elem['deg'],"tor":elem['tor']}
            out[i] = namesParam

            #
            for j in range(len(cols)): out[i]['prev_' + cols[j]] = pred[0][j]

        #
        dfOut = pd.DataFrame(out).T
        return dfOut

    def predictorML(self, dfInput,testSetDimension):

        """ Original multi-output wrapper used by the recovered training flows. """

        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]

        if self.method == 'phase':

            #
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]

        elif self.method == 'ampl':

            #
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]

        else:

            #
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]
            Y = dfInput[cols]

        #
        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=testSetDimension,random_state=0)
        self._train(X_train, Y_train)

        #
        pred = self._predict(X_test)

        for i in range(len(X_test)):

            #
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            out[i] = namesParam

            #
            for j in range(len(cols)): out[i]['prev_' + cols[j]] = pred[i][j]

        #
        dfOut = pd.DataFrame(out).T
        return dfOut

    def getAcronimMethod(self, fileName):

        """ Map the estimator name to the original report acronym. """

        #
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

        #
        method = ''

        #
        for elem in acronims.keys():
            if elem in fileName: method = acronims[elem]

        return method

    def predictorMLCrossValidation(self, dfInput,testSetDimension):

        """ Original multi-output wrapper used by the recovered training flows. """

        #
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]

        if self.method == 'phase':

            #
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]

        elif self.method == 'ampl':

            #
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]

        else:

            #
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]
            Y = dfInput[cols]

        #
        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=testSetDimension,random_state=0)
        self._train(X_train, Y_train)

        #
        errorsAcronims = {
            'test_neg_mean_squared_error' : 'MSE',
            'test_neg_root_mean_squared_error': 'RMSE',
            'test_neg_mean_absolute_error':'MAE',
            'test_neg_mean_absolute_percentage_error':'MAPE'
        }

        #
        scores = cross_validate(self.model, X, Y, cv=10,scoring=['neg_mean_squared_error',
                                                                  'neg_root_mean_squared_error',
                                                                  'neg_mean_absolute_error',
                                                                  'neg_mean_absolute_percentage_error'])

        #
        errorKeys = list(errorsAcronims.keys())
        crossValOut = {}
        crossValOut['0_method'] = self.getAcronimMethod(self.name)

        #
        for el in errorKeys: crossValOut[errorsAcronims[el]] = abs(scores[el].mean())

        for i in range(len(self.model.estimators_)):

            #
            scores = cross_validate(self.model.estimators_[i], X, Y[Y.columns[i:i + 1]], cv=10,
                                    scoring=['neg_mean_squared_error',
                                             'neg_root_mean_squared_error',
                                             'neg_mean_absolute_error',
                                             'neg_mean_absolute_percentage_error'])

            #
            errorKeys = list(errorsAcronims.keys())

            for el in errorKeys:

                #
                component = list(Y.columns[i:i + 1])[-1].split('_')[-2:]
                crossValOut[str(component[0])+'_'+str(component[1])+'_'+errorsAcronims[el]] = abs(scores[el].mean())

        #
        pred = self._predict(X_test)

        # Persist the summary exactly where the original workflow expects it.
        outputFileSummary = 'output_prediction/summaryCrossValidation+_' + self.name.split('_')[-2:][0] + '_' + self.name.split('_')[-2:][1] + '.csv'
        finalOut = pd.DataFrame(crossValOut,index=[0])

        if os.path.isfile(outputFileSummary):

            #
            existing_df = pd.read_csv(outputFileSummary, sep=';', decimal=',')
            finalOut = pd.concat([existing_df,finalOut])

        #
        finalOut.to_csv(outputFileSummary, sep=';', decimal=',', index=False)

        for i in range(len(X_test)):

            #
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            out[i] = namesParam

            #
            for j in range(len(cols)): out[i]['prev_' + cols[j]] = pred[i][j]

        #
        dfOut = pd.DataFrame(out).T
        return dfOut

    def predictorML_allForExport(self, dfInput, files):

        """ Original multi-output wrapper used by the recovered training flows. """

        #
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]

        if self.method == 'phase':

            #
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]

        elif self.method == 'ampl':

            #
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]

        else:

            #
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]
            Y = dfInput[cols]

        #
        X_train, Y_train = X, Y
        self._train(X_train, Y_train)

        return pd.DataFrame()

    def predictorMLVariableTrain(self, dfInput, testSetDimension, trainSetDimansion=None):

        """ Original multi-output wrapper used by the recovered training flows. """

        #
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]

        if self.method == 'phase':

            #
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]

        elif self.method == 'ampl':

            #
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]

        else:

            #
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]
            Y = dfInput[cols]

        #
        if trainSetDimansion == None: trainSetDimansion = 1 - testSetDimension

        #
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=testSetDimension, random_state=0)

        #
        X_train.reset_index(inplace=True,drop=True)
        X_test.reset_index(inplace=True,drop=True)
        Y_train.reset_index(inplace=True,drop=True)
        Y_test.reset_index(inplace=True,drop=True)

        #
        random.seed(0)

        #
        itemToDrop = random.sample(X_train.index.to_list(),len(X_train) - round(len(X)*trainSetDimansion))

        #
        X_train = X_train.drop(itemToDrop)
        Y_train = Y_train.drop(itemToDrop)

        #
        self._train(X_train,Y_train)

        #
        pred = self._predict(X_test.reset_index(drop=True))

        for i in range(len(X_test)):

            #
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            out[i] = namesParam

            #
            for j in range(len(cols)): out[i]['prev_' + cols[j]] = pred[i][j]

        #
        dfOut = pd.DataFrame(out).T
        return dfOut

class MLPipeline:

    """ Original pipeline-based wrapper retained for completeness. """

    def __init__(self, model, name, columnToPredict):

        #
        self.columnToPredict = columnToPredict
        self.model = Pipeline(steps=[('preprocess',StandardScaler()),('model',model)])
        self.name = name

    def _train(self, X_train, Y_train):
        self.model.fit(X_train, Y_train)

    def _predict(self, X_test):
        return self.model.predict(X_test)

    def gridSearch(self,params):

        #
        self.model = GridSearchCV(self.model, params, n_jobs=-1)

    def exportModel(self,modelName):

        #
        initial_type = [('float_input', FloatTensorType([None, self.model.n_features_in_]))]
        onx = convert_sklearn(self.model, initial_types=initial_type, options={type(self.model): {'zipmap':False}}, target_opset=12)

        #
        with open(modelName+".onnx", "wb") as f: f.write(onx.SerializeToString())
        return

    def predictorML_leaveOneOut(self, dfInput,files):

        """ Original multi-output wrapper used by the recovered training flows. """

        #
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}

        for i in range(len(dfInput)):

            #
            elem = dfInputOrig.iloc[i]
            dfInput = dfInputOrig.drop(i)
            X = dfInput[dfInput.columns[:2]]
            Y = dfInput[self.columnToPredict]
            X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[:2]]
            X_train, Y_train = X, Y

            # Train on the remaining rows and predict the held-out operating point.
            self._train(X_train,Y_train)
            pred = self._predict(X_test)

            #
            map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
            instanceName = [x for x, y in zip(files, map) if y == True]
            out[i] = {'name':instanceName[0],'prev_'+self.columnToPredict:pred[0]}

        #
        dfOut = pd.DataFrame(out).T
        return dfOut

    def predictorML_singleModel_leaveOneOut(self, dfInput,files):

        """ Original multi-output wrapper used by the recovered training flows. """

        #
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}

        for i in range(len(dfInput)):

            #
            elem = dfInputOrig.iloc[i]
            dfInput = dfInputOrig.drop(i)
            x_columns = list(dfInput.columns[:2]) + list(dfInput.columns[3:])
            x_columns.remove(self.columnToPredict)
            X = dfInput[x_columns]
            Y = dfInput[self.columnToPredict]
            X_test = pd.DataFrame(elem).T[x_columns]
            X_train, Y_train = X, Y

            # Train on the remaining rows and predict the held-out operating point.
            self._train(X_train,Y_train)
            pred = self._predict(X_test)

            #
            map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
            instanceName = [x for x, y in zip(files, map) if y == True]
            out[i] = {'name':instanceName[0],'prev_'+self.columnToPredict:pred[0]}

        #
        dfOut = pd.DataFrame(out).T
        return dfOut

class MinimumDistanceRegressor:

    """ Original minimum-distance baseline retained for completeness. """

    def _calculateDistanceMatrix(self,X_train,X_test):

        #
        return distance_matrix(X_train,X_test)

    def _getMinimum(self,distMatrix):

        # Collect the index of the nearest training sample for each test sample.
        risultati = []

        # Process the distance matrix one test-sample column at a time.
        for colonna in range(len(distMatrix[0])):

            #
            minimo_colonna = float('inf')
            indice_minimo = None

            # Scan every training sample distance for the current test sample.
            for riga in range(len(distMatrix)):

                #
                valore_attuale = distMatrix[riga][colonna]

                # Keep the row index that minimizes the current column distance.
                if valore_attuale < minimo_colonna: minimo_colonna, indice_minimo = valore_attuale, riga

            #
            risultati.append(indice_minimo)

        return risultati

    def _predict(self,X_train,X_test,Y_train):

        """ Predict the output for each test sample as the output of the nearest training sample. """

        #
        distMatrix = self._calculateDistanceMatrix(X_train,X_test)
        mins = self._getMinimum(distMatrix)
        pred = []

        #
        for i in mins: pred.append(Y_train.iloc[i])
        return pred

    def __init__(self, name, method=''):

        #
        self.name = name
        self.method = method

    def predictorML(self, dfInput, testSetDimension):

        """ Original multi-output wrapper used by the recovered training flows. """

        #
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]

        if self.method == 'phase':

            #
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]

        elif self.method == 'ampl':

            #
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]

        else:

            #
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]
            Y = dfInput[cols]

        #
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=testSetDimension, random_state=0)
        pred = self._predict(X_train.reset_index(drop=True),X_test.reset_index(drop=True),Y_train.reset_index(drop=True))

        for i in range(len(X_test)):

            #
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            out[i] = namesParam

            #
            for j in range(len(cols)): out[i]['prev_' + cols[j]] = pred[i][j]

        #
        dfOut = pd.DataFrame(out).T
        return dfOut
