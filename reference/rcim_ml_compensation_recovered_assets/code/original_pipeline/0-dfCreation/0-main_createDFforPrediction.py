# This is a sample Python script.ù
from statistic import Statistics


def main():
    inputPath = 'instances_v3/'
    s = Statistics()


    s.read_all_fft(inputPath)

    df_tot = s.genDfWithAmplEPhase('Fw') #mode Fw or Bw
    df_tot.to_csv('dataFrame_prediction_Fw_v14_newFreq.csv',sep=';',decimal=',')

    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
