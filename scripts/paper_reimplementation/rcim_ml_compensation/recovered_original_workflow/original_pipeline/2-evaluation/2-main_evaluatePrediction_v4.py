import os

import numpy as np
import pandas as pd
from instance_v4 import Instance
import re
from statistic import Statistics
from tqdm import tqdm

acronims = {
    'DecisionTreeRegressor': 'DT',
    'ExtraTreeRegressor': 'ET',
    'ExtraTreesRegressor': 'ETs',
    'RandomForestRegressor': 'RF',
    'GradientBoostingRegressor': 'GBM',
    'HistGradientBoostingRegressor': 'HGBM',
    'XGBRegressor': 'XGBM',
    'LGBMRegressor': 'LGBM',
    'SVR': 'SVM',
    'MLPRegressor': 'MLP',
    'MinimumDistance': 'MinDist'
}


def extract_values(inst):
    rpm = inst.rpm
    torque = inst.tor
    deg = inst.deg
    return rpm, torque, deg


def getAcronimMethod(fileName):

    method = ''

    for elem in acronims.keys():
        if elem in fileName:
            method = acronims[elem]

    return method

def custom_sort(main_list, order_list):
    # Creare un dizionario per mappare le stringhe alle loro posizioni nella lista di ordine
    order_dict = {val: idx for idx, val in enumerate(order_list)}

    # Definire una funzione di confronto personalizzata per la funzione di ordinamento
    def custom_compare(item):
        return [order_dict.get(part, float('inf')) for part in item.split('_')]

    # Utilizzare la funzione di confronto personalizzata per ordinare la lista principale
    main_list.sort(key=custom_compare)

# Funzione per convertire i numeri in notazione scientifica
def convert_to_scientific_notation(number):
    return "{:.1e}".format(number)


def exportTableForPaper(df, error, amplPhase, outputFile):

    df_cols = [x for x in df.columns if (error in x) and (amplPhase in x) ]

    df_data = df[df_cols]
    # Applicare la funzione a tutti gli elementi del DataFrame
    df_data = df_data.applymap(convert_to_scientific_notation)
    df_data['method'] = df['method']

    new_order_cols = df_data.columns[-1:].to_list() + df_data.columns[:-1].to_list()
    df_data = df_data[new_order_cols]

    df_data.to_csv(outputFile+'_'+error+'_'+amplPhase+'.csv', sep='\t', index=False)

def main():
    s = Statistics()


    inputPath = 'output_prediction/instV2.1/'
    files = os.listdir(inputPath)
    files = [inputPath+x for x in files if os.path.isfile(inputPath + x) and x[0]!='.']
    custom_sort(files,list(acronims.keys()))

    errors_tot = []

    instancePath = 'instances_v2/'
    s.read_all_fft(instancePath)
    errorsSummary = {'method': [], 'mode': [], 'MSE': [], 'RMSE': [], 'MAE': [], 'MAPE': []}
    count = 0
    for f in files:
        error_tot = {'instance': [], 'rpm': [], 'tor' : [], 'deg':[], 'method': [], 'mode': [],
                     'MSE': [], 'RMSE': [], 'MAE': [], 'MAPE': []}
        errors_component = {'method': [], 'mode': [], 'ampl_phase': [], 'freq': [],
                            'MSE': [], 'RMSE': [], 'MAE': [], 'MAPE': []}
        data = pd.DataFrame()

        method = getAcronimMethod(f)


        for inst in tqdm(s.instances):
            rpm, torque, deg = extract_values(inst)
            i = inst
            f = f#'output_prediction/dfOutTot_prediction_polyfit_v3.csv'
            mode = 'fft'
            mse, rmse, mae, mape, data, skip = i.predicted_TE_Fw_noShow(f, mode, data)
            if skip == True:
                continue
            #mode = 'prevOnlyPhase6'
            count += 1
            error_tot['rpm'].append(rpm)
            error_tot['tor'].append(torque)
            error_tot['deg'].append(deg)
            error_tot['instance'].append(i.name)
            #error_tot['method'].append(f.split('dfOutTot_')[1])
            error_tot['method'].append(method)
            error_tot['mode'].append(mode)
            error_tot['MSE'].append(round(mse, 5))
            error_tot['RMSE'].append(round(rmse, 5))
            error_tot['MAE'].append(round(mae, 5))
            error_tot['MAPE'].append((round(mape, 2)))
            columnToPredict = [x for x in data.columns if 'ampl' in x or 'phase' in x]
            for elem in columnToPredict:
                mse, rmse, mae, mape, data, skip = i.predicted_TE_Fw_noShow_component(f, mode, data, elem)
                #errors_component['method'].append(elem+'_'+str(f.split('/')[2]))
                errors_component['method'].append(method)
                errors_component['mode'].append(mode)
                errors_component['MSE'].append(mse)
                errors_component['RMSE'].append(rmse)
                errors_component['MAE'].append(mae)
                errors_component['MAPE'].append(mape)
                errors_component['ampl_phase'].append(elem.split('_')[-2])
                errors_component['freq'].append(elem.split('_')[-1])

        columnToPredict = [x for x in data.columns if 'ampl' in x or 'phase' in x]
        df_component = pd.DataFrame(errors_component)
        for elem in columnToPredict:
            dfmean = df_component[(df_component['ampl_phase']==elem.split('_')[-2])&(df_component['freq']==elem.split('_')[-1])]
            if elem.split('_')[-2] + '_' + elem.split('_')[-1] + '_' + 'MSE' not in errorsSummary:
                errorsSummary[elem.split('_')[-2] + '_' + elem.split('_')[-1] + '_' + 'MSE'] = []
            if elem.split('_')[-2] + '_' + elem.split('_')[-1] + '_' + 'RMSE' not in errorsSummary:
                errorsSummary[elem.split('_')[-2] + '_' + elem.split('_')[-1] + '_' + 'RMSE'] = []
            if elem.split('_')[-2] + '_' + elem.split('_')[-1] + '_' + 'MAE' not in errorsSummary:
                errorsSummary[elem.split('_')[-2] + '_' + elem.split('_')[-1] + '_' + 'MAE'] = []
            if elem.split('_')[-2] + '_' + elem.split('_')[-1] + '_' + 'MAPE' not in errorsSummary:
                errorsSummary[elem.split('_')[-2] + '_' + elem.split('_')[-1] + '_' + 'MAPE'] = []
            errorsSummary[elem.split('_')[-2] + '_' + elem.split('_')[-1] + '_' + 'MSE'].append(np.mean(dfmean['MSE']))
            errorsSummary[elem.split('_')[-2] + '_' + elem.split('_')[-1] + '_' + 'RMSE'].append(np.mean(dfmean['RMSE']))
            errorsSummary[elem.split('_')[-2] + '_' + elem.split('_')[-1] + '_' + 'MAE'].append(np.mean(dfmean['MAE']))
            errorsSummary[elem.split('_')[-2] + '_' + elem.split('_')[-1] + '_' + 'MAPE'].append(np.mean(dfmean['MAPE']))


        errors_tot.append(error_tot)
        pd.DataFrame(error_tot).to_csv('evaluation/instV2.1/details/dfOutTot_evaluation_details_V2.1'  + '_'
                                       + str(f.split('/')[2]) + '.csv', sep=';', decimal=',')
        errorsSummary['method'].append(error_tot['method'][0])
        #errorsSummary['mode'].append(error_tot['mode'][0])
        errorsSummary['mode'].append(mode)
        errorsSummary['MSE'].append(np.mean(error_tot['MSE']))
        errorsSummary['RMSE'].append(np.mean(error_tot['RMSE']))
        errorsSummary['MAE'].append(np.mean(error_tot['MAE']))
        errorsSummary['MAPE'].append(np.mean(error_tot['MAPE']))

        finalOut = pd.DataFrame(errorsSummary)

        outputFileSummary = 'evaluation/instV2.1/dfOutTot_evaluation_V2.1'+ str(f.split('/')[2])+ '.csv'
        if os.path.isfile(outputFileSummary):
            # Se il file esiste già, carica il contenuto esistente in un DataFrame
            existing_df = pd.read_csv(outputFileSummary, sep=';', decimal=',')

            # Aggiungi il nuovo contenuto al DataFrame esistente
            finalOut = existing_df.append(errorsSummary, ignore_index=True)

        # Salva il DataFrame aggiornato nel file
        finalOut.to_csv(outputFileSummary, sep=';', decimal=',', index=False)

        # error = ['_MSE','_RMSE','_MAE','_MAPE'] , amplPhase = ['ampl','phase']
        if f == files[-1]:
            for e in ['_MSE','_RMSE','_MAE','_MAPE']:
                for a in ['ampl','phase']:
                    if f.split('trainDim')[1].split('_')[1] != "":
                        trainDim = f.split('trainDim')[1].split('_')[1]
                        testDim = f.split('testDim')[1].split('_')[1]
                        exportTableForPaper(finalOut,e,a,'evaluation/instV2.1/perPaper/trainDim_'
                                            +str(trainDim)+'_testDim_'+str(testDim))
                    else:
                        exportTableForPaper(finalOut, e, a, 'evaluation/instV2.1/perPaper/')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
