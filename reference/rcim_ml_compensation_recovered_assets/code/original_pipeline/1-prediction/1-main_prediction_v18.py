import os
import pandas as pd


from predictorML_v7 import MLModelMultipleOutput


from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.ensemble import GradientBoostingRegressor
#from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import ExtraTreeRegressor

from xgboost.sklearn import  XGBRegressor
from lightgbm import LGBMRegressor
from skelm import ELMRegressor

def main():

    dfInput = pd.read_csv('dataFrame_prediction_Fw_v14_newFreq.csv',sep=';',decimal=',',index_col=[0])
    dfInput = dfInput[dfInput['deg']<=35]
    #dfInput = dfInput[dfInput['tor'] != 0]


    dfInput.reset_index(inplace=True)
    #dfInput.to_csv('dataFrame_prediction_Fw_v6_newFreq.csv',sep=';',decimal=',')


    files = os.listdir('instances_v3')

    dfOutTot = pd.DataFrame()
    #colsToPredict = ['fft_y_Fw_filtered_ampl_','fft_y_Fw_filtered_phase_']
    colsToPredict = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]

    outputFolder = 'output_prediction/instV3.8_Fw_allFreq_def/'



    ### definitivi PAPER ##

    mlModelsList = [SVR(C=1, epsilon= 0.0001, gamma= 1.1e-06, kernel= 'rbf'),
                    MLPRegressor(activation= 'tanh', early_stopping=True, hidden_layer_sizes= (200, 50), learning_rate= 'adaptive', solver= 'adam', random_state=0),
                    RandomForestRegressor(criterion= 'squared_error', max_depth= 14,  min_samples_split= 3, n_estimators= 90, random_state=0),
                    DecisionTreeRegressor(criterion= 'squared_error', max_depth= 16 ,min_samples_split= 6, random_state=0),
                    ExtraTreeRegressor(criterion='squared_error', max_depth= 15, min_samples_split= 5, random_state=0),
                    ExtraTreesRegressor(criterion='squared_error', max_depth= 15, min_samples_split= 3, n_estimators= 60, random_state=0),
                    GradientBoostingRegressor(criterion= 'squared_error', learning_rate= 0.1, max_depth=14, min_samples_split= 14, n_estimators= 36, random_state=0),
                    HistGradientBoostingRegressor(random_state=0, learning_rate=0.21, max_depth=11, max_leaf_nodes=27),
                    XGBRegressor(reg_lambda=20, alpha=0.01, max_depth=16, colsample_bytree=0.8, random_state=0),
                    LGBMRegressor(learning_rate= 0.39, max_depth= 12, subsample= 0.1, random_state=0),
                    ELMRegressor(n_neurons=250,random_state=0)]



    for m in mlModelsList:
        dfOutTot = pd.DataFrame()
        
        mlModel = MLModelMultipleOutput(m, 'multipleOutputEvaluationOnTrain_3.8_allFreq','tot')
        dfOut = mlModel.predictorMLEvalutationOnTrain(dfInput, 0.20)
        if dfOutTot.empty:
            dfOutTot=dfOut
        else:
            dfOutTot = dfOutTot.merge(dfOut,on=['rpm','deg','tor'])
        #mlModel.exportModel('gbr_MultiOutput_' + 'tot')
        dfOutTot.to_csv(outputFolder+'dfOutTot_prediction_'+mlModel.name+'.csv', sep=';', decimal=',')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
