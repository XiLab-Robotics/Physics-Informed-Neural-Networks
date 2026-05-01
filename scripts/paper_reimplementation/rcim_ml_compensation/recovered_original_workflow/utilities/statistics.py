""" Statistics helpers copied from the recovered original RCIM workflow. """

import os, re, pickle

import pandas as pd
from instance import Instance
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from tqdm import tqdm

class Statistics:

    """ Container for the original RCIM dataframe and plotting helpers. """

    def __init__(self, instances=None):
        self.instances = instances

    def _generateDf(self, valueAttribute):

        """ Build a scalar dataframe from one per-instance attribute. """

        errors = []

        for elem in self.instances:

            # Create one row per instance, using the absolute value of the specified attribute for the error column.
            row = {"rpm": elem.rpm, "deg": elem.deg, "tor": elem.tor, valueAttribute: abs(getattr(elem, valueAttribute))}
            errors.append(row)

        df = pd.DataFrame(errors)
        return df

    def _generateDf_ftt(self, valueAttribute):

        """ Build a dataframe using the maximum absolute FFT value per instance. """

        errors = []

        for elem in self.instances:

            # Create one row per instance, using the absolute value of the specified attribute for the error column.
            row = {"rpm": elem.rpm, "deg": elem.deg, "tor": elem.tor, valueAttribute: max([abs(x) for x in getattr(elem, valueAttribute)])}
            errors.append(row)

        df = pd.DataFrame(errors)
        return df

    def _generateDf_ampl(self, valueAttribute):

        """ Build a dataframe using the first amplitude-like value per instance. """

        errors = []

        for elem in self.instances:

            # Create one row per instance, using the absolute value of the specified attribute for the error column.
            row = {"rpm": elem.rpm, "deg": elem.deg, "tor": elem.tor, valueAttribute: getattr(elem, valueAttribute)[0]}
            errors.append(row)

        df = pd.DataFrame(errors)
        return df

    def _generateDf_differentFreq(self, valueAttribute):

        """ Expand one per-instance frequency vector into dataframe columns. """

        errors = []

        for elem in self.instances:

            # Create one row per instance, using the absolute value of the specified attribute for the error column.
            row = {"rpm": elem.rpm, "deg": elem.deg, "tor": elem.tor}

            # Create one column per frequency
            if len(getattr(elem, valueAttribute)) > 0:
                for i in range(len(getattr(elem, valueAttribute))):
                    row[valueAttribute + "_" + str(elem.fft_listFreq[i])] = getattr(elem, valueAttribute)[i]
            errors.append(row)

        df = pd.DataFrame(errors)
        return df

    def _generateInstance(self, filename):

        """ Load one cached instance or create the cache from the source file. """

        # Create a local pickle cache for the instance if it doesn't exist, then load it for the original FFT-specific logic.
        pikName = "instances_V3/" + filename.split("/")[-1].split(".csv")[0]

        # If the pickle exists, load it.
        if os.path.exists(pikName):
            with open(pikName, "rb") as f: ist = pickle.load(f)

        else:

            # Create Instance from the source file and cache it as a pickle for faster future loading.
            ist = Instance.read(filename)
            with open(pikName, "wb") as f: pickle.dump(ist, f)

        return ist

    def read_all(self, inputPath, vel=None, deg=None, tor=None):

        """ Load all matching raw instances without FFT-specific caching. """

        # List all files in the input directory
        files = os.listdir(inputPath)
        files = [inputPath + "/" + x for x in files]
        files_filtered = []
        instances = []

        if vel is None and deg is None and tor is None:

            # If all the filter parameters are None, return all the values in inputPath
            for f in files: instances.append(Instance.read(f))
            self.instances = instances
            return

        for f in files:

            print(f)

            # Filter the list of files based on the filter parameters
            num_regex = r"-?\d+(?:\.\d+)?"
            matches = re.findall(num_regex, f)
            rpm_f, deg_f, tor_f = float(matches[0]), float(matches[1]), float(matches[2])
            if (vel is None or rpm_f == vel) and (deg is None or deg_f == deg) and (tor is None or tor_f == tor):
                files_filtered.append(f)

        # Load the filtered list of files as instances
        for f in files_filtered: instances.append(Instance.read(f))

        self.instances = instances

    def convertNames(self, inputPath):

        """ Normalize legacy torque suffixes inside one input directory. """

        # List all files in the input directory
        files = os.listdir(inputPath)
        files = [inputPath + "/" + x for x in files]

        for f in files:

            # Rename files to replace "Nm" with "Torque"
            if "Torque" in f: continue
            os.rename(f, f.replace("Nm", "Torque"))

    def read_all_fft(self, inputPath, vel=None, deg=None, tor=None, numFreq=None):

        """ Load all matching FFT-ready instances using the local pickle cache. """

        # List all files in the input directory
        files = os.listdir(inputPath)
        files = [inputPath + "/" + x for x in files]
        instances = []

        if vel is None and deg is None and tor is None:

            for f in tqdm(files):

                # Generate an instance for each file, using the local pickle cache when available.
                if "//." in f: continue
                ist = self._generateInstance(f)
                if numFreq is None: instances.append(ist)
                else: instances.append(ist)

            self.instances = instances
            return

    def genDfWithAmplEPhase(self, mode):

        """ Create the original prediction dataframe for one direction. """

        # Get the amplitude and phase dataframes
        df_ampl = self._generateDf_differentFreq("fft_y_" + mode + "_filtered_ampl")
        df_phase = self._generateDf_differentFreq("fft_y_" + mode + "_filtered_phase")
        return df_ampl.merge(df_phase)

    def plot2dTest(self, valueAttribute):

        """ Plot each frequency component over the instance index. """

        # Build a dataframe using the maximum absolute FFT value per instance
        df = self._generateDf_differentFreq(valueAttribute)
        df_f = df[df.columns[3:]].reset_index(drop=True)

        # Plot each frequency component
        for i in range(len(df_f.columns)): plt.plot(df_f.index.to_list(), df_f[df_f.columns[i]], "o", label=df_f.columns[i])
        plt.yscale("log")
        plt.legend()
        plt.show()

    def boxPlotFreq(self, valueAttribute, axes):

        """ Plot one boxplot panel for an expanded frequency dataframe. """

        # Build a dataframe using the maximum absolute FFT value per instance
        df = self._generateDf_differentFreq(valueAttribute)
        df_f = df[df.columns[3:]].reset_index(drop=True)

        # Plot the boxplot
        df_f.columns = range(1, len(df_f.columns) + 1)
        df_f[df_f.columns].plot(ax=axes, kind="box", title=valueAttribute.split("_")[-1])
        if "freq" in valueAttribute: plt.ylim(bottom=-1)

    def analisi_scatterplot3d_freq(self, valueAttribute, x, y, color, freqNum):

        """ Render the original 3D frequency scatter plot. """

        # Build a dataframe using the maximum absolute FFT value per instance
        df = self._generateDf_differentFreq(valueAttribute)

        # Render the 3D scatter plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        sc = ax.scatter(df[x], df[y], df[valueAttribute + "_" + str(freqNum)], c=df[color], cmap="jet")
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_zlabel(valueAttribute + "_" + str(freqNum))
        ax.set_title("3D Scatterplot")
        plt.colorbar(sc, label="Temperature", location="left")
        plt.show()

    def analisi_scatterplot3d_ampl(self, valueAttribute, x, y, color):

        """ Render the original 3D amplitude scatter plot. """

        # Build a dataframe using the maximum absolute FFT value per instance
        df = self._generateDf_ampl(valueAttribute)

        # Render the 3D scatter plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        sc = ax.scatter(df[x], df[y], df[valueAttribute], c=df[color], cmap="jet")
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_zlabel(valueAttribute)
        ax.set_title("3D Scatterplot")
        plt.colorbar(sc, label="Temperature", location="left")
        plt.show()

    def analisi_scatterplot3d(self, valueAttribute, x, y, color):

        """ Render the original 3D scatter plot for one scalar attribute. """

        # Build a dataframe using the maximum absolute FFT value per instance
        df = self._generateDf(valueAttribute)

        # Render the 3D scatter plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        sc = ax.scatter(df[x], df[y], df[valueAttribute], c=df[color], cmap="jet")
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_zlabel(valueAttribute)
        ax.set_title("3D Scatterplot")
        plt.colorbar(sc, label="Temperature", location="left")
        plt.show()

    def analisi_scatterplot(self, valueAttribute, x, y):

        """ Keep the original scatter-plot helper unchanged in behavior. """

        import seaborn as sns

        # Build a dataframe using the maximum absolute FFT value per instance
        df = self._generateDf(valueAttribute)

        # Render the scatter plot
        ax = sns.scatterplot(data=df, x=x, y=y, hue=valueAttribute)
        ax.set_title(valueAttribute)
        sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
        plt.show()

    def analisi_heatmap(self, valueAttribute, x, y):

        """ Keep the original heatmap helper unchanged in behavior. """

        import seaborn as sns

        # Build a dataframe using the maximum absolute FFT value per instance
        df = self._generateDf(valueAttribute)
        df = df.pivot(index=y, columns=x, values=valueAttribute)

        # Render the heatmap
        cmap = sns.cm.rocket_r
        ax = sns.heatmap(df, cmap=cmap)
        ax.set_title(valueAttribute)
        plt.show()

    def analisi_heatmap_fft(self, valueAttribute, x, y):

        """ Keep the original FFT heatmap helper unchanged in behavior. """

        import seaborn as sns

        # Build a dataframe using the maximum absolute FFT value per instance
        df = self._generateDf_ftt(valueAttribute)
        df = df.pivot(index=y, columns=x, values=valueAttribute)

        # Render the heatmap
        cmap = sns.cm.rocket_r
        ax = sns.heatmap(df, cmap=cmap)
        ax.set_title(valueAttribute)
        plt.show()

    def describe_and_boxplot(self, valueAttribute):

        """ Compute descriptive statistics and render the original boxplot. """

        # Build a dataframe using the maximum absolute FFT value per instance
        df = self._generateDf(valueAttribute)
        stats = df[valueAttribute].describe()

        # Render the boxplot
        fig, ax = plt.subplots()
        ax.boxplot(df[valueAttribute], vert=False)

        # Add descriptive statistics as title
        title = (
            f"{valueAttribute} -->"
            f"Stats: {stats['count']} values, mean={stats['mean']:.2f}, std={stats['std']:.2f}, "
            f"min={stats['min']:.2f}, 25%={stats['25%']:.2f}, 50%={stats['50%']:.2f}, "
            f"75%={stats['75%']:.2f}, max={stats['max']:.2f}"
        )
        print(title)
        ax.set_title(valueAttribute)

        plt.show()
