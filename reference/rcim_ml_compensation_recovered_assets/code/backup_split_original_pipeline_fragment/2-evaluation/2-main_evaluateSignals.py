# This is a sample Python script.
import os
import re
from instance_v5 import Instance
from statistic import Statistics
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from tqdm import tqdm
import statistic

def extract_values(input_string):
    rpm_match = re.search(r'(\d*\.\d+)rpm', input_string)
    torque_match = re.search(r'(\d*\.\d+)Torque', input_string)
    deg_match = re.search(r'(\d*\.\d+)deg', input_string)

    rpm = float(rpm_match.group(1)) if rpm_match else None
    torque = float(torque_match.group(1)) if torque_match else None
    deg = float(deg_match.group(1)) if deg_match else None

    if torque == None:
        torque = 0
    if rpm == None:
        rpm = 0
    if deg == None:
        deg = 0

    return rpm, torque, deg



def evaluatePredictionFile(s,filePrediction):
    sigMSE = []
    sigRMSE = []
    sigMAE = []
    sigMAPE = []
    outputDf = {}
    for inst in tqdm(s.instances):
        data = pd.DataFrame()

        i = inst
        ret = i.predicted_TE(filePrediction,'fft',False, data, 'Fw')

        if(ret[0]!=0):
            sigMSE.append(ret[0])
            sigRMSE.append(ret[1])
            sigMAE.append(ret[2])
            sigMAPE.append(ret[3])


    outputDf['file'] = filePrediction
    outputDf['MSE'] = np.mean(sigMSE)
    outputDf['RMSE'] = np.mean(sigRMSE)
    outputDf['MAE'] = np.mean(sigMAE)
    outputDf['MAPE'] = np.mean(sigMAPE)
    outputDf = pd.DataFrame(outputDf,index=[0])

    outputFileSignalErrors = '20240130_evaluationSignal/outputSignalErrors_V3.5_Fw_allFreq_def.csv'

    if os.path.isfile(outputFileSignalErrors):
        # Se il file esiste già, carica il contenuto esistente in un DataFrame
        existing_df = pd.read_csv(outputFileSignalErrors, sep=';', decimal=',')

        # Aggiungi il nuovo contenuto al DataFrame esistente
        outputDf = pd.concat([existing_df, outputDf])
        # finalOut = existing_df.append(pd.DataFrame(crossValOut,index=[0]), ignore_index=True)

        # Salva il DataFrame aggiornato nel file
    outputDf.to_csv(outputFileSignalErrors, sep=';', decimal=',', index=False)


def main():
    inputPath = 'instances_v3/'
    s = Statistics()
    s.read_all_fft(inputPath)
    dir = 'output_prediction/instV3.5_Fw_allFreq_def/'
    fileList = [x for x in os.listdir(dir) if 'dfOutTot' in x]
    for f in fileList:
        if os.path.isfile(dir+f):
            evaluatePredictionFile(s,dir+f)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
