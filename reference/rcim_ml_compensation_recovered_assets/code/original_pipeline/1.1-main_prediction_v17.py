import pandas as pd

from predictorML_v7 import MLModelMultipleOutput


from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import ExtraTreeRegressor
from xgboost.sklearn import  XGBRegressor
from lightgbm import LGBMRegressor

def main():

    dfInput = pd.read_csv('dataFrame_prediction_Fw_v14_newFreq.csv',sep=';',decimal=',',index_col=[0])
    dfInput = dfInput[dfInput['deg']<=35]
    #dfInput = dfInput[dfInput['tor'] != 0]


    dfInput.reset_index(inplace=True)



    dfOutTot = pd.DataFrame()
    #colsToPredict = ['fft_y_Fw_filtered_ampl_','fft_y_Fw_filtered_phase_']
    colsToPredict = [x for x in dfInput.columns if 'ampl' in x or 'phase' in x]

    outputFolder = 'output_prediction/'

    mlModelsList = [DecisionTreeRegressor(),ExtraTreeRegressor(),ExtraTreesRegressor(),RandomForestRegressor(),
                    GradientBoostingRegressor(),HistGradientBoostingRegressor(),XGBRegressor(),LGBMRegressor(),MLPRegressor()]

    for m in mlModelsList:
        dfOutTot = pd.DataFrame()
        
        mlModel = MLModelMultipleOutput(m, '','tot')
        dfOut = mlModel.predictorML_allForExport(dfInput,0.20)
        if dfOutTot.empty:
            dfOutTot=dfOut
        else:
            dfOutTot = dfOutTot.merge(dfOut,on=['rpm','deg','tor'])
        mlModel.exportModel(mlModel.name+'_MultiOutput_' + 'tot',colsToPredict)
        dfOutTot.to_csv(outputFolder+'dfOutTot_prediction_'+mlModel.name+'.csv', sep=';', decimal=',')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

