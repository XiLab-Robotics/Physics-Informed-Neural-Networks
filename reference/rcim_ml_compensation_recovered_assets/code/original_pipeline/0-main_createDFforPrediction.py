# This is a sample Python script.ù
import os
import re
from statistic import Statistics
from matplotlib import pyplot as plt
import pandas as pd


def main():
    inputPath = 'instances_V3'
    s = Statistics()
    #s.read_all_fft(inputPath, vel=100, numFreq=2)
    # for inst in os.listdir(inputPath):
    #     i = Instance.read(inputPath + inst)
    #     i.predicted_TE_Fw('dfOutTot_prediction_gbr_v1.csv', 'fft')
    #     i.predicted_TE_Fw('dfOutTot_prediction_polyfit_v3.csv', 'fft')
    #
    # #i.predicted_TE_Fw('dfOutTot_prediction_svr_v1.csv')
    # #i.predicted_TE_Fw('dfOutTot_prediction_svr_v2.csv')
    # #i.predicted_TE_Fw('dfOutTot_prediction_svr_v3.csv')
    # i.predicted_TE_Fw('dfOutTot_prediction_rf_v1.csv','fft')
    # i.predicted_TE_Fw('dfOutTot_prediction_rf_v2.csv','fft')
    # i.predicted_TE_Fw('dfOutTot_prediction_gbr_v1.csv','fft')
    # i.predicted_TE_Fw('dfOutTot_prediction_gbr_v2.csv','fft')
    # #i.predicted_TE_Fw('dfOutTot_prediction_elastic_v1.csv')
    # #i.predicted_TE_Fw('dfOutTot_prediction_elastic_v2.csv')
    # #i.predicted_TE_Fw('dfOutTot_prediction_sgd_v1.csv')
    # #i.predicted_TE_Fw('dfOutTot_prediction_sgd_v2.csv')
    # #i.predicted_TE_Fw('dfOutTot_prediction_kridge_v1.csv')
    # #i.predicted_TE_Fw('dfOutTot_prediction_kridge_v2.csv')
    # #i.predicted_TE_Fw('dfOutTot_prediction_xgboost_v1.csv')
    # #i.predicted_TE_Fw('dfOutTot_prediction_xgboost_v2.csv')
    # i.predicted_TE_Fw('dfOutTot_prediction_polyfit_v3.csv','fft')
    # #i.predicted_TE_Fw('dfOutTot_prediction_polyfit_v1.csv','fft')
    # #i.predicted_TE_Fw('dfOutTot_prediction_polyfit_v2.csv','fft')

    s.read_all_fft(inputPath)

    df_tot = s.genDfWithAmplEPhase('Bw') #mode Fw or Bw
    df_tot.to_csv('dataFrame_prediction_Bw_v14_newFreq.csv',sep=';',decimal=',')

    # #s.plot2dTest('fft_y_Fw_filtered_freq')
    # fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(7, 6))
    # s.boxPlotFreq('fft_y_Fw_filtered_freq', axes[0])
    # s.boxPlotFreq('fft_y_Fw_filtered_ampl', axes[1])
    # s.boxPlotFreq('fft_y_Fw_filtered_phase', axes[2])
    # fig.tight_layout()
    # fig.show()
    # s.boxPlotFreq('fft_y_Fw_filtered_freq')
    # s.analisi_scatterplot3d_test('fft_y_Fw_filtered_freq', 'tor', 'rpm', 'deg')
    # s.analisi_scatterplot3d_ampl('fft_y_Fw_filtered_ampl', 'tor', 'rpm', 'deg')
    # s.analisi_scatterplot3d('max_TE_Fw','tor','rpm','deg')
    # s.describe_and_boxplot('max_TE_Fw')
    # s.analisi_heatmap('max_TE_Fw','deg','rpm')
    # s.analisi_heatmap_fft('y_Fw_filtered', 'deg', 'rpm')
    # s.analisi_heatmap('position_Max_TE_Fw','deg','rpm')
    # s.analisi_scatterplot('position_Max_TE_Fw','deg','rpm')
    #
    # print('eccolo')
    # all = read_all(inputPath)
    # v = read_all(inputPath,vel=700)
    # d = read_all(inputPath, deg=35)
    # vd = read_all(inputPath,vel=700,deg=45)
    # t = read_all(inputPath,tor=0)
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
