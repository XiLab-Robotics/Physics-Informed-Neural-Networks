""" Recovered original RCIM predictor helpers used by training and export. """

import os, copy, datetime, pickle, traceback
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
from sklearn.model_selection import GridSearchCV, ParameterGrid, cross_validate, train_test_split
from sklearn.multioutput import MultiOutputRegressor, RegressorChain
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVR
from xgboost.sklearn import XGBRegressor

METHOD_ACRONYMS = {
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
    'ELMRegressor': 'ELM',
    'MinimumDistance': 'MinDist',
}

ERROR_ACRONYMS = {
    'test_neg_mean_squared_error': 'MSE',
    'test_neg_root_mean_squared_error': 'RMSE',
    'test_neg_mean_absolute_error': 'MAE',
    'test_neg_mean_absolute_percentage_error': 'MAPE',
}
SVR_VARIANT_KEY = "__rcim_svr_variant__"
SVR_VARIANT_PARAMETERS_KEY = "__rcim_svr_parameters__"
SVR_VARIANT_RBF = "paper_faithful_rbf"
SVR_VARIANT_LINEAR_FALLBACK = "pragmatic_linear_fallback"

def _resolve_model_display_name(model):

    """ Resolve one legacy wrapper display name with optional repository override. """

    # Resolve the Legacy Wrapper Display Name.
    return getattr(model, "_rcim_display_name", type(model).__name__)

class MLModel:

    """ Original single-estimator wrapper retained for completeness. """

    def __init__(self, model, name, method=''):

        # Keep the Original Wrapper Contract Intact.
        self.model = model
        self.method = method
        self.name = _resolve_model_display_name(model) + '_' + name

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

    def get_method_acronym(self, fileName):

        """ Map the estimator name to the original report acronym. """

        # Start With an Empty Fallback Acronym.
        method = ''

        # Resolve the Acronym From the Class Name Fragment.
        for elem in METHOD_ACRONYMS.keys():
            if elem in fileName: method = METHOD_ACRONYMS[elem]

        return method

    def predictorMLCrossValidation(self, dfInput,testSetDimension):

        """ Run the original single-estimator cross-validation path. """

        # Initialize the Legacy Prediction Export Buffer.
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

        # Define the Historical Error-Acronym Mapping Used by the Summary CSV.
        error_acronyms = {
            'test_neg_mean_squared_error' : 'MSE',
            'test_neg_root_mean_squared_error': 'RMSE',
            'test_neg_mean_absolute_error':'MAE',
            'test_neg_mean_absolute_percentage_error':'MAPE'
        }

        # Run the Historical Cross-Validation Metric Sweep.
        scores = cross_validate(self.model, X, Y, cv=10,scoring=['neg_mean_squared_error',
                                                                  'neg_root_mean_squared_error',
                                                                  'neg_mean_absolute_error',
                                                                  'neg_mean_absolute_percentage_error'],)

        # Keep the Historical Metric Order Used by the CSV Summary.
        errorKeys = list(error_acronyms.keys())
        crossValOut = {}

        # Store the Estimator Acronym in the Legacy Summary Format.
        crossValOut['0_method'] = self.get_method_acronym(self.name)

        # Collapse the Cross-Validation Means Into the Original Flat Summary Shape.
        for el in errorKeys: crossValOut[error_acronyms[el]] = abs(scores[el].mean())

        # Predict the Held-Out Split With the Trained Estimator.
        pred = self._predict(X_test)

        # Persist the Summary Exactly Where the Original Workflow Expects It.
        outputFileSummary = 'output_prediction/summaryCrossValidation+_' + self.name.split('_')[-2:][0] + '_' + self.name.split('_')[-2:][1] + '.csv'
        finalOut = pd.DataFrame(crossValOut,index=[0])

        if os.path.isfile(outputFileSummary):

            # Append to the Existing Summary File Instead of Overwriting It.
            existing_df = pd.read_csv(outputFileSummary, sep=';', decimal=',')
            finalOut = pd.concat([existing_df,finalOut])

        # Write the Summary Back to the Historical Output Path.
        finalOut.to_csv(outputFileSummary, sep=';', decimal=',', index=False)

        # Export the Held-Out Prediction Rows in the Paper-Era Table Shape.
        for i in range(len(X_test)):

            # Read the Held-Out Operating Condition for This Exported Row.
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            out[i] = namesParam

            # Append One Predicted Target Value to the Exported Row.
            for j in range(len(cols)): out[i]['prev_' + cols[j]] = pred[i][j]

        dfOut = pd.DataFrame(out).T
        return dfOut

class MLModelChainedMultipleOutput:

    """ Original chained multi-output wrapper retained for completeness. """

    def __init__(self, model, name, method=''):

        # Keep the Chained Multi-Output Wrapper Contract Intact.
        self.model = RegressorChain(model)
        self.method = method
        self.name = _resolve_model_display_name(model) + '_' + name

    def _train(self, X_train, Y_train):
        self.model.fit(X_train, Y_train)

    def _predict(self, X_test):
        return self.model.predict(X_test)

    def exportModel(self,modelName):

        """ Export Each Estimator in the Regressor Chain to ONNX Format. """

        # Build the ONNX Input Contract for the Chained Estimators.
        initial_type = [('float_input', FloatTensorType([None, self.model.n_features_in_]))]

        for i in range(len(self.model.estimators_)):

            # Export the Current Chained Estimator Separately.
            est = self.model.estimators_[i]
            onx = convert_sklearn(est, initial_types=initial_type)
            with open(modelName+'_'+str(i)+".onnx", "wb") as f: f.write(onx.SerializeToString())

    def predictorML_leaveOneOut(self, dfInput,files):

        """ Leave-One-Out Cross-Validation for the Chained Multi-Output Wrapper. """

        # Keep a Copy of the Original Dataframe for Leave-One-Out Iterations.
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}

        for i in range(len(dfInput)):

            # Hold Out the Current Sample and Rebuild the Reduced Training Table.
            elem = dfInputOrig.iloc[i]
            dfInput = dfInputOrig.drop(i)
            X = dfInput[dfInput.columns[:2]]

            if self.method == 'phase':

                # Select Only the Phase Targets for the Chained Wrapper.
                cols = [x for x in dfInput.columns if 'phase' in x]
                Y = dfInput[cols]

            elif self.method == 'ampl':

                # Select Only the Amplitude Targets for the Chained Wrapper.
                cols = [x for x in dfInput.columns if 'ampl' in x]
                Y = dfInput[cols]

            else:

                # Keep the Original Full Target Surface for the Chained Wrapper.
                cols = dfInput.columns[3:]
                Y = dfInput[cols]

            # Materialize the Held-Out Feature Row for Prediction.
            X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[:2]]
            X_train, Y_train = X, Y

            # Train and Predict the Held-Out Operating Condition.
            self._train(X_train,Y_train)
            pred = self._predict(X_test)

            # Recover the Legacy Instance Name Match for the Exported Row.
            map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
            instanceName = [x for x, y in zip(files, map) if y == True]
            out[i] = {'name':instanceName[0]}

            # Append One Predicted Target Value to the Exported Row.
            for j in range(len(cols)): out[i]['prev_'+cols[j]] = pred[0][j]

        # Convert the Legacy Export Buffer Into the Expected Dataframe.
        dfOut = pd.DataFrame(out).T
        return dfOut

class MLModelMultipleOutput:

    """ Original multi-output wrapper used by the recovered training flows. """

    def __init__(self, model, name, method='', retune_grid_search_verbose=2, retune_cross_validate_verbose=1):

        # Keep the Wrapped Multi-Output Estimator Contract Intact.
        self.model = MultiOutputRegressor(model)
        self.method = method
        self.name = _resolve_model_display_name(model) + '_' + name
        self.retune_grid_search_verbose = retune_grid_search_verbose
        self.retune_cross_validate_verbose = retune_cross_validate_verbose

    def _train(self, X_train, Y_train):
        self.model.fit(X_train, Y_train)

    def _predict(self, X_test):
        return self.model.predict(X_test)

    def _select_target_columns(self, dfInput):

        """ Select the historical target surface for the current branch. """

        # Keep The Original Method-Driven Target Selection Contract Intact.
        if self.method == 'phase': return [column_name for column_name in dfInput.columns if 'phase' in column_name]
        if self.method == 'ampl':  return [column_name for column_name in dfInput.columns if 'ampl' in column_name]
        return [column_name for column_name in dfInput.columns if 'ampl' in column_name or 'phase' in column_name]

    def _build_feature_target_matrices(self, dfInput):

        """ Build the historical feature and target matrices. """

        # Keep The Original Three-Input Feature Matrix Unchanged.
        feature_dataframe = dfInput[['rpm', 'deg', 'tor']]
        target_column_list = self._select_target_columns(dfInput)
        target_dataframe = dfInput[target_column_list]
        return feature_dataframe, target_dataframe, target_column_list

    def _build_prediction_output_dataframe(self, feature_test_dataframe, target_column_list, prediction_array):

        """ Build the legacy paper-style prediction dataframe. """

        # Create the Legacy Prediction Export Buffer.
        row_payload = {}

        for row_index in range(len(feature_test_dataframe)):

            # Build the Legacy Prediction Export Row.
            operating_condition_row = feature_test_dataframe.iloc[row_index]
            exported_row = {
                'rpm': operating_condition_row['rpm'],
                'deg': operating_condition_row['deg'],
                'tor': operating_condition_row['tor'],
            }

            # Append One Predicted Target Value to the Exported Row.
            for target_index, target_column_name in enumerate(target_column_list):
                exported_row['prev_' + target_column_name] = prediction_array[row_index][target_index]
            row_payload[row_index] = exported_row

        return pd.DataFrame(row_payload).T

    def _build_summary_output_path(self, summary_prefix):

        """ Build one historical summary CSV path. """

        # Preserve The Legacy Summary Filename Contract.
        return (
            'output_prediction/'
            + summary_prefix
            + '_'
            + self.name.split('_')[-2:][0]
            + '_'
            + self.name.split('_')[-2:][1]
            + '.csv'
        )

    def _append_summary_dataframe(self, summary_output_path, summary_dataframe):

        """ Append one summary dataframe to the historical CSV path. """

        # Append To Existing Summary Files Instead Of Overwriting Them.
        if os.path.isfile(summary_output_path):
            existing_dataframe = pd.read_csv(summary_output_path, sep=';', decimal=',')
            summary_dataframe = pd.concat([existing_dataframe, summary_dataframe])

        # Write The New Summary File.
        summary_dataframe.to_csv(summary_output_path, sep=';', decimal=',', index=False)

    def _emit_progress(self, message):

        """ Emit one flush-safe progress line for long-running launcher stages. """

        print(message, flush=True)

    def _resolve_search_cv_fold_count(self, grid_search_wrapper):

        """ Resolve the effective fold count used by GridSearchCV. """

        # Match the Historical scikit-learn Default When cv Was Not Set Explicitly.
        if grid_search_wrapper.cv is None:
            return 5
        if isinstance(grid_search_wrapper.cv, int):
            return grid_search_wrapper.cv
        return 5

    def _build_cross_validate_kwargs(self, verbose_level):

        """ Build one explicit cross_validate keyword dictionary. """

        return {
            'cv': 10,
            'verbose': verbose_level,
            'scoring': [
                'neg_mean_squared_error',
                'neg_root_mean_squared_error',
                'neg_mean_absolute_error',
                'neg_mean_absolute_percentage_error',
            ],
        }

    def _evaluate_component_metrics(self, target_dataframe, target_test_dataframe, prediction_array):

        """ Evaluate per-target held-out metrics using the historical flat key shape. """

        # Preserve The Historical Flat Metric Export Surface Used By The Paper Workflow.
        component_metric_payload = {'0_method': self.get_method_acronym(self.name)}

        for target_index in range(len(self.model.estimators_)):

            # Build the Legacy Prediction Export Row.
            component = list(target_dataframe.columns[target_index:target_index + 1])[-1].split('_')[-2:]
            component_prefix = f"{component[0]}_{component[1]}"
            target_truth = target_test_dataframe[target_test_dataframe.columns[target_index]]
            target_prediction = prediction_array[:, target_index:target_index + 1]

            # Append One Predicted Target Value to the Exported Row.
            component_metric_payload[f"{component_prefix}_MSE"] = mean_squared_error(target_truth, target_prediction)
            component_metric_payload[f"{component_prefix}_RMSE"] = math.sqrt(mean_squared_error(target_truth, target_prediction))
            component_metric_payload[f"{component_prefix}_MAE"] = mean_absolute_error(target_truth, target_prediction)
            component_metric_payload[f"{component_prefix}_MAPE"] = mean_absolute_percentage_error(target_truth, target_prediction)

        return component_metric_payload

    def get_method_acronym(self, fileName):

        """ Map the estimator name to the original report acronym. """

        method = ''

        # Resolve The Acronym From The Class Name Fragment.
        for element in METHOD_ACRONYMS.keys():
            if element in fileName: method = METHOD_ACRONYMS[element]

        return method

    def getAcronimMethod(self, fileName):

        """ Backward-compatible alias for the translated acronym helper. """

        # Resolve The Acronym From The Class Name Fragment.
        return self.get_method_acronym(fileName)

    def exportModel(self, modelName, colsToPredict):

        """ Export Each Estimator in the Multi-Output Wrapper to ONNX Format. """

        # Export Each Wrapped Estimator Separately to Match the Original Surface.
        for i in range(len(self.model.estimators_)):

            # Retrieve the Current Wrapped Estimator for ONNX Export.
            est = self.model.estimators_[i]
            onnx_output_path = "model_output_dir/" + modelName + "_" + colsToPredict[i] + ".onnx"
            python_output_path = "model_output_dir/" + modelName + "_" + colsToPredict[i] + ".pkl"
            onnx_error_output_path = onnx_output_path + ".export_error.txt"

            # Always Persist the Python Estimator Artifact for Future Closeout-Time Archiving.
            with open(python_output_path, "wb") as python_output_handle:
                pickle.dump(est, python_output_handle)

            try:

                # Use the Original Family-Specific ONNX Conversion Branches.
                if isinstance(est, XGBRegressor):

                    # Recover the XGBoost Booster Before ONNX Conversion.
                    booster = est.get_booster()
                    booster.feature_names = [f"f{i}" for i in range(est.n_features_in_)]

                    # Define the XGBoost ONNX Input Contract.
                    initial_type = [('float_input', OXFloatTensorType([None, est.n_features_in_]))]
                    onx = convert_xgboost(est, initial_types=initial_type, target_opset=12)
                
                elif isinstance(est, LGBMRegressor):

                    # Define the LightGBM ONNX Input Contract.
                    initial_type = [("float_input", OXFloatTensorType([None, est.n_features_in_]))]
                    onx = convert_lightgbm(est, initial_types=initial_type, target_opset=12)

                else:

                    # Define the Generic scikit-learn ONNX Input Contract.
                    initial_type = [('float_input', FloatTensorType([None, est.n_features_in_]))]
                    onx = convert_sklearn(est, initial_types=initial_type)

                # Write Each Exported Model Into the Legacy Output Folder Contract.
                with open(onnx_output_path, "wb") as onnx_output_handle:
                    onnx_output_handle.write(onx.SerializeToString())

            except Exception as export_error:

                # Persist the ONNX Export Failure Beside the Python Artifact Instead of Crashing the Full Run.
                with open(onnx_error_output_path, "w", encoding="utf-8") as error_handle:
                    error_handle.write(traceback.format_exc())
                print(
                    f"[WARNING] ONNX Export Failed | {modelName} | {colsToPredict[i]} | "
                    f"{type(export_error).__name__}: {export_error}"
                )

    def predictorML_leaveOneOut(self, dfInput,files):

        """ Leave-One-Out Cross-Validation for the Multi-Output Wrapper. """

        # Keep a Copy of the Original Dataframe for Leave-One-Out Iterations.
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        for i in range(len(dfInput)):

            # Remove One Row and Train on the Remaining Samples.
            elem = dfInputOrig.iloc[i]
            dfInput = dfInputOrig.drop(i)
            X, Y, cols = self._build_feature_target_matrices(dfInput)

            # Materialize the Held-Out Feature Row for Prediction.
            X_test = pd.DataFrame(elem).T[['rpm','deg','tor']]
            X_train, Y_train = X, Y

            # Train on the Remaining Rows and Predict the Held-Out Operating Point.
            self._train(X_train,Y_train)
            pred = self._predict(X_test)

            # Export the Legacy Prediction Row for the Held-Out Sample.
            namesParam = {'rpm':elem['rpm'],'deg':elem['deg'],"tor":elem['tor']}
            out[i] = namesParam

            # Append One Predicted Target Value to the Exported Row.
            for j in range(len(cols)): out[i]['prev_'+cols[j]] = pred[0][j]

        # Convert the Legacy Export Buffer Into the Expected Dataframe.
        dfOut = pd.DataFrame(out).T
        return dfOut

    def predictorML(self, dfInput,testSetDimension):

        """ Original multi-output wrapper used by the recovered training flows. """

        X, Y, cols = self._build_feature_target_matrices(dfInput)

        # Keep the Original Held-Out Split Configuration.
        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=testSetDimension,random_state=0)

        # Train the Wrapped Estimator on the Historical Held-Out Split.
        self._train(X_train, Y_train)
        pred = self._predict(X_test)

        return self._build_prediction_output_dataframe(X_test, cols, pred)

    def generate_uniform_integer_values(self, n, minimum_value, maximum_value):

        """ Original multi-output wrapper used by the recovered training flows. """

        # Generate the Historical Integer Grid Used by the Search Space Builder.
        uniform_values = np.arange(minimum_value, maximum_value + 1, (maximum_value - minimum_value) // n)
        return uniform_values[:n]

    def genera_numeri_uniformi_interi(self, n, minimo, massimo):

        """ Backward-compatible alias for the translated integer-grid helper. """

        return self.generate_uniform_integer_values(n, minimo, massimo)

    def getParameterGridSearchCV(self, acronym):

        """ Original multi-output wrapper used by the recovered training flows. """

        # Build the Family-Specific Hyperparameter Grid Exactly Like the Original Helper.
        parameters = {}

        if acronym == 'DT':

            # Build the Decision-Tree Hyperparameter Grid.
            parameters['DT'] = {
                   'estimator__criterion': list(dict.fromkeys(list(['squared_error', 'absolute_error']) + [self.model.estimator.get_params()['criterion']])),
                   'estimator__max_depth': list(dict.fromkeys(list(self.generate_uniform_integer_values(5,14,21)) + [self.model.estimator.get_params()['max_depth']])),
                   'estimator__max_leaf_nodes': list(dict.fromkeys(list(self.generate_uniform_integer_values(5,23,28)) + [self.model.estimator.get_params()['max_leaf_nodes']])),
                   'estimator__min_samples_split': list(dict.fromkeys(list(self.generate_uniform_integer_values(5,2,10)) + [self.model.estimator.get_params()['min_samples_split']]))
            }

        elif acronym == 'ET':

            # Build the Extra-Tree Hyperparameter Grid.
            parameters['ET']={'estimator__criterion' : list(dict.fromkeys(list(['squared_error', 'absolute_error']) + [self.model.estimator.get_params()['criterion']])),
                   'estimator__max_depth': list(dict.fromkeys(list(self.generate_uniform_integer_values(5,14,21)) + [self.model.estimator.get_params()['max_depth']])),
                   'estimator__max_leaf_nodes': list(dict.fromkeys(list(self.generate_uniform_integer_values(5,27,35)) + [self.model.estimator.get_params()['max_leaf_nodes']])),
                   'estimator__min_samples_split': list(dict.fromkeys(list(self.generate_uniform_integer_values(5,2,10)) + [self.model.estimator.get_params()['min_samples_split']]))
            }

        elif acronym == 'ERT':

            # Build the Extra-Trees Hyperparameter Grid.
            parameters['ERT'] = {
                   'estimator__n_estimators':list(dict.fromkeys(list(self.generate_uniform_integer_values(5,20,100)) + [self.model.estimator.get_params()['n_estimators']])),
                   'estimator__criterion' : list(dict.fromkeys(list(['squared_error', 'absolute_error']) + [self.model.estimator.get_params()['criterion']])),
                   'estimator__max_depth': list(dict.fromkeys(list(self.generate_uniform_integer_values(5,14,21)) + [self.model.estimator.get_params()['max_depth']])),
                   'estimator__max_leaf_nodes':  list(dict.fromkeys(list(self.generate_uniform_integer_values(5,27,35)) + [self.model.estimator.get_params()['max_leaf_nodes']])),
                   'estimator__min_samples_split': list(dict.fromkeys(list(self.generate_uniform_integer_values(5,2,10)) + [self.model.estimator.get_params()['min_samples_split']]))
            }

        elif acronym == 'RF':

            # Build the Random-Forest Hyperparameter Grid.
            parameters['RF'] = {
                   'estimator__n_estimators': list(dict.fromkeys(list(self.generate_uniform_integer_values(5,20,100)) + [self.model.estimator.get_params()['n_estimators']])),
                   'estimator__criterion': list(dict.fromkeys(list(['squared_error', 'absolute_error']) + [self.model.estimator.get_params()['criterion']])),
                   'estimator__max_features': list(dict.fromkeys(list(["log2","sqrt"]) + [self.model.estimator.get_params()['max_features']])),
                   'estimator__max_depth': list(dict.fromkeys(list(self.generate_uniform_integer_values(5,14,21)) + [self.model.estimator.get_params()['max_depth']])),
                   'estimator__min_samples_split': list(dict.fromkeys(list(self.generate_uniform_integer_values(5,2,10)) + [self.model.estimator.get_params()['min_samples_split']])),
            }

        elif acronym == 'GBM':

            # Build the Gradient-Boosting Hyperparameter Grid.
            parameters['GBM'] = {
                'estimator__n_estimators': list(dict.fromkeys(list(self.generate_uniform_integer_values(5,20,100)) + [self.model.estimator.get_params()['n_estimators']])),
                'estimator__criterion': list(dict.fromkeys(list(['squared_error', 'absolute_error']) + [self.model.estimator.get_params()['criterion']])),
                'estimator__max_features': list(dict.fromkeys(list(["log2", "sqrt"]) + [self.model.estimator.get_params()['max_features']])),
                'estimator__max_depth': list(dict.fromkeys(list(self.generate_uniform_integer_values(5,14,21)) + [self.model.estimator.get_params()['max_depth']])),
                'estimator__min_samples_split': list(dict.fromkeys(list(self.generate_uniform_integer_values(5,2,10)) + [self.model.estimator.get_params()['min_samples_split']])),
                'estimator__learning_rate':list(dict.fromkeys(list([0.0001, 0.001, 0.01, 0.1, 1.0]) + [self.model.estimator.get_params()['learning_rate']])),
            }

        elif acronym == 'XGBM':

            # Build the XGBoost Hyperparameter Grid.
            parameters['XGBM'] = {
                'estimator__learning_rate': list(dict.fromkeys(list([0.01,0.2,0.5]) + [self.model.estimator.get_params()['learning_rate']])),
                'estimator__n_estimators': list(dict.fromkeys(list(self.generate_uniform_integer_values(5,20,100)) + [self.model.estimator.get_params()['n_estimators']])),
                'estimator__max_depth': list(dict.fromkeys(list(self.generate_uniform_integer_values(5,14,21)) + [self.model.estimator.get_params()['max_depth']])),
                'estimator__colsample_bytree': list(dict.fromkeys(list([0.3,0.5]) + [self.model.estimator.get_params()['colsample_bytree']])),
            }

        elif acronym ==  'HGBM':

            # Build the Histogram-Gradient-Boosting Hyperparameter Grid.
            parameters['HGBM'] = {
                'estimator__max_iter': list(dict.fromkeys(list([10,100,1000]) + [self.model.estimator.get_params()['max_iter']])),
                'estimator__max_depth': list(dict.fromkeys(list(self.generate_uniform_integer_values(5,14,21)) + [self.model.estimator.get_params()['max_depth']])),
                'estimator__learning_rate': list(dict.fromkeys(list([x/ 100 for x in self.generate_uniform_integer_values(5,1,100)]) + [self.model.estimator.get_params()['learning_rate']])),
                'estimator__max_leaf_nodes':list(dict.fromkeys(list(self.generate_uniform_integer_values(5,27,35)) + [self.model.estimator.get_params()['max_leaf_nodes']])),
            }

        elif acronym == 'LGBM':

            # Build the LightGBM Hyperparameter Grid.
            parameters['LGBM'] = {
                'estimator__learning_rate': list(dict.fromkeys(list([x / 100 for x in self.generate_uniform_integer_values(5, 1, 100)]) + [self.model.estimator.get_params()['learning_rate']])),
                 'estimator__max_depth': list(dict.fromkeys(list(self.generate_uniform_integer_values(5, 14, 21)) + [self.model.estimator.get_params()['max_depth']])),
                 'estimator__num_leaves': list(dict.fromkeys(list(self.generate_uniform_integer_values(5,10,100)) + [self.model.estimator.get_params()['num_leaves']])),
                 'estimator__subsample': list(dict.fromkeys(list([0.1,0.3,0.5,0.8]) + [self.model.estimator.get_params()['subsample']])),
            }

        elif acronym == 'MLP':

            # Build the MLP Hyperparameter Grid.
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

        elif acronym == 'ELM':

            # Build the ELM Hyperparameter Grid.
            parameters['ELM'] = {
                    'estimator__n_neurons': list(dict.fromkeys(list([100, 250, 500]) + ([self.model.estimator.get_params()['n_neurons']] if self.model.estimator.get_params()['n_neurons'] is not None else []))),
                    'estimator__alpha': list(dict.fromkeys(list([1e-7, 1e-5, 1e-3]) + [self.model.estimator.get_params()['alpha']])),
                    'estimator__ufunc': list(dict.fromkeys(list(['tanh']) + [self.model.estimator.get_params()['ufunc']]))
            }

        elif acronym == 'SVM':

            # Preserve The Paper-Faithful RBF Branch And Replace The Historical Linear Branch With One Pragmatic LinearSVR Fallback.
            rbf_estimator = copy.deepcopy(self.model.estimator)
            rbf_estimator.set_params(kernel='rbf')
            linear_fallback_estimator = Pipeline(
                steps=[
                    ('scaler', StandardScaler()),
                    (
                        'model',
                        LinearSVR(
                            random_state=0,
                        ),
                    ),
                ]
            )

            # Build The SVM Hyperparameter Grid With the Original RBF and Linear Branches.
            parameters['SVM'] = [
                {
                    'estimator': [rbf_estimator],
                    'estimator__C':  list(dict.fromkeys(list([1,2,3,5,6,7]) + [self.model.estimator.get_params()['C']])),
                    'estimator__epsilon': list(dict.fromkeys(list([0.0001,0.00001,0.000001,0.0000001]))),
                    'estimator__gamma': list(dict.fromkeys(list([0.0000011]))),
                },
                {
                    'estimator': [linear_fallback_estimator],
                    'estimator__model__C':  list(dict.fromkeys(list([1,2,3,5,6,7]) + [self.model.estimator.get_params()['C']])),
                    'estimator__model__epsilon': list(dict.fromkeys(list([0.0001,0.00001,0.000001,0.0000001]))),
                    'estimator__model__tol': [1e-4],
                    'estimator__model__max_iter': [5000],
                },
            ]

        return parameters[acronym]

    def _serialize_best_parameter_payload(self):

        """ Serialize the best-parameter payload into one literal reloadable shape. """

        # Extract the Best Parameter Payload.
        best_parameter_payload = self.model.best_params_

        # Serialize the Best Parameter Payload.
        if self.get_method_acronym(self.name) != 'SVM':
            return best_parameter_payload

        # Preserve The Paper-Faithful RBF Branch And Replace The Historical Linear Branch With One Pragmatic LinearSVR Fallback.
        selected_estimator = best_parameter_payload.get('estimator')
        if isinstance(selected_estimator, Pipeline):
            return {
                SVR_VARIANT_KEY: SVR_VARIANT_LINEAR_FALLBACK,
                SVR_VARIANT_PARAMETERS_KEY: {
                    'C': best_parameter_payload['estimator__model__C'],
                    'epsilon': best_parameter_payload['estimator__model__epsilon'],
                    'tol': best_parameter_payload['estimator__model__tol'],
                    'max_iter': best_parameter_payload['estimator__model__max_iter'],
                },
            }

        return {
            SVR_VARIANT_KEY: SVR_VARIANT_RBF,
            SVR_VARIANT_PARAMETERS_KEY: {
                'C': best_parameter_payload['estimator__C'],
                'epsilon': best_parameter_payload['estimator__epsilon'],
                'gamma': best_parameter_payload['estimator__gamma'],
                'kernel': 'rbf',
            },
        }

    def getAcronimMethod(self, fileName):

        """ Map the estimator name to the original report acronym. """

        # Resolve The Acronym From The Class Name Fragment.
        return self.get_method_acronym(fileName)

    def predictorMLEvalutationOnTrain(self, dfInput, testSetDimension):

        """ Original multi-output wrapper used by the recovered training flows. """

        X, Y, cols = self._build_feature_target_matrices(dfInput)

        # Materialize the Historical Held-Out Split Used by the Paper Evaluation Path.
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=testSetDimension, random_state=0)
        print("MODEL:", self.name)
        print("TRAINING START:", datetime.datetime.now())

        # Train the Wrapped Estimator Before Scoring the Held-Out Split.
        self._train(X_train, Y_train)
        print("TRAINING END:", datetime.datetime.now())

        # Predict the Held-Out Split With the Trained Estimator.
        pred = self._predict(X_test)

        crossValOut = self._evaluate_component_metrics(Y, Y_test, pred)

        # Persist the summary exactly where the original workflow expects it.
        outputFileSummary = self._build_summary_output_path('summaryCrossValidation+')
        finalOut = pd.DataFrame(crossValOut, index=[0])
        self._append_summary_dataframe(outputFileSummary, finalOut)

        return self._build_prediction_output_dataframe(X_test, cols, pred)

    def predictorMLCrossValidationWithHyperparameter(self, dfInput,testSetDimension):

        """ Original multi-output wrapper used by the recovered training flows. """

        X, Y, cols = self._build_feature_target_matrices(dfInput)
        target_count = len(cols)

        # Materialize the Historical Held-Out Split Used by the Search Branch.
        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=testSetDimension,random_state=0)

        # Wrap the original multi-output estimator in the historical grid-search path.
        parameter_grid = self.getParameterGridSearchCV(self.get_method_acronym(self.name))
        self.model = GridSearchCV(
            self.model,
            parameter_grid,
            n_jobs=-1,
            verbose=self.retune_grid_search_verbose,
        )
        search_cv_fold_count = self._resolve_search_cv_fold_count(self.model)
        candidate_count = len(ParameterGrid(parameter_grid))

        # Print the Historical Training Banner Before the Grid Search.
        self._emit_progress("MODEL: " + self.name)
        self._emit_progress("TRAINING START: " + str(datetime.datetime.now()))
        self._emit_progress(
            f"[PROGRESS] Retune | Split Ready | Samples {len(X)} | Train {len(X_train)} | "
            f"Test {len(X_test)} | Targets {target_count}"
        )
        self._emit_progress(
            f"[PROGRESS] Retune | GridSearchCV Setup | Candidates {candidate_count} | "
            f"SearchCV {search_cv_fold_count} | TargetCount {target_count} | "
            f"Wrapper MultiOutputRegressor"
        )
        self._emit_progress(
            f"[PROGRESS] Retune | GridSearchCV Start | Verbose {self.retune_grid_search_verbose}"
        )
        print(self.model.param_grid, flush=True)

        # Train the Historical Grid-Search Wrapper on the Training Split.
        self._train(X_train, Y_train)
        self._emit_progress("[PROGRESS] Retune | GridSearchCV Done")

        # Run the Historical Cross-Validation Metric Sweep on the Grid-Search Wrapper.
        self._emit_progress(
            f"[PROGRESS] Retune | Wrapper CrossValidate Start | cv 10 | Verbose {self.retune_cross_validate_verbose}"
        )
        scores = cross_validate(
            self.model,
            X,
            Y,
            **self._build_cross_validate_kwargs(self.retune_cross_validate_verbose),
        )
        self._emit_progress("[PROGRESS] Retune | Wrapper CrossValidate Done")

        # Prepare the Flat Summary Container Used by the Historical CSV Export.
        errorKeys = list(ERROR_ACRONYMS.keys())
        crossValOut = {}
        crossValOut['0_method'] = self.get_method_acronym(self.name)

        # Store the Global Cross-Validation Means for the Best-Search Wrapper.
        for el in errorKeys: crossValOut[ERROR_ACRONYMS[el]] = abs(scores[el].mean())

        # Iterate Over the Best Wrapped Estimators Target by Target.
        for i in range(len(self.model.best_estimator_.estimators_)):
            component = list(Y.columns[i:i + 1])[-1].split('_')[-2:]
            self._emit_progress(
                f"[PROGRESS] Retune | Target CrossValidate Start | {i + 1}/{target_count} | "
                f"{component[0]}_{component[1]} | cv 10"
            )

            # Re-Score the Current Best Wrapped Estimator Target by Target.
            scores = cross_validate(
                self.model.best_estimator_.estimators_[i],
                X,
                Y[Y.columns[i:i + 1]],
                **self._build_cross_validate_kwargs(self.retune_cross_validate_verbose),
            )
            self._emit_progress(
                f"[PROGRESS] Retune | Target CrossValidate Done | {i + 1}/{target_count} | "
                f"{component[0]}_{component[1]}"
            )

            # Reuse the Historical Error-Key Ordering for the Current Target.
            errorKeys = list(ERROR_ACRONYMS.keys())

            for el in errorKeys:

                # Recover the Harmonic Component Suffix Used by the Summary CSV.
                crossValOut[str(component[0])+'_'+str(component[1])+'_'+ERROR_ACRONYMS[el]] = abs(scores[el].mean())

        # Print the Historical Training Footer and Best Parameters.
        self._emit_progress("TRAINING END: " + str(datetime.datetime.now()))
        self._emit_progress("[PROGRESS] Retune | Best Parameters")
        serialized_best_parameter_payload = self._serialize_best_parameter_payload()
        print(serialized_best_parameter_payload, flush=True)
        pred = self._predict(X_test)

        # Persist the cross-validation summary exactly where the original workflow expects it.
        self._emit_progress("[PROGRESS] Retune | Write CrossValidation Summary")
        outputFileSummary = self._build_summary_output_path('summaryCrossValidation+')
        finalOut = pd.DataFrame(crossValOut,index=[0])
        self._append_summary_dataframe(outputFileSummary, finalOut)

        # Persist the best-parameter summary exactly where the original workflow expects it.
        self._emit_progress("[PROGRESS] Retune | Write BestParameter Summary")
        outputFileParameter = self._build_summary_output_path('summaryBestParameter+')
        paramOut = {'0_method':self.get_method_acronym(self.name), 'best_parameters':str(serialized_best_parameter_payload)}
        paramOut = pd.DataFrame(paramOut,index=[0])
        self._append_summary_dataframe(outputFileParameter, paramOut)
        self._emit_progress("[PROGRESS] Retune | Prediction Dataframe Build")

        return self._build_prediction_output_dataframe(X_test, cols, pred)

    def predictorMLCrossValidation(self, dfInput,testSetDimension):

        """ Original multi-output wrapper used by the recovered training flows. """

        X, Y, cols = self._build_feature_target_matrices(dfInput)

        # Materialize the Historical Held-Out Split Used by the Cross-Validation Branch.
        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=testSetDimension,random_state=0)

        # Train the Wrapped Estimator Before Running Cross-Validation Reporting.
        self._train(X_train, Y_train)

        # Run the Historical Cross-Validation Metric Sweep.
        scores = cross_validate(self.model, X, Y, cv=10,scoring=['neg_mean_squared_error',
                                                                  'neg_root_mean_squared_error',
                                                                  'neg_mean_absolute_error',
                                                                  'neg_mean_absolute_percentage_error'])

        # Prepare the Flat Summary Container Used by the Historical CSV Export.
        errorKeys = list(ERROR_ACRONYMS.keys())#[x for x in list(scores.keys()) if 'test' in x]
        crossValOut = {}
        crossValOut['0_method'] = self.get_method_acronym(self.name)

        # Store the Global Cross-Validation Means for the Wrapped Estimator.
        for el in errorKeys: crossValOut[ERROR_ACRONYMS[el]] = abs(scores[el].mean())

        for i in range(len(self.model.estimators_)):

            # Re-Score the Current Wrapped Estimator Target by Target.
            scores = cross_validate(self.model.estimators_[i], X, Y[Y.columns[i:i + 1]], cv=10,
                                    scoring=['neg_mean_squared_error',
                                             'neg_root_mean_squared_error',
                                             'neg_mean_absolute_error',
                                             'neg_mean_absolute_percentage_error'])

            # Reuse the Historical Error-Key Ordering for the Current Target.
            errorKeys = list(ERROR_ACRONYMS.keys())

            for el in errorKeys:

                # Recover the Harmonic Component Suffix Used by the Summary CSV.
                component = list(Y.columns[i:i + 1])[-1].split('_')[-2:]
                crossValOut[str(component[0])+'_'+str(component[1])+'_'+ERROR_ACRONYMS[el]] = abs(scores[el].mean())

        # Predict the Held-Out Split With the Trained Estimator.
        pred = self._predict(X_test)

        # Persist the summary exactly where the original workflow expects it.
        outputFileSummary = self._build_summary_output_path('summaryCrossValidation+')
        finalOut = pd.DataFrame(crossValOut,index=[0])
        self._append_summary_dataframe(outputFileSummary, finalOut)

        return self._build_prediction_output_dataframe(X_test, cols, pred)

    def predictorML_allForExport(self, dfInput, testSetDimension=None):

        """ Original multi-output wrapper used by the recovered training flows. """

        X, Y, cols = self._build_feature_target_matrices(dfInput)

        # Train on the Entire Original Dataset Before Exporting the Bank.
        X_train, Y_train = X, Y

        # Print the Historical Training Banner Before the Full-Dataset Export Fit.
        print("MODEL:", self.name)
        print("TRAINING START:", datetime.datetime.now())
        self._train(X_train, Y_train)
        print("TRAINING END:", datetime.datetime.now())

        return pd.DataFrame()

    def predictorML_TestForExport(self, dfTest):

        """ Run one already-trained export bank on one explicit test table. """

        # Extract the Input Columns From the Explicit Export Test Table.
        xCols = [x for x in dfTest.columns if 'input' in x]
        x_test = dfTest[xCols]
        x_test.columns = ['tor','rpm','deg']
        cl_ok = ['rpm','deg','tor']
        x_test = x_test[cl_ok]

        # Initialize the Concatenated Prediction Table for the Explicit Export Path.
        dfOut = pd.DataFrame()

        for md in self.model.estimators_:

            # Predict the Current Wrapped Output Column on the Export Test Table.
            pred_col = md.predict(x_test)
            dfOut = pd.concat([dfOut,pd.DataFrame(pred_col)],axis=1)

        # Persist the Explicit Export Prediction Table Using the Historical Filename Contract.
        pd.concat([pd.DataFrame(dfOut),x_test],axis=1).to_csv('outputCOMB_SVR_GBR_T27_'+str(datetime.datetime.now().date())+'.csv',sep=';',decimal=',')
        return dfOut

    def predictorMLVariableTrain(self, dfInput, testSetDimension, trainSetDimansion=None):

        """ Original multi-output wrapper used by the recovered training flows. """

        # Initialize the Legacy Prediction Export Buffer.
        out = {}

        # Build the Original Three-Input Feature Matrix.
        X = dfInput[['rpm', 'deg', 'tor']]

        if self.method == 'phase':

            # Select Only the Phase Targets for the Variable-Train Branch.
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]

        elif self.method == 'ampl':

            # Select Only the Amplitude Targets for the Variable-Train Branch.
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]

        else:

            # Keep the Original Full Target Surface for the Variable-Train Branch.
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]
            Y = dfInput[cols]

        # Default the Requested Train Fraction to the Complement of the Test Split.
        if trainSetDimansion == None: trainSetDimansion = 1 - testSetDimension

        # Materialize the Historical Held-Out Split Used by the Variable-Train Branch.
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=testSetDimension, random_state=0)

        # Reset the Indices Before Applying the Historical Random Subsampling Step.
        X_train.reset_index(inplace=True,drop=True)
        X_test.reset_index(inplace=True,drop=True)
        Y_train.reset_index(inplace=True,drop=True)
        Y_test.reset_index(inplace=True,drop=True)

        # Seed the Python RNG Exactly Like the Original Workflow.
        random.seed(0)

        # Drop Random Training Rows Until the Requested Effective Train Size Is Reached.
        itemToDrop = random.sample(X_train.index.to_list(),len(X_train) - round(len(X)*trainSetDimansion))

        # Remove the Sampled Rows From Both Features and Targets.
        X_train = X_train.drop(itemToDrop)
        Y_train = Y_train.drop(itemToDrop)

        # Train the Wrapped Estimator on the Reduced Training Split.
        self._train(X_train,Y_train)

        # Predict the Held-Out Split With the Reduced-Train Estimator.
        pred = self._predict(X_test.reset_index(drop=True))

        # Export the held-out prediction rows in the paper-era table shape.
        for i in range(len(X_test)):

            # Read the Held-Out Operating Condition for This Exported Row.
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            out[i] = namesParam

            # Append One Predicted Target Value to the Exported Row.
            for j in range(len(cols)): out[i]['prev_' + cols[j]] = pred[i][j]

        # Convert the Legacy Export Buffer Into the Expected Dataframe.
        dfOut = pd.DataFrame(out).T
        return dfOut

class MLModelMultiOutputCombined:

    """ Original mixed multi-output wrapper retained for completeness. """

    def __init__(self, modelsList, name, method=''):

        # Keep the Historical Mixed-Wrapper Construction Intact.
        self.model = MultiOutputRegressor(modelsList)
        self.method = method
        self.name = name

    def _train(self, X_train, Y_train):
        self.model.fit(X_train, Y_train)

    def _predict(self, X_test):
        return self.model.predict(X_test)

    def exportModel(self,modelName,colsToPredict):

        """ Export The Single Model From The Wrapped Multi-Output Estimator. """

        # Build the ONNX Input Contract for the Mixed Wrapper.
        initial_type = [('float_input', FloatTensorType([None, self.model.n_features_in_]))]

        for i in range(len(self.model.estimators_)):

            # Retrieve the Current Wrapped Estimator for ONNX Export.
            est = self.model.estimators_[i]
            onx = convert_sklearn(est, initial_types=initial_type)

            # Persist the Exported Estimator Using the Historical Naming Contract.
            with open(modelName+'_'+colsToPredict[i]+".onnx", "wb") as f: f.write(onx.SerializeToString())

    def predictorML_leaveOneOut(self, dfInput,files):

        """ Original multi-output wrapper used by the recovered training flows. """

        # Keep a Copy of the Original Dataframe for Leave-One-Out Iterations.
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}

        for i in range(len(dfInput)):

            # Hold Out the Current Sample and Rebuild the Reduced Training Table.
            elem = dfInputOrig.iloc[i]
            dfInput = dfInputOrig.drop(i)
            X = dfInput[['rpm','deg','tor']]

            if self.method == 'phase':

                # Select Only the Phase Targets for the Mixed Wrapper.
                cols = [x for x in dfInput.columns if 'phase' in x]
                Y = dfInput[cols]

            elif self.method == 'ampl':

                # Select Only the Amplitude Targets for the Mixed Wrapper.
                cols = [x for x in dfInput.columns if 'ampl' in x]
                Y = dfInput[cols]

            else:

                # Keep the Original Full Target Surface for the Mixed Wrapper.
                cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]#dfInput.columns[3:]
                Y = dfInput[cols]

            # Materialize the Held-Out Feature Row for Prediction.
            X_test = pd.DataFrame(elem).T[['rpm','deg','tor']]
            X_train, Y_train = X, Y

            # Train on the Reduced Table and Predict the Held-Out Row.
            self._train(X_train,Y_train)
            pred = self._predict(X_test)

            # Export the Held-Out Operating Condition in the Legacy Table Shape.
            namesParam = {'rpm':elem['rpm'],'deg':elem['deg'],"tor":elem['tor']}
            out[i] = namesParam

            # Append One Predicted Target Value to the Exported Row.
            for j in range(len(cols)): out[i]['prev_' + cols[j]] = pred[0][j]

        # Convert the Legacy Export Buffer Into the Expected Dataframe.
        dfOut = pd.DataFrame(out).T
        return dfOut

    def predictorML(self, dfInput,testSetDimension):

        """ Original multi-output wrapper used by the recovered training flows. """

        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]

        if self.method == 'phase':

            # Select Only the Phase Targets for the Mixed Wrapper.
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]

        elif self.method == 'ampl':

            # Select Only the Amplitude Targets for the Mixed Wrapper.
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]

        else:

            # Keep the Original Full Target Surface for the Mixed Wrapper.
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]
            Y = dfInput[cols]

        # Materialize the Historical Held-Out Split Used by the Mixed Wrapper.
        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=testSetDimension,random_state=0)
        self._train(X_train, Y_train)

        # Predict the Held-Out Split With the Trained Mixed Wrapper.
        pred = self._predict(X_test)

        for i in range(len(X_test)):

            # Read the Held-Out Operating Condition for This Exported Row.
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            out[i] = namesParam

            # Append One Predicted Target Value to the Exported Row.
            for j in range(len(cols)): out[i]['prev_' + cols[j]] = pred[i][j]

        # Convert the Legacy Export Buffer Into the Expected Dataframe.
        dfOut = pd.DataFrame(out).T
        return dfOut

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

        """ Original multi-output wrapper used by the recovered training flows. """

        # Keep a Copy of the Original Dataframe for Cross-Validation Bookkeeping.
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]

        if self.method == 'phase':

            # Select Only the Phase Targets for the Mixed Wrapper.
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]

        elif self.method == 'ampl':

            # Select Only the Amplitude Targets for the Mixed Wrapper.
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]

        else:

            # Keep the Original Full Target Surface for the Mixed Wrapper.
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]
            Y = dfInput[cols]

        # Materialize the Historical Held-Out Split Used by the Mixed Wrapper.
        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=testSetDimension,random_state=0)
        self._train(X_train, Y_train)

        # Define the Historical Error-Acronym Mapping Used by the Summary CSV.
        errorsAcronims = {
            'test_neg_mean_squared_error' : 'MSE',
            'test_neg_root_mean_squared_error': 'RMSE',
            'test_neg_mean_absolute_error':'MAE',
            'test_neg_mean_absolute_percentage_error':'MAPE'
        }

        # Run the Historical Cross-Validation Metric Sweep.
        scores = cross_validate(self.model, X, Y, cv=10,scoring=['neg_mean_squared_error',
                                                                  'neg_root_mean_squared_error',
                                                                  'neg_mean_absolute_error',
                                                                  'neg_mean_absolute_percentage_error'])

        # Prepare the Flat Summary Container Used by the Historical CSV Export.
        errorKeys = list(errorsAcronims.keys())
        crossValOut = {}
        crossValOut['0_method'] = self.getAcronimMethod(self.name)

        # Store the Global Cross-Validation Means for the Mixed Wrapper.
        for el in errorKeys: crossValOut[errorsAcronims[el]] = abs(scores[el].mean())

        for i in range(len(self.model.estimators_)):

            # Re-Score the Current Wrapped Estimator Target by Target.
            scores = cross_validate(self.model.estimators_[i], X, Y[Y.columns[i:i + 1]], cv=10,
                                    scoring=['neg_mean_squared_error',
                                             'neg_root_mean_squared_error',
                                             'neg_mean_absolute_error',
                                             'neg_mean_absolute_percentage_error'])

            # Reuse the Historical Error-Key Ordering for the Current Target.
            errorKeys = list(errorsAcronims.keys())

            for el in errorKeys:

                # Recover the Harmonic Component Suffix Used by the Summary CSV.
                component = list(Y.columns[i:i + 1])[-1].split('_')[-2:]
                crossValOut[str(component[0])+'_'+str(component[1])+'_'+errorsAcronims[el]] = abs(scores[el].mean())

        # Predict the Held-Out Split With the Trained Mixed Wrapper.
        pred = self._predict(X_test)

        # Persist the summary exactly where the original workflow expects it.
        outputFileSummary = 'output_prediction/summaryCrossValidation+_' + self.name.split('_')[-2:][0] + '_' + self.name.split('_')[-2:][1] + '.csv'
        finalOut = pd.DataFrame(crossValOut,index=[0])

        if os.path.isfile(outputFileSummary):

            # Append to the Existing Summary File Instead of Overwriting It.
            existing_df = pd.read_csv(outputFileSummary, sep=';', decimal=',')
            finalOut = pd.concat([existing_df,finalOut])

        # Write the Summary Back to the Historical Output Path.
        finalOut.to_csv(outputFileSummary, sep=';', decimal=',', index=False)

        for i in range(len(X_test)):

            # Read the Held-Out Operating Condition for This Exported Row.
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            out[i] = namesParam

            # Append One Predicted Target Value to the Exported Row.
            for j in range(len(cols)): out[i]['prev_' + cols[j]] = pred[i][j]

        # Convert the Legacy Export Buffer Into the Expected Dataframe.
        dfOut = pd.DataFrame(out).T
        return dfOut

    def predictorML_allForExport(self, dfInput, files):

        """ Original multi-output wrapper used by the recovered training flows. """

        # Keep a Copy of the Original Dataframe for Export-Only Bookkeeping.
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]

        if self.method == 'phase':

            # Select Only the Phase Targets for the Export Branch.
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]

        elif self.method == 'ampl':

            # Select Only the Amplitude Targets for the Export Branch.
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]

        else:

            # Keep the Original Full Target Surface for the Export Branch.
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]
            Y = dfInput[cols]

        # Train on the Entire Original Dataset Before Exporting the Bank.
        X_train, Y_train = X, Y
        self._train(X_train, Y_train)

        return pd.DataFrame()

    def predictorMLVariableTrain(self, dfInput, testSetDimension, trainSetDimansion=None):

        """ Original multi-output wrapper used by the recovered training flows. """

        # Keep a Copy of the Original Dataframe for Variable-Train Bookkeeping.
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]

        if self.method == 'phase':

            # Select Only the Phase Targets for the Variable-Train Branch.
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]

        elif self.method == 'ampl':

            # Select Only the Amplitude Targets for the Variable-Train Branch.
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]

        else:

            # Keep the Original Full Target Surface for the Variable-Train Branch.
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]
            Y = dfInput[cols]

        # Default the Requested Train Fraction to the Complement of the Test Split.
        if trainSetDimansion == None: trainSetDimansion = 1 - testSetDimension

        # Materialize the Historical Held-Out Split Used by the Variable-Train Branch.
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=testSetDimension, random_state=0)

        # Reset the Indices Before Applying the Historical Random Subsampling Step.
        X_train.reset_index(inplace=True,drop=True)
        X_test.reset_index(inplace=True,drop=True)
        Y_train.reset_index(inplace=True,drop=True)
        Y_test.reset_index(inplace=True,drop=True)

        # Seed the Python RNG Exactly Like the Original Workflow.
        random.seed(0)

        # Drop Random Training Rows Until the Requested Effective Train Size Is Reached.
        itemToDrop = random.sample(X_train.index.to_list(),len(X_train) - round(len(X)*trainSetDimansion))

        # Remove the Sampled Rows From Both Features and Targets.
        X_train = X_train.drop(itemToDrop)
        Y_train = Y_train.drop(itemToDrop)

        # Train the Mixed Wrapper on the Reduced Training Split.
        self._train(X_train,Y_train)

        # Predict the Held-Out Split With the Reduced-Train Estimator.
        pred = self._predict(X_test.reset_index(drop=True))

        for i in range(len(X_test)):

            # Read the Held-Out Operating Condition for This Exported Row.
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            out[i] = namesParam

            # Append One Predicted Target Value to the Exported Row.
            for j in range(len(cols)): out[i]['prev_' + cols[j]] = pred[i][j]

        # Convert the Legacy Export Buffer Into the Expected Dataframe.
        dfOut = pd.DataFrame(out).T
        return dfOut

class MLPipeline:

    """ Original pipeline-based wrapper retained for completeness. """

    def __init__(self, model, name, columnToPredict):

        # Keep the Historical Pipeline Wrapper Contract Intact.
        self.columnToPredict = columnToPredict
        self.model = Pipeline(steps=[('preprocess',StandardScaler()),('model',model)])
        self.name = name

    def _train(self, X_train, Y_train):
        self.model.fit(X_train, Y_train)

    def _predict(self, X_test):
        return self.model.predict(X_test)

    def gridSearch(self,params):

        # Replace the Pipeline With the Historical Grid-Search Wrapper.
        self.model = GridSearchCV(self.model, params, n_jobs=-1)

    def exportModel(self,modelName):

        # Build the ONNX Input Contract for the Pipeline Wrapper.
        initial_type = [('float_input', FloatTensorType([None, self.model.n_features_in_]))]
        onx = convert_sklearn(self.model, initial_types=initial_type, options={type(self.model): {'zipmap':False}}, target_opset=12)

        # Persist the Exported Pipeline Model Using the Historical Naming Contract.
        with open(modelName+".onnx", "wb") as f: f.write(onx.SerializeToString())
        return

    def predictorML_leaveOneOut(self, dfInput,files):

        """ Original multi-output wrapper used by the recovered training flows. """

        # Keep a Copy of the Original Dataframe for Leave-One-Out Iterations.
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}

        for i in range(len(dfInput)):

            # Hold Out the Current Sample and Rebuild the Reduced Training Table.
            elem = dfInputOrig.iloc[i]
            dfInput = dfInputOrig.drop(i)
            X = dfInput[dfInput.columns[:2]]
            Y = dfInput[self.columnToPredict]
            X_test = pd.DataFrame(elem).T[pd.DataFrame(elem).T.columns[:2]]
            X_train, Y_train = X, Y

            # Train on the remaining rows and predict the held-out operating point.
            self._train(X_train,Y_train)
            pred = self._predict(X_test)

            # Recover the Legacy Instance Name Match for the Exported Row.
            map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
            instanceName = [x for x, y in zip(files, map) if y == True]
            out[i] = {'name':instanceName[0],'prev_'+self.columnToPredict:pred[0]}

        # Convert the Legacy Export Buffer Into the Expected Dataframe.
        dfOut = pd.DataFrame(out).T
        return dfOut

    def predictorML_singleModel_leaveOneOut(self, dfInput,files):

        """ Original multi-output wrapper used by the recovered training flows. """

        # Keep a Copy of the Original Dataframe for Leave-One-Out Iterations.
        dfInputOrig = copy.deepcopy(dfInput)
        out = {}

        for i in range(len(dfInput)):

            # Hold Out the Current Sample and Rebuild the Reduced Training Table.
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

            # Recover the Legacy Instance Name Match for the Exported Row.
            map = [x.startswith(str(elem['rpm'])+'rpm'+str(elem['deg'])+'deg') for x in files]
            instanceName = [x for x, y in zip(files, map) if y == True]
            out[i] = {'name':instanceName[0],'prev_'+self.columnToPredict:pred[0]}

        # Convert the Legacy Export Buffer Into the Expected Dataframe.
        dfOut = pd.DataFrame(out).T
        return dfOut

class MinimumDistanceRegressor:

    """ Original minimum-distance baseline retained for completeness. """

    def _calculateDistanceMatrix(self,X_train,X_test):

        # Compute the Full Distance Matrix Between Train and Test Samples.
        return distance_matrix(X_train,X_test)

    def _getMinimum(self,distMatrix):

        # Collect the index of the nearest training sample for each test sample.
        risultati = []

        # Process the distance matrix one test-sample column at a time.
        for colonna in range(len(distMatrix[0])):

            # Initialize the Running Minimum for the Current Test Column.
            minimo_colonna = float('inf')
            indice_minimo = None

            # Scan every training sample distance for the current test sample.
            for riga in range(len(distMatrix)):

                # Read the Current Train-to-Test Distance Entry.
                valore_attuale = distMatrix[riga][colonna]

                # Keep the row index that minimizes the current column distance.
                if valore_attuale < minimo_colonna: minimo_colonna, indice_minimo = valore_attuale, riga

            # Store the Index of the Nearest Training Sample for This Test Column.
            risultati.append(indice_minimo)

        return risultati

    def _predict(self,X_train,X_test,Y_train):

        """ Predict the output for each test sample as the output of the nearest training sample. """

        # Compute the Distance Matrix and Resolve the Nearest Indices.
        distMatrix = self._calculateDistanceMatrix(X_train,X_test)
        mins = self._getMinimum(distMatrix)
        pred = []

        # Gather the Target Rows Associated With the Nearest Training Samples.
        for i in mins: pred.append(Y_train.iloc[i])
        return pred

    def __init__(self, name, method=''):

        # Keep the Historical Minimum-Distance Wrapper Contract Intact.
        self.name = name
        self.method = method

    def predictorML(self, dfInput, testSetDimension):

        """ Original multi-output wrapper used by the recovered training flows. """

        # Initialize the Legacy Prediction Export Buffer.
        out = {}
        X = dfInput[['rpm', 'deg', 'tor']]

        if self.method == 'phase':

            # Select Only the Phase Targets for the Minimum-Distance Branch.
            cols = [x for x in dfInput.columns if 'phase' in x]
            Y = dfInput[cols]

        elif self.method == 'ampl':

            # Select Only the Amplitude Targets for the Minimum-Distance Branch.
            cols = [x for x in dfInput.columns if 'ampl' in x]
            Y = dfInput[cols]

        else:

            # Keep the Original Full Target Surface for the Minimum-Distance Branch.
            cols = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]
            Y = dfInput[cols]

        # Materialize the Historical Held-Out Split Used by the Minimum-Distance Branch.
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=testSetDimension, random_state=0)
        pred = self._predict(X_train.reset_index(drop=True),X_test.reset_index(drop=True),Y_train.reset_index(drop=True))

        for i in range(len(X_test)):

            # Read the Held-Out Operating Condition for This Exported Row.
            elem = X_test.iloc[i]
            namesParam = {'rpm': elem['rpm'], 'deg': elem['deg'], "tor": elem['tor']}
            out[i] = namesParam

            # Append One Predicted Target Value to the Exported Row.
            for j in range(len(cols)): out[i]['prev_' + cols[j]] = pred[i][j]

        # Convert the Legacy Export Buffer Into the Expected Dataframe.
        dfOut = pd.DataFrame(out).T
        return dfOut
