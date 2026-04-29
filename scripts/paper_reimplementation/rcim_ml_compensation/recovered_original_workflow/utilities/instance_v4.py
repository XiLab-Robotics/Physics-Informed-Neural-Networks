import csv
import re

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error,mean_absolute_error
import os


class Instance:
    #fft_listFreq = [0, 1, 40, 80, 120, 160, 240]
    fft_listFreq = [0, 1, 3, 39, 40, 78, 80, 237, 240]
    fft_listFreqNotFiltered = list(range(0,300))

    def __init__(self, x_Fw, y_Fw, x_Bw, y_Bw, max_TE_Fw, max_TE_Bw, position_Max_TE_Fw, position_Max_TE_Bw, rpm,
                 deg, tor, fft_x_Fw, fft_y_Fw, fft_x_Bw, fft_y_Bw, fft_y_Fw_filtered, y_Fw_filtered, fft_y_Fw_ampl,
                 fft_y_Fw_freq,fft_y_Fw_phase,fft_y_Fw_filtered_ampl, fft_y_Fw_filtered_freq,fft_y_Fw_filtered_phase,
                 fft_y_Bw_filtered,y_Bw_filtered,fft_y_Bw_ampl,fft_y_Bw_freq,fft_y_Bw_phase,fft_y_Bw_filtered_ampl,
                 fft_y_Bw_filtered_freq,fft_y_Bw_filtered_phase,name):
        self.x_Fw = x_Fw
        self.y_Fw = y_Fw
        self.x_Bw = x_Bw
        self.y_Bw = y_Bw
        self.max_TE_Fw = max_TE_Fw
        self.max_TE_Bw = max_TE_Bw
        self.position_Max_TE_Fw = position_Max_TE_Fw
        self.position_Max_TE_Bw = position_Max_TE_Bw
        self.rpm = rpm
        self.deg = deg
        self.tor = tor
        self.fft_x_Fw = fft_x_Fw
        self.fft_y_Fw = fft_y_Fw
        self.fft_x_Bw = fft_x_Bw
        self.fft_y_Bw = fft_y_Bw
        self.y_Fw_filtered = y_Fw_filtered
        self.fft_y_Fw_filtered = fft_y_Fw_filtered
        self.fft_y_Fw_filtered_freq = fft_y_Fw_filtered_freq#[0] * len(self.fft_listFreq)
        self.fft_y_Fw_filtered_ampl = fft_y_Fw_filtered_ampl#[0] * len(self.fft_listFreq)
        self.fft_y_Fw_filtered_phase = fft_y_Fw_filtered_phase#[0] * len(self.fft_listFreq)
        self.fft_y_Fw_ampl = fft_y_Fw_ampl
        self.fft_y_Fw_freq = fft_y_Fw_freq
        self.fft_y_Fw_phase = fft_y_Fw_phase
        self.y_Bw_filtered = y_Bw_filtered
        self.fft_y_Bw_filtered = fft_y_Bw_filtered
        self.fft_y_Bw_filtered_freq = fft_y_Bw_filtered_freq#[0] * len(self.fft_listFreq)
        self.fft_y_Bw_filtered_ampl = fft_y_Bw_filtered_ampl#[0] * len(self.fft_listFreq)
        self.fft_y_Bw_filtered_phase = fft_y_Bw_filtered_phase#[0] * len(self.fft_listFreq)
        self.fft_y_Bw_ampl = fft_y_Bw_ampl
        self.fft_y_Bw_freq = fft_y_Bw_freq
        self.fft_y_Bw_phase = fft_y_Bw_phase
        self.name = name

    @classmethod
    def read(self, filename):
        with open(filename, 'r') as csvfile:
            data = list(csv.reader(csvfile))
            data=data[1:]
            data = [[float(c) for c in row] for row in data]
            data = [row for row in data if not np.any(np.isnan(row))]
            x_Fw = [float(row[0]) for row in data]
            y_Fw = [float(row[1]) for row in data]
            x_Bw = [float(row[2]) for row in data]
            y_Bw = [float(row[3]) for row in data]
            max_TE_Fw = min(y_Fw)
            max_TE_Bw = min(y_Bw)
            position_Max_TE_Fw = float(x_Fw[y_Fw.index(max_TE_Fw)])
            position_Max_TE_Bw = float(x_Bw[y_Bw.index(max_TE_Bw)])

            tor = float(re.search(r'(\d+(\.\d+)?|0)Torque', filename).group(1))
            rpm = float(re.search(r'(\d+\.\d+)rpm', filename).group(1))
            deg = float(re.search(r'(\d+\.\d+)deg', filename).group(1))

            #num_regex = r'-?\d+(?:\.\d+)?'
            #matches = re.findall(num_regex, filename)
            #rpm, tor, deg  = float(matches[0]), float(matches[1]), float(matches[2])
            N= len(x_Fw)
            T = 1.0 /4000.0

            fft_y_Fw = np.fft.fft(y_Fw)
            fft_x_Fw = np.linspace(0.0, 1.0/(2.0*T), N//2)
            fft_y_Bw = np.fft.fft(y_Bw)
            fft_x_Bw = np.linspace(0.0, 1.0/(2.0*T), N//2)


            fft_y_Fw_filtered = np.zeros_like(fft_y_Fw)
            fft_y_Fw_filtered[self.fft_listFreq] = fft_y_Fw[self.fft_listFreq]

            fft_y_Bw_filtered = np.zeros_like(fft_y_Bw)
            fft_y_Bw_filtered[self.fft_listFreq] = fft_y_Bw[self.fft_listFreq]

            y_Fw_Notfiltered = np.zeros_like(y_Fw)
            y_Fw_filtered = np.zeros_like(y_Fw)
            y_Bw_Notfiltered = np.zeros_like(y_Bw)
            y_Bw_filtered = np.zeros_like(y_Bw)


            fft_y_Fw_ampl = [0] * len(self.fft_listFreqNotFiltered)
            fft_y_Fw_freq = [0] * len(self.fft_listFreqNotFiltered)
            fft_y_Fw_phase = [0] * len(self.fft_listFreqNotFiltered)


            fft_y_Bw_ampl = [0] * len(self.fft_listFreqNotFiltered)
            fft_y_Bw_freq = [0] * len(self.fft_listFreqNotFiltered)
            fft_y_Bw_phase = [0] * len(self.fft_listFreqNotFiltered)


            fft_y_Fw_filtered_ampl = [0] * len(self.fft_listFreq)
            fft_y_Fw_filtered_freq = [0] * len(self.fft_listFreq)
            fft_y_Fw_filtered_phase = [0] * len(self.fft_listFreq)
            fft_y_Bw_filtered_freq = [0] * len(self.fft_listFreq)
            fft_y_Bw_filtered_ampl = [0] * len(self.fft_listFreq)
            fft_y_Bw_filtered_phase = [0] * len(self.fft_listFreq)




            #CALCULATE filtered Fw
            for i,k in enumerate(self.fft_listFreq):
                Xk = fft_y_Fw_filtered[k]
                if k==0:
                    # fft_y_Fw_filtered_ampl[i] = 1.0 / len(y_Fw) * np.abs(Xk) #calc ampl per == 0
                    fft_y_Fw_filtered_ampl[i] = (1.0 / len(y_Fw) * np.abs(Xk)) * np.cos(np.angle(Xk))  # calc ampl per == 0
                    fft_y_Fw_filtered_phase[i] = 0
                else:
                    fft_y_Fw_filtered_ampl[i] = 2.0 / len(y_Fw) * np.abs(Xk) #calc ampl per != 0
                    fft_y_Fw_filtered_phase[i] = np.angle(Xk)  # calc phase

                fft_y_Fw_filtered_freq[i] = 2 * np.pi * k / len(y_Fw) #calc freq
                n = np.arange(len(y_Fw))
                y_Fw_filtered = y_Fw_filtered + (fft_y_Fw_filtered_ampl[i] * np.cos(fft_y_Fw_filtered_freq[i] * n + fft_y_Fw_filtered_phase[i]))

            #CALCULATE NOT filtered Fw
            for i in range(0,300):
                Xk = fft_y_Fw[i]
                T1 = 54.0
                T2 = 56.0
                fft_y_Fw_freq[i] = 2 * np.pi * i / len(y_Fw)  # calc freq
                if i==0:
                    # fft_y_Fw_filtered_ampl[i] = 1.0 / len(y_Fw) * np.abs(Xk) #calc ampl per == 0
                    fft_y_Fw_ampl[i] = (1.0 / len(y_Fw) * np.abs(Xk)) * np.cos(np.angle(Xk))  # calc ampl per == 0
                    fft_y_Fw_phase[i] = 0
                else:
                    if (fft_x_Fw[i] >= T1) & (fft_x_Fw[i] <= T2):
                        Xk = 0
                    fft_y_Fw_ampl[i] = 2.0 / len(y_Fw) * np.abs(Xk) #calc ampl per != 0
                    fft_y_Fw_phase[i] = np.angle(Xk)  # calc phase


                n = np.arange(len(y_Fw))
                y_Fw_Notfiltered = y_Fw_Notfiltered + (fft_y_Fw_ampl[i] * np.cos(fft_y_Fw_freq[i] * n + fft_y_Fw_phase[i]))


            #CALCULATE filtered Bw
            for i,k in enumerate(self.fft_listFreq):
                Xk = fft_y_Bw_filtered[k]
                if k==0:
                    # fft_y_Fw_filtered_ampl[i] = 1.0 / len(y_Fw) * np.abs(Xk) #calc ampl per == 0
                    fft_y_Bw_filtered_ampl[i] = (1.0 / len(y_Bw) * np.abs(Xk)) * np.cos(np.angle(Xk))  # calc ampl per == 0
                    fft_y_Bw_filtered_phase[i] = 0
                else:
                    fft_y_Bw_filtered_ampl[i] = 2.0 / len(y_Bw) * np.abs(Xk) #calc ampl per != 0
                    fft_y_Bw_filtered_phase[i] = np.angle(Xk)  # calc phase

                fft_y_Bw_filtered_freq[i] = 2 * np.pi * k / len(y_Bw) #calc freq
                n = np.arange(len(y_Bw))
                y_Bw_filtered = y_Bw_filtered + (fft_y_Bw_filtered_ampl[i] * np.cos(fft_y_Bw_filtered_freq[i] * n + fft_y_Bw_filtered_phase[i]))

            #CALCULATE NOT filtered Bw
            for i in range(0,300):
                Xk = fft_y_Bw[i]

                if i==0:
                    # fft_y_Fw_filtered_ampl[i] = 1.0 / len(y_Fw) * np.abs(Xk) #calc ampl per == 0
                    fft_y_Bw_ampl[i] = (1.0 / len(y_Bw) * np.abs(Xk)) * np.cos(np.angle(Xk))  # calc ampl per == 0
                    fft_y_Bw_phase[i] = 0
                else:
                    if (fft_x_Bw[i] >= T1) & (fft_x_Bw[i] <= T2):
                        Xk = 0
                    fft_y_Bw_ampl[i] = 2.0 / len(y_Fw) * np.abs(Xk) #calc ampl per != 0
                    fft_y_Bw_phase[i] = np.angle(Xk)  # calc phase

                fft_y_Bw_freq[i] = 2 * np.pi * i / len(y_Bw) #calc freq
                n = np.arange(len(y_Bw))
                y_Bw_Notfiltered = y_Bw_Notfiltered + (fft_y_Bw_ampl[i] * np.cos(fft_y_Bw_freq[i] * n + fft_y_Bw_phase[i]))



            #print(fft_y_Fw_filtered_phase)
            name = [x for x in filename.split('/') if '.csv' in x][0]


            return self( x_Fw, y_Fw, x_Bw, y_Bw, max_TE_Fw, max_TE_Bw, position_Max_TE_Fw, position_Max_TE_Bw, rpm,
                 deg, tor, fft_x_Fw, fft_y_Fw, fft_x_Bw, fft_y_Bw, fft_y_Fw_filtered, y_Fw_filtered, fft_y_Fw_ampl,
                 fft_y_Fw_freq,fft_y_Fw_phase,fft_y_Fw_filtered_ampl, fft_y_Fw_filtered_freq,fft_y_Fw_filtered_phase,
                 fft_y_Bw_filtered,y_Bw_filtered,fft_y_Bw_ampl,fft_y_Bw_freq,fft_y_Bw_phase,fft_y_Bw_filtered_ampl,
                 fft_y_Bw_filtered_freq,fft_y_Bw_filtered_phase,name)


    def max_error(self, y, y_rec):
        errors = [abs((y[i] - y_rec[i]) / y[i]) for i in range(len(y))]
        #errors = [abs((y[i] - y_rec[i])) for i in range(len(y))]
        return max(errors)

    def max_error_2(self,y, y_rec):
        v = max([abs(y[i]) for i in range(len(y))])
        errors = [abs((y[i] - y_rec[i])) / v for i in range(len(y))]
        max_index = errors.index(max(errors))
        print("CAZZZO: ", y[max_index], y_rec[max_index])
        return max(errors) * 100


    def predicted_TE_Fw_noShow_component(self, filename, mode, data, component):
        ampl = []
        phase = []
        if data.empty:
            data = pd.read_csv(filename, sep=';', decimal=',', index_col=[0])
            for col in data.columns[1:]:
                data[col] = pd.to_numeric(data[col])
        else:
            data = data
        # dataRow = data.loc[(data['rpm'] ==self.rpm)]
        dataRow = data.loc[(data['rpm'] == self.rpm) & (data['deg'] == self.deg) & (data['tor'] == self.tor)]
        if dataRow.empty:
            return 0, 0, 0, 0, data, True

        ampl = [float(dataRow[f"prev_fft_y_Fw_filtered_ampl_{i}"]) for i in self.fft_listFreq]
        phase = [float(dataRow[f"prev_fft_y_Fw_filtered_phase_{i}"]) for i in self.fft_listFreq]

        columnToPredict_ampl = [x for x in data.columns if 'ampl' in x]
        columnToPredict_phase = [x for x in data.columns if 'phase' in x]

        for j in columnToPredict_ampl:
            if j != component:
                freq =  self.fft_listFreq.index(int(j.split('_')[-1]))
                ampl[freq] = self.fft_y_Fw_filtered_ampl[freq]

        for j in columnToPredict_phase:
            if j != component:
                freq =  self.fft_listFreq.index(int(j.split('_')[-1]))
                phase[freq] = self.fft_y_Fw_filtered_phase[freq]


        # ampl[0] = self.fft_y_Fw_filtered_ampl[0]
        # ampl[1] = self.fft_y_Fw_filtered_ampl[1]
        # ampl[2] = self.fft_y_Fw_filtered_ampl[2]
        # ampl[3] = self.fft_y_Fw_filtered_ampl[3]
        # ampl[4] = self.fft_y_Fw_filtered_ampl[4]
        # ampl[5] = self.fft_y_Fw_filtered_ampl[5]
        # ampl[6] = self.fft_y_Fw_filtered_ampl[6]
        #
        # phase[0] = self.fft_y_Fw_filtered_phase[0]
        # phase[1] = self.fft_y_Fw_filtered_phase[1]
        # phase[2] = self.fft_y_Fw_filtered_phase[2]
        # phase[3] = self.fft_y_Fw_filtered_phase[3]
        # phase[4] = self.fft_y_Fw_filtered_phase[4]
        # phase[5] = self.fft_y_Fw_filtered_phase[5]
        #phase[6] = self.fft_y_Fw_filtered_phase[6]


        # assuming there's only one row with the given name, exit loop
        n = np.arange(len(self.x_Fw))
        # Calculate the harmonics of the selected frequencies using cosine
        harmonics = [ampl[i] * np.cos(2 * n * np.pi * k / len(self.x_Fw) + phase[i]) for i, k in
                     enumerate(self.fft_listFreq)]
        # Sum the harmonics together to get the reconstructed signal
        reconstructed_signal_previsto = np.sum(harmonics, axis=0)
        harmonics_fft_filterd = [self.fft_y_Fw_filtered_ampl[i] * np.cos(
            2 * n * np.pi * k / len(self.x_Fw) + self.fft_y_Fw_filtered_phase[i]) for i, k in
                                 enumerate(self.fft_listFreq)]
        reconstructed_signal_fft_filtered = np.sum(harmonics_fft_filterd, axis=0)

        #plt.plot(reconstructed_signal_fft_filtered, color='red', label='orginal_fft')
        # plt.plot(self.y_Fw,color='green', label='orginal')
        #labelName = filename.split('dfOutTot_')[1]
        #plt.plot(reconstructed_signal_previsto, label=labelName)
       # print('reale vs fft, MAPE:', mean_absolute_percentage_error(self.y_Fw, reconstructed_signal_fft_filtered))
        if mode == 'fft':
            mse = mean_squared_error(reconstructed_signal_fft_filtered, reconstructed_signal_previsto)
            rmse = np.sqrt(mse) ##occhio che sta roba non ha senso!!!
            mae = mean_absolute_error(reconstructed_signal_fft_filtered, reconstructed_signal_previsto)
            mape = mean_absolute_percentage_error(reconstructed_signal_fft_filtered, reconstructed_signal_previsto)
            # msle = mean_squared_log_error(reconstructed_signal_fft_filtered,reconstructed_signal_previsto)
        elif mode == 'orig':
            mse = mean_squared_error(self.y_Fw, reconstructed_signal_previsto)
            rmse = np.sqrt(mse)
            mae = mean_absolute_error(self.y_Fw, reconstructed_signal_previsto)
            mape = mean_absolute_percentage_error(self.y_Fw, reconstructed_signal_previsto)
            # msle = mean_squared_log_error(self.y_Fw,reconstructed_signal_previsto)
        else:
            print('ERROR: mode must be \'fft\'or \'orig\'')
            return 0.0, 0.0, 0.0, 0.0
        #plt.xlabel(labelName + '_MSE:' + str(round(mse, 10)) + '_MAPE:' + str(round(mape, 4)))
        #plt.title(self.name)
        #plt.legend()
        #if show:
        #    plt.show()
        return mse, rmse, mae, mape, data, False

    def predicted_TE_Fw_noShow(self, filename, mode, data):
        ampl = []
        phase = []
        if data.empty:
            data = pd.read_csv(filename, sep=';', decimal=',', index_col=[0])
            for col in data.columns[1:]:
                data[col] = pd.to_numeric(data[col])
        else:
            data = data
        # dataRow = data.loc[(data['rpm'] ==self.rpm)]
        dataRow = data.loc[(data['rpm'] == self.rpm) & (data['deg'] == self.deg) & (data['tor'] == self.tor)]
        if dataRow.empty:
            return 0, 0, 0, 0, data, True

        ampl = [float(dataRow[f"prev_fft_y_Fw_filtered_ampl_{i}"]) for i in self.fft_listFreq]
        phase = [float(dataRow[f"prev_fft_y_Fw_filtered_phase_{i}"]) for i in self.fft_listFreq]


        # ampl[0] = self.fft_y_Fw_filtered_ampl[0]
        # ampl[1] = self.fft_y_Fw_filtered_ampl[1]
        # ampl[2] = self.fft_y_Fw_filtered_ampl[2]
        # ampl[3] = self.fft_y_Fw_filtered_ampl[3]
        # ampl[4] = self.fft_y_Fw_filtered_ampl[4]
        # ampl[5] = self.fft_y_Fw_filtered_ampl[5]
        # ampl[6] = self.fft_y_Fw_filtered_ampl[6]
        #
        # phase[0] = self.fft_y_Fw_filtered_phase[0]
        # phase[1] = self.fft_y_Fw_filtered_phase[1]
        # phase[2] = self.fft_y_Fw_filtered_phase[2]
        # phase[3] = self.fft_y_Fw_filtered_phase[3]
        # phase[4] = self.fft_y_Fw_filtered_phase[4]
        # phase[5] = self.fft_y_Fw_filtered_phase[5]
        #phase[6] = self.fft_y_Fw_filtered_phase[6]


        # assuming there's only one row with the given name, exit loop
        n = np.arange(len(self.x_Fw))
        # Calculate the harmonics of the selected frequencies using cosine
        harmonics = [ampl[i] * np.cos(2 * n * np.pi * k / len(self.x_Fw) + phase[i]) for i, k in
                     enumerate(self.fft_listFreq)]
        # Sum the harmonics together to get the reconstructed signal
        reconstructed_signal_previsto = np.sum(harmonics, axis=0)
        harmonics_fft_filterd = [self.fft_y_Fw_filtered_ampl[i] * np.cos(
            2 * n * np.pi * k / len(self.x_Fw) + self.fft_y_Fw_filtered_phase[i]) for i, k in
                                 enumerate(self.fft_listFreq)]
        reconstructed_signal_fft_filtered = np.sum(harmonics_fft_filterd, axis=0)

        #plt.plot(reconstructed_signal_fft_filtered, color='red', label='orginal_fft')
        # plt.plot(self.y_Fw,color='green', label='orginal')
        #labelName = filename.split('dfOutTot_')[1]
        #plt.plot(reconstructed_signal_previsto, label=labelName)
       # print('reale vs fft, MAPE:', mean_absolute_percentage_error(self.y_Fw, reconstructed_signal_fft_filtered))
        if mode == 'fft':
            mse = mean_squared_error(reconstructed_signal_fft_filtered, reconstructed_signal_previsto)
            rmse = np.sqrt(mse) ##occhio che sta roba non ha senso!!!
            mae = mean_absolute_error(reconstructed_signal_fft_filtered, reconstructed_signal_previsto)
            mape = mean_absolute_percentage_error(reconstructed_signal_fft_filtered, reconstructed_signal_previsto)
            # msle = mean_squared_log_error(reconstructed_signal_fft_filtered,reconstructed_signal_previsto)
        elif mode == 'orig':
            mse = mean_squared_error(self.y_Fw, reconstructed_signal_previsto)
            rmse = np.sqrt(mse)
            mae = mean_absolute_error(self.y_Fw, reconstructed_signal_previsto)
            mape = mean_absolute_percentage_error(self.y_Fw, reconstructed_signal_previsto)
            # msle = mean_squared_log_error(self.y_Fw,reconstructed_signal_previsto)
        else:
            print('ERROR: mode must be \'fft\'or \'orig\'')
            return 0.0, 0.0, 0.0, 0.0
        #plt.xlabel(labelName + '_MSE:' + str(round(mse, 10)) + '_MAPE:' + str(round(mape, 4)))
        #plt.title(self.name)
        #plt.legend()
        #if show:
        #    plt.show()
        return mse, rmse, mae, mape, data, False
    def predicted_TE_Fw(self, filename, mode, show, data):
        ampl=[]
        phase=[]
        if data.empty:
            data = pd.read_csv(filename,sep=';',decimal=',', index_col=[0])
            for col in data.columns[1:]:
                data[col] = pd.to_numeric(data[col])
        else:
            data = data
        #dataRow = data.loc[(data['rpm'] ==self.rpm)]
        dataRow = data.loc[(data['rpm'] ==self.rpm)&(data['deg'] ==self.deg)&(data['tor'] ==self.tor)]
        if dataRow.empty:
            return 0, 0, 0, 0, data, True

        ampl = [float(dataRow[f"prev_fft_y_Fw_filtered_ampl_{i}"]) for i in range(len(self.fft_listFreq))]
        phase= [float(dataRow[f"prev_fft_y_Fw_filtered_phase_{i}"]) for i in range(len(self.fft_listFreq))]

        print('ampl_prevista:', ampl)
        print('phase_prevista:', phase)


        print('ampl_orig:', self.fft_y_Fw_filtered_ampl)
        print('phase_prevista:', self.fft_y_Fw_filtered_phase)

        ampl[0] = -0.06583024019#self.fft_y_Fw_filtered_ampl[0]
        ampl[1] = self.fft_y_Fw_filtered_ampl[1]
        ampl[2] = self.fft_y_Fw_filtered_ampl[2]
        ampl[3] = self.fft_y_Fw_filtered_ampl[3]
        ampl[4] = self.fft_y_Fw_filtered_ampl[4]
        ampl[5] = self.fft_y_Fw_filtered_ampl[5]
        ampl[6] = self.fft_y_Fw_filtered_ampl[6]

        phase[0] = self.fft_y_Fw_filtered_phase[0]
        phase[1] = self.fft_y_Fw_filtered_phase[1]
        phase[2] = self.fft_y_Fw_filtered_phase[2]
        phase[3] = self.fft_y_Fw_filtered_phase[3]
        phase[4] = self.fft_y_Fw_filtered_phase[4]
        phase[5] = self.fft_y_Fw_filtered_phase[5]
        phase[6] = self.fft_y_Fw_filtered_phase[6]

        # assuming there's only one row with the given name, exit loop
        n = np.arange( len(self.x_Fw))
        # Calculate the harmonics of the selected frequencies using cosine
        harmonics = [ampl[i]* np.cos(2 *n* np.pi * k / len(self.x_Fw)+phase[i]) for i,k in enumerate(self.fft_listFreq)]
        # Sum the harmonics together to get the reconstructed signal
        reconstructed_signal_previsto = np.sum(harmonics, axis=0)
        harmonics_fft_filterd = [self.fft_y_Fw_filtered_ampl[i]* np.cos(2 *n* np.pi * k / len(self.x_Fw)+self.fft_y_Fw_filtered_phase[i]) for i,k in enumerate(self.fft_listFreq)]
        reconstructed_signal_fft_filtered = np.sum(harmonics_fft_filterd, axis=0)

        #reconstructed_signal_previsto = [x + 0.1 for x in reconstructed_signal_previsto]
        #reconstructed_signal_fft_filtered = [x + 0.1 for x in reconstructed_signal_fft_filtered]

        # listIndex = []
        #
        # for i,v in enumerate(reconstructed_signal_fft_filtered):
        #     if round(v,2) == 0:
        #         listIndex.append(i)
        #
        # reconstructed_signal_fft_filtered = [v for i,v in enumerate(reconstructed_signal_fft_filtered) if i not in listIndex]
        # reconstructed_signal_previsto = [v for i,v in enumerate(reconstructed_signal_previsto) if i not in listIndex]

        plt.plot(reconstructed_signal_fft_filtered, color='red', label='orginal_fft')
        #plt.plot(self.y_Fw,color='green', label='orginal')
        labelName = 'replica_2'#filename.split('dfOutTot_')[1]
        plt.plot(reconstructed_signal_previsto, label=labelName, alpha=0.7)
        #print('reale vs fft, MAPE:', mean_absolute_percentage_error(self.y_Fw,reconstructed_signal_fft_filtered))
        if mode == 'fft':
            pd.DataFrame(reconstructed_signal_fft_filtered).to_csv('controllo_segnaleOrig_x1000.csv',sep=';',decimal=',')
            pd.DataFrame(reconstructed_signal_previsto).to_csv('controllo_segnalePrev_x1000.csv',sep=';', decimal=',')
            mse = mean_squared_error(reconstructed_signal_fft_filtered,reconstructed_signal_previsto)
            rmse = np.sqrt(mse)
            mae = mean_absolute_error(reconstructed_signal_fft_filtered,reconstructed_signal_previsto)
            mape = mean_absolute_percentage_error(reconstructed_signal_fft_filtered, reconstructed_signal_previsto)
            #msle = mean_squared_log_error(reconstructed_signal_fft_filtered,reconstructed_signal_previsto)
        elif mode == 'orig':
            mse = mean_squared_error(self.y_Fw,reconstructed_signal_previsto)
            rmse = np.sqrt(mse)
            mae = mean_absolute_error(self.y_Fw,reconstructed_signal_previsto)
            mape = mean_absolute_percentage_error(self.y_Fw, reconstructed_signal_previsto)
            #msle = mean_squared_log_error(self.y_Fw,reconstructed_signal_previsto)
        else:
            print('ERROR: mode must be \'fft\'or \'orig\'')
            return 0.0,0.0,0.0,0.0
        plt.xlabel(labelName+'_MSE:'+ str(round(mse,10))+'_MAPE:'+str(round(mape,4)))
        plt.title(self.name)
        plt.legend()
        if show:
            plt.show()
        return mse, rmse,mae, mape, data, False
        #er = self.max_error_2(reconstructed_signal_fft_filtered,reconstructed_signal)
        #error = self.max_error_2(self.y_Fw,reconstructed_signal)
        #error2 = self.max_error_2(self.y_Fw,reconstructed_signal)
        #print(error)


    # def filter_freq(self):
    #     #keep only the two largest magnitude coefficients
    #     indices = np.argsort(np.abs(self.fft_y_Fw))[::-1][:n_freq_max]
    #     # Create a copy of the FFT output with only the important coefficients
    #     self.fft_y_Fw_filtered = np.zeros_like(self.fft_y_Fw)
    #     self.fft_y_Fw_filtered[indices] = self.fft_y_Fw[indices]
    #     self.y_Fw_filtered = np.zeros(len(self.x_Fw))
    #     self.fft_y_Fw_filtered_freq = np.zeros(n_freq_max)
    #     self.fft_y_Fw_filtered_ampl = np.zeros(n_freq_max)
    #     self.fft_y_Fw_filtered_phase = np.zeros(n_freq_max)
    #
    #     for i,k in enumerate(indices):
    #         Xk = self.fft_y_Fw_filtered[k]
    #         amplitude = 1.0/len(self.x_Fw) * np.abs(Xk)
    #         phase = np.angle(Xk)
    #         frequency = 2 * np.pi * k / len(self.x_Fw)
    #         self.fft_y_Fw_filtered_freq[i] = frequency
    #         self.fft_y_Fw_filtered_ampl[i] = amplitude
    #         self.fft_y_Fw_filtered_phase[i] = phase
    #         n = np.arange(len(self.x_Fw))
    #         self.y_Fw_filtered = self.y_Fw_filtered +amplitude * np.cos(frequency * n + phase) #- 1j * amplitude * np.sin(frequency * n + phase)
    #
    #     #keep only the two largest magnitude coefficients
    #     indices = np.argsort(np.abs(self.fft_y_Bw))[::-1][:n_freq_max]
    #     # Create a copy of the FFT output with only the important coefficients
    #     self.fft_y_Bw_filtered = np.zeros_like(self.fft_y_Bw)
    #     self.fft_y_Bw_filtered[indices] = self.fft_y_Bw[indices]
    #     self.y_Bw_filtered = np.zeros(len(self.x_Bw))
    #     self.fft_y_Bw_filtered_freq = np.zeros(n_freq_max)
    #     self.fft_y_Bw_filtered_ampl = np.zeros(n_freq_max)
    #     self.fft_y_Bw_filtered_phase = np.zeros(n_freq_max)
    #     for i,k in enumerate(indices):
    #         Xk = self.fft_y_Bw_filtered[k]
    #         amplitude = 1.0/len(self.x_Bw) * np.abs(Xk)
    #         phase = np.angle(Xk)
    #         frequency = 2 * np.pi * k / len(self.x_Bw)
    #         self.fft_y_Bw_filtered_freq[i] = frequency
    #         self.fft_y_Bw_filtered_ampl[i] = amplitude
    #         self.fft_y_Bw_filtered_phase[i] = phase
    #         n = np.arange(len(self.x_Bw))
    #         self.y_Bw_filtered = self.y_Bw_filtered +amplitude * np.cos(frequency * n + phase) #- 1j * amplitude * np.sin(frequency * n + phase)
    #     self._orderVectors()


    def _orderVectors(self):
        # creare una lista di tuple in cui ogni tupla contiene gli elementi dei tre vettori
        tutti_vettori = list(zip(self.fft_y_Fw_filtered_freq, self.fft_y_Fw_filtered_ampl, self.fft_y_Fw_filtered_phase))

        # ordinare la lista di tuple in base agli elementi del primo vettore
        ordinati = sorted(tutti_vettori, key=lambda x: x[0])

        # scomporre la lista ordinata in tre vettori separati
        self.fft_y_Fw_filtered_freq, self.fft_y_Fw_filtered_ampl, self.fft_y_Fw_filtered_phase = zip(*ordinati)


#predicted_TE_Fw()