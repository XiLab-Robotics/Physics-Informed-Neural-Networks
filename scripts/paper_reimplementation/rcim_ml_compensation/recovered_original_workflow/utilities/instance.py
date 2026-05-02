""" Recovered original RCIM instance helper used by dataframe creation and evaluation. """

import os, sys, re, csv

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import mean_squared_error

sys.modules.setdefault("instance_v5", sys.modules[__name__])

class Instance:

    """ Original RCIM instance container for the v5 helper path. """

    fft_listFreq = [0, 1, 3, 39, 40, 78, 81, 156, 162, 240]
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

            # Split the Raw Columns into Forward and Backward Traces.
            x_Fw = [float(row[0]) for row in data]
            y_Fw = [float(row[1]) for row in data]
            x_Bw = [float(row[2]) for row in data]
            y_Bw = [float(row[3]) for row in data]

            # Recover the Original Scalar Metadata from the Waveform.
            max_TE_Fw = min(y_Fw)
            max_TE_Bw = min(y_Bw)
            position_Max_TE_Fw = float(x_Fw[y_Fw.index(max_TE_Fw)])
            position_Max_TE_Bw = float(x_Bw[y_Bw.index(max_TE_Bw)])

            # Parse the Operating Condition Encoded in the Filename.
            tor = float(re.search(r'(\d+(\.\d+)?|0)Torque', filename).group(1))
            rpm = float(re.search(r'(\d+\.\d+)rpm', filename).group(1))
            deg = float(re.search(r'(\d+\.\d+)deg', filename).group(1))

            # Build the FFT Support Used by the Original Harmonic Reconstruction.
            N = len(x_Fw)
            T = 1.0 / 4000.0

            # Build the Forward and Backward FFT Support Arrays.
            fft_y_Fw = np.fft.fft(y_Fw)
            fft_x_Fw = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)
            fft_y_Bw = np.fft.fft(y_Bw)
            fft_x_Bw = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)

            # Keep Only the Harmonics Selected by the Original Filtered Branch.
            fft_y_Fw_filtered = np.zeros_like(fft_y_Fw)
            fft_y_Bw_filtered = np.zeros_like(fft_y_Bw)
            fft_y_Fw_filtered[self.fft_listFreq] = fft_y_Fw[self.fft_listFreq]
            fft_y_Bw_filtered[self.fft_listFreq] = fft_y_Bw[self.fft_listFreq]

            # Prepare the Reconstructed Waveform Buffers.
            y_Fw_Notfiltered = np.zeros_like(y_Fw)
            y_Bw_Notfiltered = np.zeros_like(y_Bw)
            y_Fw_filtered = np.zeros_like(y_Fw)
            y_Bw_filtered = np.zeros_like(y_Bw)

            # Allocate the Dense Harmonic Descriptors.
            fft_y_Fw_ampl  = [0] * len(self.fft_listFreqNotFiltered)
            fft_y_Fw_freq  = [0] * len(self.fft_listFreqNotFiltered)
            fft_y_Fw_phase = [0] * len(self.fft_listFreqNotFiltered)
            fft_y_Bw_ampl  = [0] * len(self.fft_listFreqNotFiltered)
            fft_y_Bw_freq  = [0] * len(self.fft_listFreqNotFiltered)
            fft_y_Bw_phase = [0] * len(self.fft_listFreqNotFiltered)

            # Allocate the Filtered Harmonic Descriptors.
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

                    # Keep the DC Component in Its Scalar Form.
                    fft_y_Fw_filtered_ampl[i] = (1.0 / len(y_Fw) * np.abs(Xk)) * np.cos(np.angle(Xk))
                    fft_y_Fw_filtered_phase[i] = 0

                else:

                    # Convert the Non-DC Harmonic into Amplitude and Phase.
                    fft_y_Fw_filtered_ampl[i] = 2.0 / len(y_Fw) * np.abs(Xk)
                    fft_y_Fw_filtered_phase[i] = np.angle(Xk)

                # Reconstruct the Current Filtered Forward Harmonic in Time Domain.
                fft_y_Fw_filtered_freq[i] = 2 * np.pi * k / len(y_Fw)
                n = np.arange(len(y_Fw))
                y_Fw_filtered = y_Fw_filtered + (fft_y_Fw_filtered_ampl[i] * np.cos(fft_y_Fw_filtered_freq[i] * n + fft_y_Fw_filtered_phase[i]))

            # Calculate the Dense Forward Harmonic Representation.
            for i in range(0, 300):

                # Read the Current Dense Forward Harmonic Coefficient.
                Xk = fft_y_Fw[i]
                fft_y_Fw_freq[i] = 2 * np.pi * i / len(y_Fw)

                if i == 0:

                    # Keep the Dense Forward DC Component in Scalar Form.
                    fft_y_Fw_ampl[i] = (1.0 / len(y_Fw) * np.abs(Xk)) * np.cos(np.angle(Xk))
                    fft_y_Fw_phase[i] = 0

                else:

                    # Convert the Non-DC Dense Forward Harmonic into Amplitude and Phase.
                    fft_y_Fw_ampl[i] = 2.0 / len(y_Fw) * np.abs(Xk)
                    fft_y_Fw_phase[i] = np.angle(Xk)

                # Reconstruct the Current Dense Forward Harmonic in Time Domain.
                n = np.arange(len(y_Fw))
                y_Fw_Notfiltered = y_Fw_Notfiltered + (fft_y_Fw_ampl[i] * np.cos(fft_y_Fw_freq[i] * n + fft_y_Fw_phase[i]))

            # Calculate the Filtered Backward Harmonic Representation.
            for i, k in enumerate(self.fft_listFreq):

                # Read the Current Filtered Backward Harmonic Coefficient.
                Xk = fft_y_Bw_filtered[k]

                if k == 0:

                    # Keep the Backward DC Component in Its Scalar Form.
                    fft_y_Bw_filtered_ampl[i] = (1.0 / len(y_Bw) * np.abs(Xk)) * np.cos(np.angle(Xk))
                    fft_y_Bw_filtered_phase[i] = 0

                else:

                    # Convert the Non-DC Backward Harmonic into Amplitude and Phase.
                    fft_y_Bw_filtered_ampl[i] = 2.0 / len(y_Bw) * np.abs(Xk)
                    fft_y_Bw_filtered_phase[i] = np.angle(Xk)

                # Reconstruct the Current Filtered Backward Harmonic in Time Domain.
                fft_y_Bw_filtered_freq[i] = 2 * np.pi * k / len(y_Bw)
                n = np.arange(len(y_Bw))
                y_Bw_filtered = y_Bw_filtered + (fft_y_Bw_filtered_ampl[i] * np.cos(fft_y_Bw_filtered_freq[i] * n + fft_y_Bw_filtered_phase[i]))

            # Calculate the Dense Backward Harmonic Representation.
            for i in range(0, 300):

                # Read the Current Dense Backward Harmonic Coefficient.
                Xk = fft_y_Bw[i]

                if i == 0:

                    # Keep the Dense Backward DC Component in Scalar Form.
                    fft_y_Bw_ampl[i] = (1.0 / len(y_Bw) * np.abs(Xk)) * np.cos(np.angle(Xk))
                    fft_y_Bw_phase[i] = 0

                else:

                    # Convert the Non-DC Dense Backward Harmonic into Amplitude and Phase.
                    fft_y_Bw_ampl[i] = 2.0 / len(y_Fw) * np.abs(Xk)
                    fft_y_Bw_phase[i] = np.angle(Xk)

                # Reconstruct the Current Dense Backward Harmonic in Time Domain.
                fft_y_Bw_freq[i] = 2 * np.pi * i / len(y_Bw)
                n = np.arange(len(y_Bw))
                y_Bw_Notfiltered = y_Bw_Notfiltered + (fft_y_Bw_ampl[i] * np.cos(fft_y_Bw_freq[i] * n + fft_y_Bw_phase[i]))

            # Keep the Original Filename-Based Instance Naming Contract.
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

        # Compute the Pointwise Relative Error Across the Signal.
        errors = [abs((y[i] - y_rec[i]) / y[i]) for i in range(len(y))]
        return max(errors)

    def max_error_2(self,y, y_rec):

        """ Compute the original normalized maximum error against the max magnitude. """

        # Normalize the Error Against the Largest Absolute Reference Value.
        v = max([abs(y[i]) for i in range(len(y))])
        errors = [abs((y[i] - y_rec[i])) / v for i in range(len(y))]
        return max(errors) * 100

    def _load_prediction_dataframe(self, filename, data):

        """ Load one prediction dataframe only once per evaluation pass. """

        # Reuse The Already-Parsed Prediction Table Whenever The Caller Provides It.
        if not data.empty: return data

        # Parse The Prediction Table From The CSV File.
        loaded_dataframe = pd.read_csv(filename, sep=';', decimal=',', index_col=[0])
        for column_name in loaded_dataframe.columns[1:]: loaded_dataframe[column_name] = pd.to_numeric(loaded_dataframe[column_name])
        return loaded_dataframe

    def _select_prediction_row(self, prediction_dataframe):

        """ Select the prediction row that matches the current operating condition. """

        # Match The Historical rpm-deg-tor Triple Used Throughout The Workflow.
        return prediction_dataframe.loc[
            (prediction_dataframe['rpm'] == self.rpm)
            & (prediction_dataframe['deg'] == self.deg)
            & (prediction_dataframe['tor'] == self.tor)
        ]

    def _reconstruct_signal_pair(self, amplitude_values, phase_values, direction_code):

        """ Reconstruct the predicted and reference filtered signals for one direction. """

        # Resolve The Direction-Specific Reference Arrays Before Reconstructing The Signal Pair.
        if direction_code == 'Fw':

            # Use The Forward Position Grid and the Forward Filtered FFT
            x_values = self.x_Fw
            reference_amplitudes = self.fft_y_Fw_filtered_ampl
            reference_phases = self.fft_y_Fw_filtered_phase

        elif direction_code == 'Bw':

            # Use The Backward Position Grid and the Backward Filtered FFT
            x_values = self.x_Bw
            reference_amplitudes = self.fft_y_Bw_filtered_ampl
            reference_phases = self.fft_y_Bw_filtered_phase

        else:

            # Invalid Direction Code
            raise ValueError(f"Unsupported direction code: {direction_code}")

        # Rebuild The Predicted Harmonic Superposition On The Original Position Grid.
        sample_index = np.arange(len(x_values))
        predicted_harmonic_list = [
            amplitude_values[i] * np.cos(2 * sample_index * np.pi * frequency / len(x_values) + phase_values[i])
            for i, frequency in enumerate(self.fft_listFreq)
        ]
        predicted_signal = np.sum(predicted_harmonic_list, axis=0)

        # Rebuild The Reference Filtered Signal Using The Stored Harmonic Descriptors.
        reference_harmonic_list = [
            reference_amplitudes[i] * np.cos(2 * sample_index * np.pi * frequency / len(x_values) + reference_phases[i])
            for i, frequency in enumerate(self.fft_listFreq)
        ]
        filtered_reference_signal = np.sum(reference_harmonic_list, axis=0)
        return predicted_signal, filtered_reference_signal

    def _compute_prediction_metrics(self, predicted_signal, filtered_reference_signal, mode, direction_code):

        """ Compute the historical metric set for one reconstructed signal. """

        # Compare Against The Filtered FFT Reconstruction Or The Original Time Trace.
        if mode == 'fft': target_signal = filtered_reference_signal
        elif mode == 'orig' and direction_code == 'Fw': target_signal = self.y_Fw
        elif mode == 'orig' and direction_code == 'Bw': target_signal = self.y_Bw
        else: print('ERROR: mode must be \'fft\'or \'orig\''); return 0.0, 0.0, 0.0, 0.0

        # Compute the Pointwise Error Metrics.
        mse = mean_squared_error(target_signal, predicted_signal)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(target_signal, predicted_signal)
        mape = mean_absolute_percentage_error(target_signal, predicted_signal)
        return mse, rmse, mae, mape

    def predicted_TE_Fw_noShow_component(self, filename, mode, data, component):

        """ Evaluate one reconstructed forward component without plotting. """

        # Load the Prediction Table and Select the Prediction Row.
        data = self._load_prediction_dataframe(filename, data)
        prediction_row = self._select_prediction_row(data)
        if prediction_row.empty: return 0, 0, 0, 0, data, True

        # Read the Predicted Filtered Harmonic Descriptors.
        amplitude_values = [float(prediction_row[f"prev_fft_y_Fw_filtered_ampl_{i}"].iloc[0]) for i in self.fft_listFreq]
        phase_values = [float(prediction_row[f"prev_fft_y_Fw_filtered_phase_{i}"].iloc[0]) for i in self.fft_listFreq]

        # Detect Which Harmonic Columns Belong to Amplitude and Phase.
        columnToPredict_ampl = [x for x in data.columns if 'ampl' in x]
        columnToPredict_phase = [x for x in data.columns if 'phase' in x]

        # Restore the Reference Amplitudes for Every Non-Predicted Component.
        for j in columnToPredict_ampl:
            if j != component:

                # Map the Column Suffix Back to the Filtered Frequency Index.
                freq = self.fft_listFreq.index(int(j.split('_')[-1]))
                amplitude_values[freq] = self.fft_y_Fw_filtered_ampl[freq]

        # Restore the Reference Phases for Every Non-Predicted Component.
        for j in columnToPredict_phase:
            if j != component:

                # Map the Column Suffix Back to the Filtered Frequency Index.
                freq = self.fft_listFreq.index(int(j.split('_')[-1]))
                phase_values[freq] = self.fft_y_Fw_filtered_phase[freq]

        # Reconstruct the Predicted and Reference Filtered Signals.
        predicted_signal, filtered_reference_signal = self._reconstruct_signal_pair(amplitude_values, phase_values, 'Fw')
        mse, rmse, mae, mape = self._compute_prediction_metrics(predicted_signal, filtered_reference_signal, mode, 'Fw')

        return mse, rmse, mae, mape, data, False

    def predicted_TE_Fw_noShow(self, filename, mode, data):

        """ Evaluate the reconstructed forward signal without plotting. """

        # Load the Prediction Table and Select the Prediction Row.
        data = self._load_prediction_dataframe(filename, data)
        prediction_row = self._select_prediction_row(data)
        if prediction_row.empty: return 0, 0, 0, 0, data, True

        # Rebuild the Predicted Harmonic Vectors from the Stored Prediction Row.
        amplitude_values = [float(prediction_row[f"prev_fft_y_Fw_filtered_ampl_{i}"].iloc[0]) for i in self.fft_listFreq]
        phase_values = [float(prediction_row[f"prev_fft_y_Fw_filtered_phase_{i}"].iloc[0]) for i in self.fft_listFreq]
        predicted_signal, filtered_reference_signal = self._reconstruct_signal_pair(amplitude_values, phase_values, 'Fw')
        mse, rmse, mae, mape = self._compute_prediction_metrics(predicted_signal, filtered_reference_signal, mode, 'Fw')

        return mse, rmse, mae, mape, data, False

    def predicted_TE(self, filename, mode, show, data, FwBw):

        """ Plot one reconstructed signal branch and compute its error metrics. """

        # Load the Prediction Table and Select the Prediction Row.
        data = self._load_prediction_dataframe(filename, data)
        prediction_row = self._select_prediction_row(data)
        if prediction_row.empty: return 0, 0, 0, 0, data, True

        if FwBw == 'Fw':

            # Rebuild the forward prediction from the stored harmonic vectors.
            amplitude_values = [float(prediction_row[f"prev_fft_y_Fw_filtered_ampl_{i}"].iloc[0]) for i in self.fft_listFreq]
            phase_values = [float(prediction_row[f"prev_fft_y_Fw_filtered_phase_{i}"].iloc[0]) for i in self.fft_listFreq]
            predicted_signal, filtered_reference_signal = self._reconstruct_signal_pair(amplitude_values, phase_values, 'Fw')

        elif FwBw == 'Bw':

            # Rebuild the backward prediction from the stored harmonic vectors.
            amplitude_values = [float(prediction_row[f"prev_fft_y_Bw_filtered_ampl_{i}"].iloc[0]) for i in self.fft_listFreq]
            phase_values = [float(prediction_row[f"prev_fft_y_Bw_filtered_phase_{i}"].iloc[0]) for i in self.fft_listFreq]
            predicted_signal, filtered_reference_signal = self._reconstruct_signal_pair(amplitude_values, phase_values, 'Bw')

        else:

            # Keep the Legacy Direction Error Message Contract Intact.
            print('ERROR: FwBw must be Fw o Bw')
            return 0, 0, 0, 0, data, True

        # Plot the Legacy Comparison View Before Computing the Metric Payload.
        plt.plot(filtered_reference_signal, color='red', label='orginal_fft')
        labelName = filename.split('dfOutTot_')[1]
        plt.plot(predicted_signal, label=labelName, alpha=0.7)

        if mode == 'fft':

            # Compare the Predicted Signal Against the Reference FFT Reconstruction.
            pd.DataFrame(filtered_reference_signal).to_csv('controllo_segnaleOrig_x1000.csv',sep=';',decimal=',')
            pd.DataFrame(predicted_signal).to_csv('controllo_segnalePrev_x1000.csv',sep=';', decimal=',')
            mse, rmse, mae, mape = self._compute_prediction_metrics(predicted_signal, filtered_reference_signal, mode, FwBw)

        elif mode == 'orig':

            # Compare the Predicted Signal Against the Original Time Trace.
            mse, rmse, mae, mape = self._compute_prediction_metrics(predicted_signal, filtered_reference_signal, mode, FwBw)

        else:

            # Keep the Legacy Error Message Contract Intact.
            print('ERROR: mode must be \'fft\'or \'orig\'')
            return 0.0,0.0,0.0,0.0

        # Encode the Metrics into the X-Axis Label Exactly Like the Original Workflow.
        plt.xlabel(labelName+'_MSE:'+ str(round(mse,10))+'_MAPE:'+str(round(mape,4)))
        plt.title(self.name)
        plt.legend()

        # Show the Plot Only When the Caller Explicitly Requests It.
        if show: plt.show()

        else:

            # Preserve the Original Evaluation Export Folder Contract.
            if not os.path.exists('20231120_evalutationSignal/'+filename.split('/')[-1]):
                os.makedirs('20231120_evalutationSignal/'+filename.split('/')[-1])
            plt.savefig('20231120_evalutationSignal/'+filename.split('/')[-1]+'/'+self.name+'.png')
            plt.close()

        return mse, rmse,mae, mape, data, False

    def predicted_TE_Fw(self, filename, mode, show, data):

        """ Plot the reconstructed forward signal and compute its error metrics. """

        # Load the Prediction Table and Select the Prediction Row.
        data = self._load_prediction_dataframe(filename, data)
        prediction_row = self._select_prediction_row(data)
        if prediction_row.empty: return 0, 0, 0, 0, data, True

        # Rebuild the Predicted Harmonic Vectors from the Stored Prediction Row.
        amplitude_values = [float(prediction_row[f"prev_fft_y_Fw_filtered_ampl_{i}"].iloc[0]) for i in self.fft_listFreq]
        phase_values = [float(prediction_row[f"prev_fft_y_Fw_filtered_phase_{i}"].iloc[0]) for i in self.fft_listFreq]
        predicted_signal, filtered_reference_signal = self._reconstruct_signal_pair(amplitude_values, phase_values, 'Fw')

        # Plot the Legacy Comparison View Before Computing the Metric Payload.
        plt.plot(filtered_reference_signal, color='red', label='orginal_fft')
        labelName = filename.split('dfOutTot_')[1]
        plt.plot(predicted_signal, label=labelName, alpha=0.7)

        if mode == 'fft':

            # Compare the Predicted Signal Against the Reference FFT Reconstruction.
            pd.DataFrame(filtered_reference_signal).to_csv('controllo_segnaleOrig_x1000.csv',sep=';',decimal=',')
            pd.DataFrame(predicted_signal).to_csv('controllo_segnalePrev_x1000.csv',sep=';', decimal=',')
            mse, rmse, mae, mape = self._compute_prediction_metrics(predicted_signal, filtered_reference_signal, mode, 'Fw')

        elif mode == 'orig':

            # Compare the Predicted Signal Against the Original Forward Trace.
            mse, rmse, mae, mape = self._compute_prediction_metrics(predicted_signal, filtered_reference_signal, mode, 'Fw')

        else:

            # Keep the Legacy Error Message Contract Intact.
            print('ERROR: mode must be \'fft\'or \'orig\'')
            return 0.0,0.0,0.0,0.0

        # Encode the Metrics into the X-Axis Label Exactly Like the Original Workflow.
        plt.xlabel(labelName+'_MSE:'+ str(round(mse,10))+'_MAPE:'+str(round(mape,4)))
        plt.title(self.name)
        plt.legend()

        # Show the Plot Only When the Caller Explicitly Requests It.
        if show: plt.show()

        else:

            # Preserve the Original Evaluation Export Folder Contract.
            if not os.path.exists('20231120_evalutationSignal/'+filename.split('/')[-1]):
                os.makedirs('20231120_evalutationSignal/'+filename.split('/')[-1])
            plt.savefig('20231120_evalutationSignal/'+filename.split('/')[-1]+'/'+self.name+'.png')
            plt.close()

        return mse, rmse,mae, mape, data, False

    def _orderVectors(self):

        """ Keep the filtered harmonic vectors sorted by frequency. """

        # Zip the Harmonic Vectors Before Sorting Them by Frequency.
        all_vectors = list(zip(self.fft_y_Fw_filtered_freq, self.fft_y_Fw_filtered_ampl, self.fft_y_Fw_filtered_phase))
        ordered = sorted(all_vectors, key=lambda x: x[0])
        self.fft_y_Fw_filtered_freq, self.fft_y_Fw_filtered_ampl, self.fft_y_Fw_filtered_phase = zip(*ordered)
