""" Statistics helpers copied from the recovered original RCIM workflow. """

import re, shutil, pickle
from pathlib import Path

import pandas as pd
from instance import Instance
from matplotlib import pyplot as plt
from tqdm import tqdm

class Statistics:

    """ Container for the original RCIM dataframe and plotting helpers. """

    def __init__(self, instances=None, instance_cache_directory_path=None):

        # Keep The Recovered Workflow State Explicit.
        self.instances = instances
        self.instance_cache_directory_path = (
            Path(instance_cache_directory_path).resolve()
            if instance_cache_directory_path is not None
            else None
        )

        # Create The Shared Pickle Cache Directory Only When The Caller Configures One.
        if self.instance_cache_directory_path is not None:
            self.instance_cache_directory_path.mkdir(parents=True, exist_ok=True)

    def _build_scalar_dataframe(self, value_attribute):

        """ Build a scalar dataframe from one per-instance attribute. """

        row_list = []

        for instance in self.instances:

            # Create One Row Per Instance Using The Requested Scalar Attribute.
            row = {
                "rpm": instance.rpm,
                "deg": instance.deg,
                "tor": instance.tor,
                value_attribute: abs(getattr(instance, value_attribute)),
            }
            row_list.append(row)

        return pd.DataFrame(row_list)

    def _build_fft_max_dataframe(self, value_attribute):

        """ Build a dataframe using the maximum absolute FFT value per instance. """

        row_list = []

        for instance in self.instances:

            # Collapse The FFT Vector To The Historical Maximum-Absolute Scalar.
            row = {
                "rpm": instance.rpm,
                "deg": instance.deg,
                "tor": instance.tor,
                value_attribute: max(abs(value) for value in getattr(instance, value_attribute)),
            }
            row_list.append(row)

        return pd.DataFrame(row_list)

    def _build_amplitude_dataframe(self, value_attribute):

        """ Build a dataframe using the first amplitude-like value per instance. """

        row_list = []

        for instance in self.instances:

            # Keep The First Amplitude Entry Exactly Like The Original Helper.
            row = {
                "rpm": instance.rpm,
                "deg": instance.deg,
                "tor": instance.tor,
                value_attribute: getattr(instance, value_attribute)[0],
            }
            row_list.append(row)

        return pd.DataFrame(row_list)

    def _build_frequency_dataframe(self, value_attribute):

        """ Expand one per-instance frequency vector into dataframe columns. """

        row_list = []

        for instance in self.instances:

            # Start From The Shared Operating-Condition Columns.
            row = {"rpm": instance.rpm, "deg": instance.deg, "tor": instance.tor}
            value_vector = getattr(instance, value_attribute)

            # Expand One Column Per Harmonic Frequency.
            if len(value_vector) > 0:
                for index, frequency in enumerate(instance.fft_listFreq):
                    row[f"{value_attribute}_{frequency}"] = value_vector[index]

            row_list.append(row)

        return pd.DataFrame(row_list)

    def _build_cache_file_path(self, source_file_path):

        """ Build the shared cache file path for one source CSV instance file. """

        # Persist Pickles With An Explicit .pickle Suffix Inside The Shared Cache Directory.
        if self.instance_cache_directory_path is None:
            return None

        source_file_path = Path(source_file_path)
        return self.instance_cache_directory_path / f"{source_file_path.stem}.pickle"

    def _load_cached_instance(self, cache_file_path):

        """ Load one pickled instance from the shared cache directory. """

        # Keep The Cache Loader Isolated So The Main Loop Stays Readable.
        with open(cache_file_path, "rb") as handle:
            return pickle.load(handle)

    def _write_cached_instance(self, cache_file_path, instance):

        """ Persist one pickled instance into the shared cache directory. """

        # Create Or Update The Shared Cache File For Faster Future Loads.
        with open(cache_file_path, "wb") as handle:
            pickle.dump(instance, handle)

    def _load_or_create_instance(self, source_file_path):

        """ Load one cached instance or create the cache from the source file. """

        source_file_path = Path(source_file_path)
        cache_file_path = self._build_cache_file_path(source_file_path)

        # Mirror Source Pickles Into The Shared Repository-Owned Cache When Available.
        if source_file_path.suffix.lower() == ".pickle":
            if cache_file_path is not None and not cache_file_path.exists():
                shutil.copy2(source_file_path, cache_file_path)
            if cache_file_path is not None:
                return self._load_cached_instance(cache_file_path)
            return self._load_cached_instance(source_file_path)

        # Otherwise Reuse Or Create The Repository-Owned Shared Cache File.
        if cache_file_path is not None and cache_file_path.exists():
            return self._load_cached_instance(cache_file_path)

        instance = Instance.read(str(source_file_path))
        if cache_file_path is not None:
            self._write_cached_instance(cache_file_path, instance)
        return instance

    def _iter_source_file_paths(self, input_path):

        """ Yield the sorted file list used by the original loading helpers. """

        # Keep The File Iteration Stable So Cache Reuse And Debug Prints Stay Predictable.
        input_directory_path = Path(input_path)
        candidate_file_path_list = sorted(
            file_path
            for file_path in input_directory_path.iterdir()
            if file_path.is_file() and not file_path.name.startswith(".")
        )

        # Prefer Serialized Pickles Over CSV Files When Both Exist For The Same Stem.
        preferred_file_path_by_stem = {}
        for file_path in candidate_file_path_list:
            existing_file_path = preferred_file_path_by_stem.get(file_path.stem)
            if existing_file_path is None:
                preferred_file_path_by_stem[file_path.stem] = file_path
                continue
            if file_path.suffix.lower() == ".pickle":
                preferred_file_path_by_stem[file_path.stem] = file_path

        return list(preferred_file_path_by_stem.values())

    def read_all_instances(self, input_path, vel=None, deg=None, tor=None):

        """ Load all matching raw instances without FFT-specific caching. """

        source_file_path_list = self._iter_source_file_paths(input_path)
        filtered_source_file_path_list = []
        instance_list = []

        if vel is None and deg is None and tor is None:

            # Keep The Original All-Instances Branch Available For Manual Exploration.
            for source_file_path in source_file_path_list:
                instance_list.append(Instance.read(str(source_file_path)))
            self.instances = instance_list
            return

        for source_file_path in source_file_path_list:

            # Preserve The Historical Debug Print Before Filename Filtering.
            print(source_file_path)

            # Filter The Source Files By The Encoded Operating Condition.
            numeric_regex = r"-?\d+(?:\.\d+)?"
            matches = re.findall(numeric_regex, str(source_file_path))
            rpm_value, deg_value, tor_value = float(matches[0]), float(matches[1]), float(matches[2])

            if (
                (vel is None or rpm_value == vel)
                and (deg is None or deg_value == deg)
                and (tor is None or tor_value == tor)
            ):
                filtered_source_file_path_list.append(source_file_path)

        # Materialize The Filtered Instances Without The FFT Cache Branch.
        for source_file_path in filtered_source_file_path_list:
            instance_list.append(Instance.read(str(source_file_path)))

        self.instances = instance_list

    def normalize_legacy_names(self, input_path):

        """ Normalize legacy torque suffixes inside one input directory. """

        for source_file_path in self._iter_source_file_paths(input_path):

            # Rename Legacy Nm Files To The Torque Suffix Used By The Later Workflow.
            if "Torque" in str(source_file_path):
                continue

            renamed_path = str(source_file_path).replace("Nm", "Torque")
            source_file_path.rename(renamed_path)

    def read_all_fft_instances(self, input_path, vel=None, deg=None, tor=None, num_freq=None):

        """ Load all matching FFT-ready instances using the shared pickle cache. """

        source_file_path_list = self._iter_source_file_paths(input_path)
        instance_list = []

        if vel is None and deg is None and tor is None:

            for source_file_path in tqdm(source_file_path_list):

                # Load Or Build One Instance While Reusing The Shared Pickle Cache.
                instance = self._load_or_create_instance(source_file_path)

                # Keep The Historical numFreq Argument Surface Even Though The Branches Match.
                if num_freq is None:
                    instance_list.append(instance)
                else:
                    instance_list.append(instance)

            self.instances = instance_list
            return

    def build_prediction_dataframe_with_amplitude_and_phase(self, mode):

        """ Create the original prediction dataframe for one direction. """

        amplitude_dataframe = self._build_frequency_dataframe(f"fft_y_{mode}_filtered_ampl")
        phase_dataframe = self._build_frequency_dataframe(f"fft_y_{mode}_filtered_phase")
        return amplitude_dataframe.merge(phase_dataframe)

    def plot2dTest(self, valueAttribute):

        """ Plot each frequency component over the instance index. """

        frequency_dataframe = self._build_frequency_dataframe(valueAttribute)
        frequency_value_dataframe = frequency_dataframe[frequency_dataframe.columns[3:]].reset_index(drop=True)

        for column_name in frequency_value_dataframe.columns:
            plt.plot(
                frequency_value_dataframe.index.to_list(),
                frequency_value_dataframe[column_name],
                "o",
                label=column_name,
            )

        plt.yscale("log")
        plt.legend()
        plt.show()

    def boxPlotFreq(self, valueAttribute, axes):

        """ Plot one boxplot panel for an expanded frequency dataframe. """

        frequency_dataframe = self._build_frequency_dataframe(valueAttribute)
        frequency_value_dataframe = frequency_dataframe[frequency_dataframe.columns[3:]].reset_index(drop=True)
        frequency_value_dataframe.columns = range(1, len(frequency_value_dataframe.columns) + 1)
        frequency_value_dataframe[frequency_value_dataframe.columns].plot(
            ax=axes,
            kind="box",
            title=valueAttribute.split("_")[-1],
        )

        if "freq" in valueAttribute:
            plt.ylim(bottom=-1)

    def analyze_frequency_3d_scatterplot(self, valueAttribute, x, y, color, freqNum):

        """ Render the original 3D frequency scatter plot. """

        frequency_dataframe = self._build_frequency_dataframe(valueAttribute)
        figure = plt.figure()
        axes = figure.add_subplot(111, projection="3d")
        scatter = axes.scatter(
            frequency_dataframe[x],
            frequency_dataframe[y],
            frequency_dataframe[f"{valueAttribute}_{freqNum}"],
            c=frequency_dataframe[color],
            cmap="jet",
        )
        axes.set_xlabel(x)
        axes.set_ylabel(y)
        axes.set_zlabel(f"{valueAttribute}_{freqNum}")
        axes.set_title("3D Scatterplot")
        plt.colorbar(scatter, label="Temperature", location="left")
        plt.show()

    def analyze_amplitude_3d_scatterplot(self, valueAttribute, x, y, color):

        """ Render the original 3D amplitude scatter plot. """

        amplitude_dataframe = self._build_amplitude_dataframe(valueAttribute)
        figure = plt.figure()
        axes = figure.add_subplot(111, projection="3d")
        scatter = axes.scatter(
            amplitude_dataframe[x],
            amplitude_dataframe[y],
            amplitude_dataframe[valueAttribute],
            c=amplitude_dataframe[color],
            cmap="jet",
        )
        axes.set_xlabel(x)
        axes.set_ylabel(y)
        axes.set_zlabel(valueAttribute)
        axes.set_title("3D Scatterplot")
        plt.colorbar(scatter, label="Temperature", location="left")
        plt.show()

    def analyze_3d_scatterplot(self, valueAttribute, x, y, color):

        """ Render the original 3D scatter plot for one scalar attribute. """

        scalar_dataframe = self._build_scalar_dataframe(valueAttribute)
        figure = plt.figure()
        axes = figure.add_subplot(111, projection="3d")
        scatter = axes.scatter(
            scalar_dataframe[x],
            scalar_dataframe[y],
            scalar_dataframe[valueAttribute],
            c=scalar_dataframe[color],
            cmap="jet",
        )
        axes.set_xlabel(x)
        axes.set_ylabel(y)
        axes.set_zlabel(valueAttribute)
        axes.set_title("3D Scatterplot")
        plt.colorbar(scatter, label="Temperature", location="left")
        plt.show()

    def analyze_scatterplot(self, valueAttribute, x, y):

        """ Keep the original scatter-plot helper unchanged in behavior. """

        import seaborn as sns

        scalar_dataframe = self._build_scalar_dataframe(valueAttribute)
        axes = sns.scatterplot(data=scalar_dataframe, x=x, y=y, hue=valueAttribute)
        axes.set_title(valueAttribute)
        sns.move_legend(axes, "upper left", bbox_to_anchor=(1, 1))
        plt.show()

    def analyze_heatmap(self, valueAttribute, x, y):

        """ Keep the original heatmap helper unchanged in behavior. """

        import seaborn as sns

        scalar_dataframe = self._build_scalar_dataframe(valueAttribute)
        scalar_dataframe = scalar_dataframe.pivot(index=y, columns=x, values=valueAttribute)
        axes = sns.heatmap(scalar_dataframe, cmap=sns.cm.rocket_r)
        axes.set_title(valueAttribute)
        plt.show()

    def analyze_fft_heatmap(self, valueAttribute, x, y):

        """ Keep the original FFT heatmap helper unchanged in behavior. """

        import seaborn as sns

        fft_dataframe = self._build_fft_max_dataframe(valueAttribute)
        fft_dataframe = fft_dataframe.pivot(index=y, columns=x, values=valueAttribute)
        axes = sns.heatmap(fft_dataframe, cmap=sns.cm.rocket_r)
        axes.set_title(valueAttribute)
        plt.show()

    def describe_and_boxplot(self, valueAttribute):

        """ Compute descriptive statistics and render the original boxplot. """

        scalar_dataframe = self._build_scalar_dataframe(valueAttribute)
        statistics_summary = scalar_dataframe[valueAttribute].describe()
        figure, axes = plt.subplots()
        axes.boxplot(scalar_dataframe[valueAttribute], vert=False)

        title = (
            f"{valueAttribute} -->"
            f"Stats: {statistics_summary['count']} values, mean={statistics_summary['mean']:.2f}, "
            f"std={statistics_summary['std']:.2f}, min={statistics_summary['min']:.2f}, "
            f"25%={statistics_summary['25%']:.2f}, 50%={statistics_summary['50%']:.2f}, "
            f"75%={statistics_summary['75%']:.2f}, max={statistics_summary['max']:.2f}"
        )
        print(title)
        axes.set_title(valueAttribute)
        plt.show()

    # Backward-Compatible Aliases Preserved For The Historical Helper Surface.
    _generateDf = _build_scalar_dataframe
    _generateDf_ftt = _build_fft_max_dataframe
    _generateDf_ampl = _build_amplitude_dataframe
    _generateDf_differentFreq = _build_frequency_dataframe
    _generateInstance = _load_or_create_instance
    read_all = read_all_instances
    convertNames = normalize_legacy_names
    read_all_fft = read_all_fft_instances
    genDfWithAmplEPhase = build_prediction_dataframe_with_amplitude_and_phase
    analisi_scatterplot3d_freq = analyze_frequency_3d_scatterplot
    analisi_scatterplot3d_ampl = analyze_amplitude_3d_scatterplot
    analisi_scatterplot3d = analyze_3d_scatterplot
    analisi_scatterplot = analyze_scatterplot
    analisi_heatmap = analyze_heatmap
    analisi_heatmap_fft = analyze_fft_heatmap
