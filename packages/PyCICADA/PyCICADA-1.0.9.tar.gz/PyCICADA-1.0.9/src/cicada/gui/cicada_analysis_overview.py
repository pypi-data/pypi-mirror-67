from qtpy.QtWidgets import *
from qtpy.QtCore import Qt
import os
import platform
from qtpy import QtCore
from random import randint
from functools import partial
import subprocess
import sys


class AnalysisOverview(QWidget):
    """Class containing the overview linked to an analysis"""
    def __init__(self, config_handler, parent=None):
        QWidget.__init__(self, parent=parent)

        self.config_handler = config_handler
        self.special_background_on = False
        self.current_style_sheet_background = ".QWidget{background-image:url(\"\"); background-position: center;}"
        self.created_analysis_names = []
        self.created_analysis = []
        # Add the scroll bar
        # ==============================
        self.main_layout = QVBoxLayout()
        self.scrollArea = QScrollArea()
        # ScrollBarAlwaysOff = 1
        # ScrollBarAlwaysOn = 2
        # ScrollBarAsNeeded = 0
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.main_layout.addWidget(self.scrollArea)

        self.scroll_area_widget_contents = QWidget()
        self.scrollArea.setWidget(self.scroll_area_widget_contents)
        self.layout = QVBoxLayout(self.scroll_area_widget_contents)
        # we add strech now and we will insert new widget before the strech
        self.layout.addStretch(1)
        # ==============================
        self.setLayout(self.main_layout)

        if config_handler.main_window_bg_pictures_displayed_by_default:
            self.set_random_background_picture()

    def add_analysis_overview(self, cicada_analysis, analysis_id, obj):
        """
        Add widgets to track the corresponding analysis
        Args:
            cicada_analysis (CicadaAnalysis): CicadaAnalysis instance
            analysis_id (str): Randomly generated ID linked to the analysis
            obj (object): The analysis window's object itself

        """
        self.created_analysis_names.append(analysis_id + '_overview')

        setattr(self, analysis_id + '_overview', AnalysisState(analysis_id=obj, cicada_analysis=cicada_analysis,
                                                               parent=self.scroll_area_widget_contents))
        analysis_overview = getattr(self, analysis_id + '_overview')

        # self.layout.addWidget(analysis_overview)
        self.layout.insertLayout(self.layout.count() - 1, analysis_overview)
        # analysis_overview.setStyleSheet("background-color:transparent; border-radius: 20px;")
        setattr(self, 'hlayout_' + analysis_id, QHBoxLayout())
        h_layout = getattr(self, 'hlayout_' + analysis_id)
        # setattr(self, analysis_id + '_remaining_time_label', RemainingTime())
        # exec('self.' + analysis_id + '_remaining_time_label = RemainingTime()')
        setattr(self, analysis_id + '_progress_bar', QProgressBar())
        # exec('self.' + analysis_id + '_progress_bar = QProgressBar()')
        h_layout.addWidget(getattr(self, analysis_id + '_progress_bar'))
        setattr(self, analysis_id + '_button', ResultsButton(cicada_analysis=cicada_analysis))
        results_button = getattr(self, analysis_id + '_button')
        # eval('self.hlayout_' + analysis_id + '.addWidget(self.' + analysis_id + '_remaining_time_label)')
        self.layout.insertLayout(self.layout.count() - 1, h_layout)
        self.layout.insertLayout(self.layout.count() - 1, results_button)
        # self.layout.addLayout(h_layout)

    def set_random_background_picture(self):
        pic_path = self.config_handler.get_random_main_window_bg_picture(widget_id="overview")
        if pic_path is None:
            return
        self.current_style_sheet_background = ".QWidget{background-image:url(\"" + \
                                              pic_path + \
                                              "\"); background-position: center top; background-repeat:repeat-xy;}"
        self.scroll_area_widget_contents.setStyleSheet(self.current_style_sheet_background)  # no-repeat
        self.special_background_on = True

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_P:
            if self.special_background_on:
                self.current_style_sheet_background = ".QWidget{background-image:url(\"\"); background-position: center;}"
                self.scroll_area_widget_contents.setStyleSheet(self.current_style_sheet_background)
                self.special_background_on = False
            else:
                self.set_random_background_picture()


class AnalysisState(QHBoxLayout):
    """Class containing the name of the analysis and the subjects analysed"""
    def __init__(self, analysis_id, cicada_analysis, parent=None, without_bringing_to_front=False):
        """

        Args:
            analysis_id (QWidget): Corresponding analysis widget object
            cicada_analysis (CicadaAnalysis): Chosen analysis
            without_bringing_to_front (bool): If true remove the change of color for the QLabel when hover state
        """
        super().__init__(parent)

        self.q_scroll_bar = QScrollArea()
        # self.h_layout = QHBoxLayout()
        property_value = "True"
        if without_bringing_to_front:
            # this way we can remove the change of color for QLabel when hover state
            # and we can increase the max-height of the scrollbar
            property_value = "False"

        self.q_label_analysis_name = QLabel()
        self.q_label_analysis_name.setText(cicada_analysis.name)
        self.q_label_analysis_name.setAlignment(Qt.AlignCenter)
        # use for personnalized style-sheet
        self.q_label_analysis_name.setProperty("state", property_value)
        self.setProperty("state", "True")
        if not without_bringing_to_front:
            self.q_label_analysis_name.mouseDoubleClickEvent = partial(self.bring_to_front, analysis_id)
        self.addWidget(self.q_label_analysis_name)

        data_identifiers = "\n".join(cicada_analysis.get_data_identifiers())
        self.q_label_data_identifiers = QLabel()
        self.q_label_data_identifiers.setText(data_identifiers)
        self.q_label_data_identifiers.setAlignment(Qt.AlignCenter)
        # use for personnalized style-sheet
        self.q_label_data_identifiers.setProperty("state", property_value)
        self.q_scroll_bar.setProperty("state", property_value)

        if not without_bringing_to_front:
            self.q_label_data_identifiers.mouseDoubleClickEvent = partial(self.bring_to_front, analysis_id)

        # ScrollBarAlwaysOff = 1
        # ScrollBarAlwaysOn = 2
        # ScrollBarAsNeeded = 0
        self.q_scroll_bar.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        # self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.q_scroll_bar.setWidgetResizable(True)
        self.q_scroll_bar.setWidget(self.q_label_data_identifiers)

        self.addWidget(self.q_scroll_bar)
        # self.addStretch(1)

    def bring_to_front(self, window_id, event):
        """
        Bring corresponding analysis window to the front (re-routed from the double click method)

        Args:
            window_id (QWidget) : Analysis Widget object
            event (QEvent) : Double click event
        """
        window_id.setWindowState(window_id.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
        # For Windows/Linux
        window_id.activateWindow()
        # For Mac
        window_id.raise_()

    def deleteLater(self):
        """Re-implementation of the deleteLater method to properly delete the whole widget"""
        try:
            self.q_label_analysis_name.deleteLater()
            self.q_label_data_identifiers.deleteLater()
            self.q_scroll_bar.deleteLater()
        except RuntimeError:
            pass


class ResultsButton(QHBoxLayout):
    """Class containing the button to open the result folder"""
    def __init__(self, cicada_analysis):
        """
        Args:
            cicada_analysis (CicadaAnalysis): Chosen analysis
        """
        super().__init__()
        self.result_button = QPushButton()
        self.result_button.setEnabled(False)
        self.result_button.setText('Open results folder')
        self.result_path = cicada_analysis.get_results_path()
        self.addWidget(self.result_button)
        self.result_button.clicked.connect(self.open_explorer)

    def open_explorer(self):
        """Open the file explorer depending on the OS"""
        if self.result_path is None:
            pass
        else:
            if platform.system() == 'Darwin':
                subprocess.run(['open', '--', os.path.realpath(self.result_path)])
            elif platform.system() == 'Linux':
                # subprocess.run(['xdg-open', os.path.abspath(self.result_path)])
                subprocess.run(['xdg-open', self.result_path])
                # nautilus doesn't work
                # subprocess.run(['nautilus --browser', self.result_path])

            elif platform.system() == 'Windows':
                subprocess.run(['explorer', os.path.realpath(self.result_path)])

    def deleteLater(self):
        """Re-implementation of the deleteLater method to properly delete the widget"""
        try:
            self.result_button.deleteLater()
        except RuntimeError:
            pass
