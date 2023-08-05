from cicada.analysis.cicada_analysis import CicadaAnalysis
from cicada.utils.misc import get_continous_time_periods, get_yang_frames, from_timestamps_to_frame_epochs
from cicada.utils.pairwise_correlation_analysis import compute_similarity_matrix, plot_similarity_matrix
import numpy as np


class CicadaAnalysisPairwiseSimilarity(CicadaAnalysis):
    def __init__(self, config_handler=None):
        """
        """
        CicadaAnalysis.__init__(self, name="Pairwise similarity", family_id="Descriptive statistics",
                                short_description="Evaluate and show pairwise similarity",
                                config_handler=config_handler)

    def check_data(self):
        """
        Check the data given one initiating the class and return True if the data given allows the analysis
        implemented, False otherwise.
        :return: a boolean
        """
        super().check_data()

        # self.invalid_data_help = "Not implemented yet"
        # return False

        if self._data_format != "nwb":
            self.invalid_data_help = "Non NWB format compatibility not yet implemented"
            return False

        for data_to_analyse in self._data_to_analyse:
            roi_response_series = data_to_analyse.get_roi_response_series()
            if len(roi_response_series) == 0:
                self.invalid_data_help = f"No roi response series available in " \
                                         f"{data_to_analyse.identifier}"
                return False

        return True

    def set_arguments_for_gui(self):
        """

        Returns:

        """
        CicadaAnalysis.set_arguments_for_gui(self)

        self.add_roi_response_series_arg_for_gui(short_description="Neuronal activity to use", long_description=None)

        data_avalaible = ["Suite2p deconvolution", "Traces", "Rasterdur", "Raster"]
        self.add_choices_arg_for_gui(arg_name="data_to_use", choices=data_avalaible,
                                     default_value="Rasterdur",
                                     short_description="Data to use to compute pairwise similarity measures",
                                     multiple_choices=False,
                                     family_widget="figure_config_data_to_use")

        # TODO: implement something with connectivity (to see the cell that have similar connectivity)
        similarity_metrics = ["Pearson", "Hamming", "Jacquard"]
        self.add_choices_arg_for_gui(arg_name="similarity_metric", choices=similarity_metrics,
                                     default_value="Jacquard",
                                     short_description="Metric to use to build the pairwise similarity matrix",
                                     multiple_choices=False,
                                     family_widget="figure_config_metric_to_use")

        possibilities = ['full_recording', 'one_by_epoch']
        self.add_choices_arg_for_gui(arg_name="epochs_to_use", choices=possibilities,
                                     default_value="all_recording",
                                     short_description="Compute one similarity matrix over the full recording or one by epoch",
                                     multiple_choices=False,
                                     family_widget="epochs")

        all_epochs = []
        for data_to_analyse in self._data_to_analyse:
            all_epochs.extend(data_to_analyse.get_behavioral_epochs_names())
        all_epochs = list(np.unique(all_epochs))
        self.add_choices_for_groups_for_gui(arg_name="epochs_names", choices=all_epochs,
                                            with_color=True,
                                            mandatory=False,
                                            short_description="Behaviors to group: build one similarity matrix per epoch",
                                            long_description="Here you need to specify which individual behaviors "
                                                             "belong to the same group",
                                            family_widget="epochs")

        self.add_bool_option_for_gui(arg_name="specify_twitches_duration", true_by_default=False,
                                     short_description="Arbitrary set twitch duration",
                                     family_widget="epochs")

        self.add_int_values_arg_for_gui(arg_name="twitches_duration", min_value=100, max_value=1500,
                                        short_description="Duration after twitch to define 'twitch-related' activity (ms)",
                                        default_value=1000, family_widget="epochs")

    def update_original_data(self):
        """
        To be called if the data to analyse should be updated after the analysis has been run.
        :return: boolean: return True if the data has been modified
        """
        pass

    def run_analysis(self, **kwargs):
        """
        test
        :param kwargs:
          segmentation

        :return:
        """
        CicadaAnalysis.run_analysis(self, **kwargs)

        verbose = True

        roi_response_series_dict = kwargs["roi_response_series"]

        data_to_use = kwargs.get("data_to_use")

        similarity_metric = kwargs.get("similarity_metric")

        epochs_to_use = kwargs.get("epochs_to_use")

        epoch_groups = kwargs.get("epochs_names")

        specify_twitches_duration = kwargs.get("specify_twitches_duration")

        path_results = self.get_results_path()

        print("Description of pairwise similarity: coming soon...")

        n_sessions = len(self._data_to_analyse)
        n_sessions_to_use = n_sessions
        if verbose:
            print(f"{n_sessions} sessions to analyse")

        for session_index, session_data in enumerate(self._data_to_analyse):
            # Get Session Info
            session_identifier = session_data.identifier
            animal_id = session_data.subject_id
            animal_age = int(session_data.age)
            animal_weight = session_data.weight

            if verbose:
                print(f"------------------ ONGOING SESSION: {session_identifier} -------------------- ")

            # Get Data
            if isinstance(roi_response_series_dict, dict):
                roi_response_serie_info = roi_response_series_dict[session_identifier]
            else:
                roi_response_serie_info = roi_response_series_dict

            # Get Data Timestamps
            neuronal_data_timestamps = session_data.get_roi_response_serie_timestamps(keys=roi_response_serie_info)
            duration_s = neuronal_data_timestamps[len(neuronal_data_timestamps) - 1] - neuronal_data_timestamps[0]
            duration_m = duration_s / 60
            if verbose:
                print(f"Acquisition last for : {duration_s} seconds // {duration_m} minutes ")

            # Get Neuronal Data
            neuronal_data = session_data.get_roi_response_serie_data(keys=roi_response_serie_info)
            raster_dur = neuronal_data
            [n_cells, n_frames] = raster_dur.shape
            raster = np.zeros((n_cells, n_frames))
            for cell in range(n_cells):
                tmp_tple = get_continous_time_periods(raster_dur[cell, :])
                for tple in range(len(tmp_tple)):
                    onset = tmp_tple[tple][0]
                    raster[cell, onset] = 1

            # Get cells that spikes at least once
            sum_spikes = np.sum(raster, axis=1)
            active_cells = np.where(sum_spikes >= 1)[0]
            no_active_cells = n_cells - len(active_cells)

            if verbose:
                print(f"N cells: {n_cells}, N frames: {n_frames}")

            # Get the traces and Z-score
            trace_neuronal_data = session_data.get_roi_response_serie_data_by_keyword(keys=roi_response_serie_info[:-1],
                                                                                      keyword="trace")
            for key, data in trace_neuronal_data.items():
                traces = trace_neuronal_data.get(key)
            for trace_index, trace in enumerate(traces):
                traces[trace_index] = (trace - np.mean(trace)) / np.std(trace)

            # Get Cell-type Data and build cell-type list
            cell_indices_by_cell_type = session_data.get_cell_indices_by_cell_type(roi_serie_keys=
                                                                                   roi_response_serie_info)
            cell_type_list = []
            for cell in range(n_cells):
                cell_type_list.append("Unclassified")

            for key, info in cell_indices_by_cell_type.items():
                cell_type = key.capitalize()
                indexes = cell_indices_by_cell_type.get(key)
                tmp_n_cell = len(indexes)
                for cell in range(tmp_n_cell):
                    tmp_ind = indexes[cell]
                    cell_type_list[tmp_ind] = cell_type

            # Select data to use and keep only active cells for rasters
            if data_to_use == "Suite2p deconvolution":
                pass
            if data_to_use == "Traces":
                data = traces
            if data_to_use == "Rasterdur":
                data = raster_dur
                data = data[active_cells, :]
                if verbose:
                    print(f"Remove {no_active_cells} cells without spikes in the recording")
            if data_to_use == "Raster":
                data = raster
                data = data[active_cells, :]
                if verbose:
                    print(f"Remove {no_active_cells} cells without spikes in the recording")

            # Get the sampling rate and number of frames to consider after twitches
            sampling_rate = session_data.get_ci_movie_sampling_rate(only_2_photons=True)
            twitches_duration = kwargs.get("twitches_duration")
            twitches_duration = twitches_duration / 1000
            frames_delay = int(np.round(twitches_duration * sampling_rate))

            # Filter data based on the epochs: get the frames included in each epoch
            data_for_epoch = dict()
            active_frames = []
            group_names = []
            for epoch_group_name, epoch_info in epoch_groups.items():
                if len(epoch_info) != 2:
                    continue
                group_names.append(epoch_group_name)

                # Check whether this main epoch is the one of twitches
                name_to_check = epoch_group_name.lower()
                twitches_group = False
                if name_to_check.find('twi') != -1:
                    twitches_group = True

                epochs_names_in_group = epoch_info[0]

                # Loop on all the epochs included in the main epoch
                epochs_frames_in_group = []
                for epoch_name in epochs_names_in_group:
                    # looking in behavior or intervals
                    epochs_timestamps = session_data.get_interval_times(interval_name=epoch_name)
                    if epochs_timestamps is None:
                        epochs_timestamps = session_data.get_behavioral_epochs_times(epoch_name=epoch_name)
                    if epochs_timestamps is None:
                        # means this session doesn't have this epoch name
                        continue
                    # now we want to get the intervals time_stamps and convert them in frames
                    intervals_frames = from_timestamps_to_frame_epochs(time_stamps_array=epochs_timestamps,
                                                                       frames_timestamps=neuronal_data_timestamps,
                                                                       as_list=True)
                    epochs_frames_in_group.extend(intervals_frames)
                active_frames.extend(epochs_frames_in_group)

                n_periods = len(epochs_frames_in_group)
                frames_to_take = []
                for event in range(n_periods):
                    start = epochs_frames_in_group[event][0]
                    if twitches_group is True and specify_twitches_duration is True:
                        end = epochs_frames_in_group[event][0] + frames_delay
                    else:
                        end = epochs_frames_in_group[event][1]
                    frames_to_take.extend(np.arange(start, end + 1))

                data_epoch = data[:, frames_to_take]
                sum_spikes_epoch = np.sum(data_epoch, axis=1)
                epoch_active_cells = np.where(sum_spikes_epoch)[0]
                epoch_no_active_cells = np.where(sum_spikes_epoch == 0)[0]
                if verbose:
                    print(f"Remove {len(epoch_no_active_cells)} cells with no spikes in '{epoch_group_name}' epoch")
                data_to_take = data[:, frames_to_take]
                data_to_take = data_to_take[epoch_active_cells, :]
                data_for_epoch[epoch_group_name] = data_to_take

            group_names.append('rest')
            rest_frames = get_yang_frames(total_frames=n_frames, yin_frames=active_frames)[1]
            rest_data = data[:, rest_frames]
            sum_spikes_rest = np.sum(rest_data, axis=1)
            rest_active_cells = np.where(sum_spikes_rest)[0]
            rest_no_active_cells = np.where(sum_spikes_rest == 0)[0]
            rest_data = rest_data[rest_active_cells, :]
            if verbose:
                print(f"Remove {len(rest_no_active_cells)} cells with no spikes in 'rest' epoch")
            data_for_epoch['rest'] = rest_data

            # Check compatibility between data to use and similarity metric
            if data_to_use in ["Suite2p deconvolution", "Traces"] and similarity_metric in ["Hamming", "Jacquard"]:
                if verbose:
                    print(f"Data from: {data_to_use} is not compatible with similarity from {similarity_metric}")
                    print(f"Use Pearson correlation as default metric")
                similarity_metric = "Pearson"

            # Compute similarity matrix: Use full recording or compute one for each specified epoch
            if epochs_to_use == 'full_recording':
                data_to_use = data
                similarity_matrix = compute_similarity_matrix(neuronal_data=data_to_use, method=similarity_metric,
                                                              verbose=verbose)
            else:
                similarity_matrix_dict = dict()
                for index, name in enumerate(group_names):
                    if verbose:
                        print(f"Working on epoch: {name}")
                    data_to_use = data_for_epoch.get(name)
                    similarity_matrix = compute_similarity_matrix(neuronal_data=data_to_use, method=similarity_metric,
                                                                  verbose=verbose)
                    similarity_matrix_dict[name] = similarity_matrix

            # Do some plotings
            if verbose:
                print(f"Do the plots")
            if epochs_to_use == 'full_recording':
                plot_similarity_matrix(data=similarity_matrix, filename="test", background_color="black",
                                       size_fig=(5, 5),
                                       save_figure=True, path_results=path_results, save_formats="pdf",
                                       with_timestamp_in_file_name=False)
            else:
                plot_similarity_matrix(data=similarity_matrix_dict,  filename="test", background_color="black",
                                       size_fig=(5, 5),
                                       save_figure=True, path_results=path_results, save_formats="pdf",
                                       with_timestamp_in_file_name=False)




