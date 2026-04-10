from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import numpy as np
import re
import copy

class PolyFunc:

    def __init__(self,  name, columnToPredict):
        self.columnToPredict = columnToPredict
        self.name = name

    def _func_prediction_v2(self,x_data, *params):
        temp = 0.0

        x_in, y_in = x_data

        # mi serve quando uso la funzione per calcolare i valori perchè
        # passa i parametri come 1 tupla con dentro l'array
        if len(params)==1:
            params = params[0]

        # coefficients
        a = params[0]
        b = params[1]
        c = params[2]
        d = params[3]
        e = params[4]
        f = params[5]
        g = params[6]
        h = params[7]
        i = params[8]
        j = params[9]

        temp = a
        temp += b * 1 * y_in
        temp += c * 1 * y_in ** 2.0
        temp += d * 1 * y_in ** 3.0
        temp += e * x_in * 1
        temp += f * x_in * y_in
        temp += g * x_in * y_in ** 2.0
        temp += h * x_in ** 2.0 * 1
        temp += i * x_in ** 2.0 * y_in
        temp += j * x_in ** 3.0 * 1
        return temp

    def _getPolyFuncOptimalParams(self,x_data,y_data):
        p0 = np.zeros(10)
        params_opt,cov_matrix = curve_fit(self._func_prediction_v2,x_data.values.T,y_data,p0=p0)
        return params_opt,cov_matrix


    def _getPolyFuncValues(self, params_opt, x_data, y_data):
        prev = []
        for i in range(len(y_data)):
             prev.append(self._func_prediction_v2(x_data.values[i],tuple(params_opt)))

        return prev

    def _getInstanceName(self,x_data,files):
        names = []
        #get instance names from x_data
        for i in range(len(x_data)):
            e = x_data.iloc[i]
            map = [x.startswith(str(e['rpm']) + 'rpm' + str(e['deg']) + 'deg') for x in files]
            instanceName = [x for x, y in zip(files, map) if y == True]
            names.append(instanceName[0])

        return names

    def predictorPolyFunc_leaveOneOut(self,dfInput,files):

        dfInputOrig = copy.deepcopy(dfInput)
        out = {}
        for i in range(len(dfInput)):

            elem = dfInputOrig.iloc[i]
            dfInput = dfInputOrig.drop(i)

            x_data_test = pd.DataFrame([elem[['rpm','deg']]])
            y_data_test = [elem[self.columnToPredict]]
            #
            # dfInput_train = dfInput.drop(dfInput.loc[(dfInput['rpm']==float(testFile.split('rpm')[0]))&
            #                                          (dfInput['deg']==float(testFile.split('rpm')[1].split('deg')[0]))].index).reset_index(drop=True)
            #
            x_data_train = dfInput[['rpm','deg']]
            y_data_train = dfInput[self.columnToPredict]

            names = self._getInstanceName(x_data_test,files)


            params_opt,cov_matrix = self._getPolyFuncOptimalParams(x_data_train,y_data_train)

            prev = self._getPolyFuncValues(params_opt,x_data_test,y_data_test)


            out[i] = {'name':names[0],'prev_'+self.columnToPredict:prev[0]}

        dfOut = pd.DataFrame(out).T
        #self.plotGraph(dfOut,)

        return dfOut


    def predictorPolyFunc_NoTest(self,dfInput,files,testFile):


        x_data_compl = dfInput[['rpm','deg']]
        y_data_compl = dfInput[self.columnToPredict]

        dfInput_train = dfInput.drop(dfInput.loc[(dfInput['rpm']==float(testFile.split('rpm')[0]))&
                                                 (dfInput['deg']==float(testFile.split('rpm')[1].split('deg')[0]))].index).reset_index(drop=True)

        x_data_train = dfInput_train[['rpm','deg']]
        y_data_train = dfInput_train[self.columnToPredict]

        names = self._getInstanceName(x_data_compl,files)


        params_opt,cov_matrix = self._getPolyFuncOptimalParams(x_data_train,y_data_train)

        prev = self._getPolyFuncValues(params_opt,x_data_compl,y_data_compl)


        dfOut = {'name':names,'prev_'+self.columnToPredict:prev}
        dfOut = pd.DataFrame(dfOut)

        return dfOut,params_opt


    def predictorPolyFunc(self,dfInput,files):


        x_data_compl = dfInput[['rpm','deg']]
        y_data_compl = dfInput[self.columnToPredict]

        dfInput_train = dfInput#dfInput.drop(dfInput.loc[(dfInput['rpm']==500)&(dfInput['deg']==30)].index).reset_index(drop=True)

        x_data_train = dfInput_train[['rpm','deg']]
        y_data_train = dfInput_train[self.columnToPredict]

        names = self._getInstanceName(x_data_compl,files)


        params_opt,cov_matrix = self._getPolyFuncOptimalParams(x_data_train,y_data_train)

        prev = self._getPolyFuncValues(params_opt,x_data_compl,y_data_compl)


        dfOut = {'name':names,'prev_'+self.columnToPredict:prev}
        dfOut = pd.DataFrame(dfOut)

        return dfOut,params_opt

    def plotGraph(self, dfOut, params):
        x = np.linspace(0, 2500, 250)
        y = np.linspace(20, 50, 30)
        X, Y = np.meshgrid(x, y)
        x_data = (X,Y)

        points = []
        for row in range(len(dfOut)):
            num_regex = r'-?\d+(?:\.\d+)?'
            matches = re.findall(num_regex, dfOut.loc[row,'name'])
            rpm, deg, tor = float(matches[0]), float(matches[1]), float(matches[2])
            points.append((rpm, deg, dfOut.loc[row, 'prev_'+self.columnToPredict]))


        Z = self._func_prediction_v2(x_data,tuple(params))
        #Z = func_prediction_v2_predict_plot(X, Y, params)

        self._LinePlot(X, Y, Z, points)

    def _LinePlot(self, X, Y, Z, points):
        # Create a 3D plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='plasma',alpha=0.5)
        ax.scatter(list(zip(*points))[0], list(zip(*points))[1], list(zip(*points))[2], color='black')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.xlabel(self.columnToPredict)
        #ax.view_init(0,0)
        plt.show()