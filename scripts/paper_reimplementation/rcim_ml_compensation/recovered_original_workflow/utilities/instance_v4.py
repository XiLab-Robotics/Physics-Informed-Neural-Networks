""" Recovered original RCIM instance helper used by the evaluation stage. """

import csv, re

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import mean_squared_error

class Instance:

    """ Original RCIM instance container for the v4 evaluation path. """

    fft_listFreq = [0, 1, 3, 39, 40, 78, 80, 237, 240]
    fft_listFreqNotFiltered = list(range(0, 300))

    def __init__(
        self,
        x_Fw,
        y_Fw,
        x_Bw,
        y_Bw,
        max_TE_Fw,
        max_TE_Bw,
        position_Max_TE_Fw,
        position_Max_TE_Bw,
        rpm,
        deg,
        tor,
        fft_x_Fw,
        fft_y_Fw,
        fft_x_Bw,
        fft_y_Bw,
        fft_y_Fw_filtered,
        y_Fw_filtered,
        fft_y_Fw_ampl,
        fft_y_Fw_freq,
        fft_y_Fw_phase,
        fft_y_Fw_filtered_ampl,
        fft_y_Fw_filtered_freq,
        fft_y_Fw_filtered_phase,
        fft_y_Bw_filtered,
        y_Bw_filtered,
        fft_y_Bw_ampl,
        fft_y_Bw_freq,
        fft_y_Bw_phase,
        fft_y_Bw_filtered_ampl,
        fft_y_Bw_filtered_freq,
        fft_y_Bw_filtered_phase,
        name,
    ):

        # Keep the Recovered Original Attribute Surface Intact.
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
        self.fft_y_Fw_filtered_freq = fft_y_Fw_filtered_freq
        self.fft_y_Fw_filtered_ampl = fft_y_Fw_filtered_ampl
        self.fft_y_Fw_filtered_phase = fft_y_Fw_filtered_phase
        self.fft_y_Fw_ampl = fft_y_Fw_ampl
        self.fft_y_Fw_freq = fft_y_Fw_freq
        self.fft_y_Fw_phase = fft_y_Fw_phase
        self.y_Bw_filtered = y_Bw_filtered
        self.fft_y_Bw_filtered = fft_y_Bw_filtered
        self.fft_y_Bw_filtered_freq = fft_y_Bw_filtered_freq
        self.fft_y_Bw_filtered_ampl = fft_y_Bw_filtered_ampl
        self.fft_y_Bw_filtered_phase = fft_y_Bw_filtered_phase
        self.fft_y_Bw_ampl = fft_y_Bw_ampl
        self.fft_y_Bw_freq = fft_y_Bw_freq
        self.fft_y_Bw_phase = fft_y_Bw_phase
        self.name = name

    @classmethod
    def read(self, filename):

        """ Load one original RCIM instance from one exported CSV file. """

        with open(filename, 'r') as csvfile:

            # Read and Sanitize the Exported Original CSV Rows.
            data = list(csv.reader(csvfile))
            data = data[1:]
            data = [[float(c) for c in row] for row in data]
            data = [row for row in data if not np.any(np.isnan(row))]

            # Split the raw columns into forward and backward traces.
            x_Fw = [float(row[0]) for row in data]
            y_Fw = [float(row[1]) for row in data]
            x_Bw = [float(row[2]) for row in data]
            y_Bw = [float(row[3]) for row in data]

            # Recover the original scalar metadata from the waveform.
            max_TE_Fw = min(y_Fw)
            max_TE_Bw = min(y_Bw)
            position_Max_TE_Fw = float(x_Fw[y_Fw.index(max_TE_Fw)])
            position_Max_TE_Bw = float(x_Bw[y_Bw.index(max_TE_Bw)])

            # Parse the operating condition encoded in the filename.
            tor = float(re.search(r'(\d+(\.\d+)?|0)Torque', filename).group(1))
            rpm = float(re.search(r'(\d+\.\d+)rpm', filename).group(1))
            deg = float(re.search(r'(\d+\.\d+)deg', filename).group(1))

            # Build the FFT support used by the original harmonic reconstruction.
            N = len(x_Fw)
            T = 1.0 / 4000.0

            # 
            fft_y_Fw = np.fft.fft(y_Fw)
            fft_x_Fw = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)
            fft_y_Bw = np.fft.fft(y_Bw)
            fft_x_Bw = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)

            # Keep only the harmonics selected by the original filtered branch.
            fft_y_Fw_filtered = np.zeros_like(fft_y_Fw)
            fft_y_Bw_filtered = np.zeros_like(fft_y_Bw)
            fft_y_Fw_filtered[self.fft_listFreq] = fft_y_Fw[self.fft_listFreq]
            fft_y_Bw_filtered[self.fft_listFreq] = fft_y_Bw[self.fft_listFreq]

            # Prepare the reconstructed waveform buffers.
            y_Fw_Notfiltered = np.zeros_like(y_Fw)
            y_Bw_Notfiltered = np.zeros_like(y_Bw)
            y_Fw_filtered = np.zeros_like(y_Fw)
            y_Bw_filtered = np.zeros_like(y_Bw)

            # Allocate the dense harmonic descriptors.
            fft_y_Fw_ampl  = [0] * len(self.fft_listFreqNotFiltered)
            fft_y_Fw_freq  = [0] * len(self.fft_listFreqNotFiltered)
            fft_y_Fw_phase = [0] * len(self.fft_listFreqNotFiltered)
            fft_y_Bw_ampl  = [0] * len(self.fft_listFreqNotFiltered)
            fft_y_Bw_freq  = [0] * len(self.fft_listFreqNotFiltered)
            fft_y_Bw_phase = [0] * len(self.fft_listFreqNotFiltered)

            # Allocate the filtered harmonic descriptors.
            fft_y_Fw_filtered_ampl  = [0] * len(self.fft_listFreq)
            fft_y_Fw_filtered_freq  = [0] * len(self.fft_listFreq)
            fft_y_Fw_filtered_phase = [0] * len(self.fft_listFreq)
            fft_y_Bw_filtered_freq  = [0] * len(self.fft_listFreq)
            fft_y_Bw_filtered_ampl  = [0] * len(self.fft_listFreq)
            fft_y_Bw_filtered_phase = [0] * len(self.fft_listFreq)

            for i, k in enumerate(self.fft_listFreq):

                # Calculate the Filtered Forward Harmonic Representation.
                Xk = fft_y_Fw_filtered[k]

                if k == 0:

                    #
                    fft_y_Fw_filtered_ampl[i] = (1.0 / len(y_Fw) * np.abs(Xk)) * np.cos(np.angle(Xk))
                    fft_y_Fw_filtered_phase[i] = 0

                else:

                    #
                    fft_y_Fw_filtered_ampl[i] = 2.0 / len(y_Fw) * np.abs(Xk)
                    fft_y_Fw_filtered_phase[i] = np.angle(Xk)

                #
                fft_y_Fw_filtered_freq[i] = 2 * np.pi * k / len(y_Fw)
                n = np.arange(len(y_Fw))
                y_Fw_filtered = y_Fw_filtered + (fft_y_Fw_filtered_ampl[i] * np.cos(fft_y_Fw_filtered_freq[i] * n + fft_y_Fw_filtered_phase[i]))

            # Calculate the Dense Forward Harmonic Representation.
            for i in range(0, 300):

                #
                Xk = fft_y_Fw[i]
                fft_y_Fw_freq[i] = 2 * np.pi * i / len(y_Fw)
                T1, T2 = 54.0, 56.0

                if i == 0:

                    #
                    fft_y_Fw_ampl[i] = (1.0 / len(y_Fw) * np.abs(Xk)) * np.cos(np.angle(Xk))
                    fft_y_Fw_phase[i] = 0

                else:

                    #
                    if (fft_x_Fw[i] >= T1) & (fft_x_Fw[i] <= T2): Xk = 0
                    fft_y_Fw_ampl[i] = 2.0 / len(y_Fw) * np.abs(Xk)
                    fft_y_Fw_phase[i] = np.angle(Xk)

                #
                n = np.arange(len(y_Fw))
                y_Fw_Notfiltered = y_Fw_Notfiltered + (fft_y_Fw_ampl[i] * np.cos(fft_y_Fw_freq[i] * n + fft_y_Fw_phase[i]))

            # Calculate the Filtered Backward Harmonic Representation.
            for i, k in enumerate(self.fft_listFreq):

                #
                Xk = fft_y_Bw_filtered[k]

                if k == 0:

                    #
                    fft_y_Bw_filtered_ampl[i] = (1.0 / len(y_Bw) * np.abs(Xk)) * np.cos(np.angle(Xk))
                    fft_y_Bw_filtered_phase[i] = 0

                else:

                    #
                    fft_y_Bw_filtered_ampl[i] = 2.0 / len(y_Bw) * np.abs(Xk)
                    fft_y_Bw_filtered_phase[i] = np.angle(Xk)

                #
                fft_y_Bw_filtered_freq[i] = 2 * np.pi * k / len(y_Bw)
                n = np.arange(len(y_Bw))
                y_Bw_filtered = y_Bw_filtered + (fft_y_Bw_filtered_ampl[i] * np.cos(fft_y_Bw_filtered_freq[i] * n + fft_y_Bw_filtered_phase[i]))

            # Calculate the Dense Backward Harmonic Representation.
            for i in range(0, 300):

                #
                Xk = fft_y_Bw[i]

                if i == 0:

                    #
                    fft_y_Bw_ampl[i] = (1.0 / len(y_Bw) * np.abs(Xk)) * np.cos(np.angle(Xk))
                    fft_y_Bw_phase[i] = 0
                else:

                    #
                    if (fft_x_Bw[i] >= T1) & (fft_x_Bw[i] <= T2): Xk = 0
                    fft_y_Bw_ampl[i] = 2.0 / len(y_Fw) * np.abs(Xk)
                    fft_y_Bw_phase[i] = np.angle(Xk)

                #
                fft_y_Bw_freq[i] = 2 * np.pi * i / len(y_Bw)
                n = np.arange(len(y_Bw))
                y_Bw_Notfiltered = y_Bw_Notfiltered + (fft_y_Bw_ampl[i] * np.cos(fft_y_Bw_freq[i] * n + fft_y_Bw_phase[i]))

            # Keep the original filename-based instance naming contract.
            name = [x for x in filename.split('/') if '.csv' in x][0]

            return self(
                x_Fw,
                y_Fw,
                x_Bw,
                y_Bw,
                max_TE_Fw,
                max_TE_Bw,
                position_Max_TE_Fw,
                position_Max_TE_Bw,
                rpm,
                deg,
                tor,
                fft_x_Fw,
                fft_y_Fw,
                fft_x_Bw,
                fft_y_Bw,
                fft_y_Fw_filtered,
                y_Fw_filtered,
                fft_y_Fw_ampl,
                fft_y_Fw_freq,
                fft_y_Fw_phase,
                fft_y_Fw_filtered_ampl,
                fft_y_Fw_filtered_freq,
                fft_y_Fw_filtered_phase,
                fft_y_Bw_filtered,
                y_Bw_filtered,
                fft_y_Bw_ampl,
                fft_y_Bw_freq,
                fft_y_Bw_phase,
                fft_y_Bw_filtered_ampl,
                fft_y_Bw_filtered_freq,
                fft_y_Bw_filtered_phase,
                name,
            )


    def max_error(self, y, y_rec):

        """ Compute the original normalized maximum pointwise error. """

        #
        errors = [abs((y[i] - y_rec[i]) / y[i]) for i in range(len(y))]
        return max(errors)

    def max_error_2(self,y, y_rec):

        """ Compute the original normalized maximum error against the max magnitude. """

        #
        v = max([abs(y[i]) for i in range(len(y))])
        errors = [abs((y[i] - y_rec[i])) / v for i in range(len(y))]
        return max(errors) * 100

    def predicted_TE_Fw_noShow_component(self, filename, mode, data, component):

        """ Evaluate one reconstructed forward component without plotting. """

        #
        ampl, phase = [],  []

        # Load the Cached Prediction Table Only Once.
        if data.empty:

            #
            data = pd.read_csv(filename, sep=';', decimal=',', index_col=[0])
            for col in data.columns[1:]: data[col] = pd.to_numeric(data[col])

        #
        else: data = data

        # Select the Row That Matches the Current Operating Condition.
        dataRow = data.loc[(data['rpm'] == self.rpm) & (data['deg'] == self.deg) & (data['tor'] == self.tor)]
        if dataRow.empty: return 0, 0, 0, 0, data, True

        # Read the Predicted Filtered Harmonic Descriptors.
        ampl = [float(dataRow[f"prev_fft_y_Fw_filtered_ampl_{i}"]) for i in self.fft_listFreq]
        phase = [float(dataRow[f"prev_fft_y_Fw_filtered_phase_{i}"]) for i in self.fft_listFreq]

        # Detect Which Harmonic Columns Belong to Amplitude and Phase.
        columnToPredict_ampl = [x for x in data.columns if 'ampl' in x]
        columnToPredict_phase = [x for x in data.columns if 'phase' in x]

        # Restore the Reference Amplitudes for Every Non-Predicted Component.
        for j in columnToPredict_ampl:
            if j != component:

                #
                freq = self.fft_listFreq.index(int(j.split('_')[-1]))
                ampl[freq] = self.fft_y_Fw_filtered_ampl[freq]

        # Restore the Reference Phases for Every Non-Predicted Component.
        for j in columnToPredict_phase:
            if j != component:

                #
                freq = self.fft_listFreq.index(int(j.split('_')[-1]))
                phase[freq] = self.fft_y_Fw_filtered_phase[freq]

        # Reconstruct the Predicted and Reference Filtered Signals.
        n = np.arange(len(self.x_Fw))
        harmonics = [ampl[i] * np.cos(2 * n * np.pi * k / len(self.x_Fw) + phase[i]) for i, k in enumerate(self.fft_listFreq)]
        reconstructed_signal_previsto = np.sum(harmonics, axis=0)
        harmonics_fft_filterd = [self.fft_y_Fw_filtered_ampl[i] * np.cos(2 * n * np.pi * k / len(self.x_Fw) + self.fft_y_Fw_filtered_phase[i]) for i, k in enumerate(self.fft_listFreq)]
        reconstructed_signal_fft_filtered = np.sum(harmonics_fft_filterd, axis=0)

        if mode == 'fft':

            #
            mse = mean_squared_error(reconstructed_signal_fft_filtered, reconstructed_signal_previsto)
            rmse = np.sqrt(mse)
            mae = mean_absolute_error(reconstructed_signal_fft_filtered, reconstructed_signal_previsto)
            mape = mean_absolute_percentage_error(reconstructed_signal_fft_filtered, reconstructed_signal_previsto)

        elif mode == 'orig':

            #
            mse = mean_squared_error(self.y_Fw, reconstructed_signal_previsto)
            rmse = np.sqrt(mse)
            mae = mean_absolute_error(self.y_Fw, reconstructed_signal_previsto)
            mape = mean_absolute_percentage_error(self.y_Fw, reconstructed_signal_previsto)

        else:

            #
            print('ERROR: mode must be \'fft\'or \'orig\'')
            return 0.0, 0.0, 0.0, 0.0

        return mse, rmse, mae, mape, data, False

    def predicted_TE_Fw_noShow(self, filename, mode, data):

        """ Evaluate the reconstructed forward signal without plotting. """

        ampl, phase = [], []

        if data.empty:

            # Load the cached prediction table only once when the caller did not provide an already-parsed dataframe.
            data = pd.read_csv(filename, sep=';', decimal=',', index_col=[0])
            for col in data.columns[1:]: data[col] = pd.to_numeric(data[col])

        #
        else: data = data

        # Select the row that matches the current operating condition.
        dataRow = data.loc[(data['rpm'] == self.rpm) & (data['deg'] == self.deg) & (data['tor'] == self.tor)]
        if dataRow.empty: return 0, 0, 0, 0, data, True

        # Rebuild the predicted harmonic vectors from the stored prediction row.
        ampl = [float(dataRow[f"prev_fft_y_Fw_filtered_ampl_{i}"]) for i in self.fft_listFreq]
        phase = [float(dataRow[f"prev_fft_y_Fw_filtered_phase_{i}"]) for i in self.fft_listFreq]

        # Reconstruct both the predicted signal and the reference filtered one.
        n = np.arange(len(self.x_Fw))
        harmonics = [ampl[i] * np.cos(2 * n * np.pi * k / len(self.x_Fw) + phase[i]) for i, k in enumerate(self.fft_listFreq)]
        reconstructed_signal_previsto = np.sum(harmonics, axis=0)
        harmonics_fft_filterd = [self.fft_y_Fw_filtered_ampl[i] * np.cos(2 * n * np.pi * k / len(self.x_Fw) + self.fft_y_Fw_filtered_phase[i]) for i, k in enumerate(self.fft_listFreq)]
        reconstructed_signal_fft_filtered = np.sum(harmonics_fft_filterd, axis=0)

        if mode == 'fft':

            #
            mse = mean_squared_error(reconstructed_signal_fft_filtered, reconstructed_signal_previsto)
            rmse = np.sqrt(mse)
            mae = mean_absolute_error(reconstructed_signal_fft_filtered, reconstructed_signal_previsto)
            mape = mean_absolute_percentage_error(reconstructed_signal_fft_filtered, reconstructed_signal_previsto)

        elif mode == 'orig':

            #
            mse = mean_squared_error(self.y_Fw, reconstructed_signal_previsto)
            rmse = np.sqrt(mse)
            mae = mean_absolute_error(self.y_Fw, reconstructed_signal_previsto)
            mape = mean_absolute_percentage_error(self.y_Fw, reconstructed_signal_previsto)

        else:

            #
            print('ERROR: mode must be \'fft\'or \'orig\'')
            return 0.0, 0.0, 0.0, 0.0

        return mse, rmse, mae, mape, data, False

    def predicted_TE_Fw(self, filename, mode, show, data):

        """ Plot the reconstructed forward signal and compute its error metrics. """

        #
        ampl, phase = [], []

        if data.empty:

            # Load the cached prediction table only once when needed.
            data = pd.read_csv(filename, sep=';', decimal=',', index_col=[0])
            for col in data.columns[1:]: data[col] = pd.to_numeric(data[col])

        #
        else: data = data

        # Select the row that matches the current operating condition.
        dataRow = data.loc[(data['rpm'] == self.rpm) & (data['deg'] == self.deg) & (data['tor'] == self.tor)]
        if dataRow.empty: return 0, 0, 0, 0, data, True

        # Rebuild the predicted harmonic vectors from the stored prediction row.
        ampl = [float(dataRow[f"prev_fft_y_Fw_filtered_ampl_{i}"]) for i in range(len(self.fft_listFreq))]
        phase = [float(dataRow[f"prev_fft_y_Fw_filtered_phase_{i}"]) for i in range(len(self.fft_listFreq))]

        #
        print('ampl_prevista:', ampl)
        print('phase_prevista:', phase)

        #
        print('ampl_orig:', self.fft_y_Fw_filtered_ampl)
        print('phase_prevista:', self.fft_y_Fw_filtered_phase)

        # Keep the legacy manual override path intact because it belongs to the recovered original evaluation workflow that we want to preserve.
        ampl[0] = -0.06583024019
        ampl[1] = self.fft_y_Fw_filtered_ampl[1]
        ampl[2] = self.fft_y_Fw_filtered_ampl[2]
        ampl[3] = self.fft_y_Fw_filtered_ampl[3]
        ampl[4] = self.fft_y_Fw_filtered_ampl[4]
        ampl[5] = self.fft_y_Fw_filtered_ampl[5]
        ampl[6] = self.fft_y_Fw_filtered_ampl[6]

        #
        phase[0] = self.fft_y_Fw_filtered_phase[0]
        phase[1] = self.fft_y_Fw_filtered_phase[1]
        phase[2] = self.fft_y_Fw_filtered_phase[2]
        phase[3] = self.fft_y_Fw_filtered_phase[3]
        phase[4] = self.fft_y_Fw_filtered_phase[4]
        phase[5] = self.fft_y_Fw_filtered_phase[5]
        phase[6] = self.fft_y_Fw_filtered_phase[6]

        # Reconstruct both the predicted signal and the reference filtered one.
        n = np.arange(len(self.x_Fw))
        harmonics = [ampl[i] * np.cos(2 * n * np.pi * k / len(self.x_Fw) + phase[i]) for i, k in enumerate(self.fft_listFreq)]
        reconstructed_signal_previsto = np.sum(harmonics, axis=0)
        harmonics_fft_filterd = [self.fft_y_Fw_filtered_ampl[i] * np.cos(2 * n * np.pi * k / len(self.x_Fw) + self.fft_y_Fw_filtered_phase[i]) for i, k in enumerate(self.fft_listFreq)]
        reconstructed_signal_fft_filtered = np.sum(harmonics_fft_filterd, axis=0)

        # Plot the legacy comparison view before computing the metric payload.
        plt.plot(reconstructed_signal_fft_filtered, color='red', label='orginal_fft')
        labelName = 'replica_2'
        plt.plot(reconstructed_signal_previsto, label=labelName, alpha=0.7)

        if mode == 'fft':

            #
            pd.DataFrame(reconstructed_signal_fft_filtered).to_csv('controllo_segnaleOrig_x1000.csv', sep=';', decimal=',')
            pd.DataFrame(reconstructed_signal_previsto).to_csv('controllo_segnalePrev_x1000.csv', sep=';', decimal=',')
            mse = mean_squared_error(reconstructed_signal_fft_filtered, reconstructed_signal_previsto)
            rmse = np.sqrt(mse)
            mae = mean_absolute_error(reconstructed_signal_fft_filtered, reconstructed_signal_previsto)
            mape = mean_absolute_percentage_error(reconstructed_signal_fft_filtered, reconstructed_signal_previsto)

        elif mode == 'orig':

            #
            mse = mean_squared_error(self.y_Fw, reconstructed_signal_previsto)
            rmse = np.sqrt(mse)
            mae = mean_absolute_error(self.y_Fw, reconstructed_signal_previsto)
            mape = mean_absolute_percentage_error(self.y_Fw, reconstructed_signal_previsto)

        else:

            #
            print('ERROR: mode must be \'fft\'or \'orig\'')
            return 0.0, 0.0, 0.0, 0.0

        # Encode the metrics into the x-axis label exactly like the original workflow.
        plt.xlabel(labelName + '_MSE:' + str(round(mse, 10)) + '_MAPE:' + str(round(mape, 4)))
        plt.title(self.name)
        plt.legend()

        #
        if show: plt.show()

        return mse, rmse, mae, mape, data, False

    def _orderVectors(self):

        """ Keep the filtered harmonic vectors sorted by frequency. """

        #
        all_vectors = list(zip(self.fft_y_Fw_filtered_freq, self.fft_y_Fw_filtered_ampl, self.fft_y_Fw_filtered_phase))
        ordered = sorted(all_vectors, key=lambda x: x[0])
        self.fft_y_Fw_filtered_freq, self.fft_y_Fw_filtered_ampl, self.fft_y_Fw_filtered_phase = zip(*ordered)
