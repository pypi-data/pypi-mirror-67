from qtpy.QtWidgets import *
from qtpy.QtCore import QAbstractItemModel, QModelIndex, Qt
from qtpy import QtCore, QtGui
from sortedcontainers import SortedDict
from cicada.preprocessing.utils import class_name_to_module_name, module_name_to_class_name
from cicada.gui.cicada_analysis_parameters_gui import AnalysisPackage
import importlib
import glob
import os
from time import time
import numpy as np

"""
Interesting exemples:
https://www.programcreek.com/python/example/101690/PyQt5.QtCore.Qt.CustomContextMenu
https://github.com/EternityForest/mdNotes/blob/master/pyscrapbook/__main__.py
https://stackoverflow.com/questions/45035515/qtreeview-change-icon-on-row-icon-click

"""


class TreeItem(object):
    def __init__(self, family_section=None, cicada_analysis=None, parent=None):
        """

        Args:
            family_section:
            cicada_analysis:
            parent:
        """
        self.parent_item = parent
        self.cicada_analysis = cicada_analysis
        self.family_section = family_section
        if self.cicada_analysis is None:
            if family_section is None:
                # then we define the header
                self.item_data = ("Analysis", "Description")
            else:
                self.item_data = (family_section, "")
        else:
            self.item_data = (self.cicada_analysis.name, self.cicada_analysis.short_description)
        self.child_items = []
        self.data_valid = False

    def set_data(self, data_to_analyse, data_format):
        """
        Set the data to analysis and filter the analysis that are possible on those data
        :param data_to_analyse:
        :param data_format:
        :return:
        """
        for child_item in self.child_items:
            child_item.set_data(data_to_analyse, data_format)
        if self.cicada_analysis is not None:
            # start_time = time()
            self.cicada_analysis.set_data(data_to_analyse, data_format)
            # time at 0.0s for all
            # stop_time = time()
            # print(f"Time set_data {self.cicada_analysis.name}: "
            #       f"{np.round(stop_time - start_time, 3)} s")
        self.check_data()

    def invalidate_all_items(self):
        """
        Invalidate all items
        Returns:

        """
        # print("invalidate_all_items")
        # TODO: find out why the items are not deactivated in the tree when this method is called
        for child_item in self.child_items:
            child_item.invalidate_all_items()

        self.data_valid = False

    def check_data(self):
        '''
        Check if the data to analyse if valid for a given analysis
        :param data_to_check:
        :param format_data:
        :return:
        '''
        # check if data is valid for at least one child
        one_child_ok = False
        for child_item in self.child_items:
            child_item.check_data()
            if child_item.data_valid:
                one_child_ok = True

        if self.cicada_analysis is None:
            if one_child_ok:
                self.data_valid = True
            else:
                self.data_valid = False
        else:
            # start_time = time()
            self.data_valid = self.cicada_analysis.check_data()
            # stop_time = time()
            # TODO: understand why: Time check_data DeepCINAC prediction: 2.414 s while is 0.0s otherwise
            # print(f"Time check_data {self.cicada_analysis.name}: "
            #       f"{np.round(stop_time - start_time, 3)} s")

    def append_child(self, item):
        # print("append_child")
        self.child_items.append(item)

    def child(self, row):
        return self.child_items[row]

    def child_count(self):
        return len(self.child_items)

    def column_count(self):
        return len(self.item_data)

    def data(self, column):
        try:
            # code that can be used to produce an icon
            # then a list should be return with icon and text
            # and then should be handled by the fct data() in QAnalysisTreeModel
            # item = QtGui.QStandardItem()
            # item.setData("titi", role=QtCore.Qt.UserRole)
            # icon_path = "cicada/gui/icons/like.svg"
            # # if os.path.isdir(path):
            # #     icon_path = DIR_ICON_PATH
            # icon = QtGui.QIcon(icon_path)
            # item.setText("toto")
            # item.setIcon(icon)
            # return icon
            return self.item_data[column]
        except IndexError:
            return None

    def parent(self):
        return self.parent_item

    def row(self):
        if self.parent_item:
            return self.parent_item.child_items.index(self)

        return 0


class QAnalysisTreeView(QTreeView):
    """

    """
    def __init__(self, tree_item, config_handler, parent=None):
        """

        Args:
            tree_item:
            parent:
        """
        QTreeView.__init__(self)
        self.config_handler = config_handler
        # in case we want to hide the header
        # self.setHeaderHidden(True)
        # same height for all the rows
        self.setUniformRowHeights(True)
        # not editable
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.horizontalScrollBar().setEnabled(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded) # ScrollBarAsNeeded
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.header().setStretchLastSection(True)

        self.tree_item = tree_item
        self.special_background_on = False

        if self.config_handler.main_window_bg_pictures_displayed_by_default:
            self.set_random_background_picture()

        # self.setAutoFillBackground(True)
        # self.setStyleSheet(
        #     "background-image:url(\"cicada/gui/icons/rc/sky_night.jpeg\"); background-position: center;")
        # palette = self.palette()
        # palette.setColor(self.backgroundRole(), Qt.black)
        # self.setPalette(palette)

        # w = QtGui.QLineEdit()
        # one way of changing the font
        # palette = self.palette()
        # palette.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
        # self.setPalette(palette)
        # font = QtGui.QFont("Times", 15, QtGui.QFont.Bold)
        # self.setFont(font)

        # in case to change the arrow
        # theItem.setChildIndicatorPolicy(QTreeWidgetItem.ShowIndicator)

    # used to draw the branches on the first column

    # def mouseDoubleClickEvent(self, event):
    #     # QMouseEvent
    #     print(f'mouseDoubleClickEvent {event}')

    def set_random_background_picture(self):
        pic_path = self.config_handler.get_random_main_window_bg_picture(widget_id="tree")
        if pic_path is None:
            return
        self.setStyleSheet(
            f"background-image:url(\"{pic_path}\"); "
            f"background-position: center top; "
            f"background-repeat: repeat-xy;")  # no-repeat
        self.special_background_on = True

    def keyPressEvent(self, event):
        """

        Args:
            event: P -> set background picture

        Returns:

        """
        # setting background picture
        if event.key() == QtCore.Qt.Key_P:
            if self.special_background_on:
                self.setStyleSheet(
                    "background-image:url(\"\"); background-position: center;")
                self.special_background_on = False
            else:
                self.set_random_background_picture()

    # def mouseMoveEvent(self, event):
    #     print("mouse")

    def drawBranches(self, painter, rect, index):
        QTreeView.drawBranches(self, painter, rect, index)
        # # print(f"drawBranches index {index.row()}")
        # print(f"internalPointer {index.internalPointer()}")
        # # instance of TreeItem
        # tree_item = index.internalPointer()
        # tree_model = index.model()
        #
        # if index.row() == 0:
        #     painter.fillRect(rect, Qt.black)
        # else:
        #     painter.fillRect(rect, Qt.black)
        # if tree_item.family_section is not None:
        #     icon_path = "cicada/gui/icons/like.svg"
        #     # icon = QtGui.QIcon(icon_path)
        #     pixmap = QtGui.QPixmap(icon_path)
        #     painter.drawPixmap(rect, pixmap) #, sourceRect=rect)
        # # else
        # #     painter->fillRect(rect, Qt.green)
        #
        # QTreeView.drawBranches(self, painter, rect, index)

    def isIndexHidden(self, q_model_index):
        """
        Avoid to select the line that display the family name
        :param q_model_index:
        :return:
        """

        # return QTreeView.isIndexHidden(self, q_model_index)
        tree_item = q_model_index.internalPointer()
        if tree_item.family_section is None:
            return not tree_item.data_valid
        else:
            return False

    # def setSelection(self, rect, command):
    #     print(f"command {command}")
    #     return


class QAnalysisTreeModel(QAbstractItemModel):
    """

    """
    def __init__(self, tree_item, parent=None):
        super(QAnalysisTreeModel, self).__init__(parent)

        self.rootItem = tree_item

    def columnCount(self, parent):
        if parent.isValid():
            return parent.internalPointer().column_count()
        else:
            return self.rootItem.column_count()

    def data(self, index, role):
        """

        :param index:
        :param role:
        :return:
        """
        """
        Different roles:
        The general purpose roles (and the associated types) are:

        Constant	Value	Description
        Qt::DisplayRole	0	The key data to be rendered in the form of text. (QString)
        Qt::DecorationRole	1	The data to be rendered as a decoration in the form of an icon. (QColor, QIcon or QPixmap)
        Qt::EditRole	2	The data in a form suitable for editing in an editor. (QString)
        Qt::ToolTipRole	3	The data displayed in the item's tooltip. (QString)
        Qt::StatusTipRole	4	The data displayed in the status bar. (QString)
        Qt::WhatsThisRole	5	The data displayed for the item in "What's This?" mode. (QString)
        Qt::SizeHintRole	13	The size hint for the item that will be supplied to views. (QSize)
        Roles describing appearance and meta data (with associated types):
        
        Constant	Value	Description
        Qt::FontRole	6	The font used for items rendered with the default delegate. (QFont)
        Qt::TextAlignmentRole	7	The alignment of the text for items rendered with the default delegate. (Qt::AlignmentFlag)
        Qt::BackgroundRole	8	The background brush used for items rendered with the default delegate. (QBrush)
        Qt::BackgroundColorRole	8	This role is obsolete. Use BackgroundRole instead.
        Qt::ForegroundRole	9	The foreground brush (text color, typically) used for items rendered with the default delegate. (QBrush)
        Qt::TextColorRole	9	This role is obsolete. Use ForegroundRole instead.
        Qt::CheckStateRole	10	This role is used to obtain the checked state of an item. (Qt::CheckState)
        Qt::InitialSortOrderRole	14	This role is used to obtain the initial sort order of a header view section. (Qt::SortOrder). This role was introduced in Qt 4.8.
        Accessibility roles (with associated types):
        
        Constant	Value	Description
        Qt::AccessibleTextRole	11	The text to be used by accessibility extensions and plugins, such as screen readers. (QString)
        Qt::AccessibleDescriptionRole	12	A description of the item for accessibility purposes. (QString)
        User roles:
        
        Constant	Value	Description
        Qt::UserRole	32	The first role that can be used for application-specific purposes.
        """
        if not index.isValid():
            return None
        # print(f"role {role}")
        # print(f"Qt.UserRole {Qt.UserRole}")
        if role == Qt.DecorationRole:
            item = index.internalPointer()
            return item.data(index.column())

        item = index.internalPointer()

        if (role == Qt.ToolTipRole) and (not item.data_valid):
            tree_item = index.internalPointer()
            if tree_item.family_section is None:
                if tree_item.cicada_analysis.invalid_data_help:
                    return tree_item.cicada_analysis.invalid_data_help

        if (role == Qt.ForegroundRole) and (not item.data_valid):
            color = QtGui.QColor()
            # light-dark gray for non active items
            color.setRgb(150, 150, 150)
            return QtGui.QBrush(color)

        if role == Qt.ForegroundRole:
            tree_item = index.internalPointer()
            if tree_item.family_section is not None:
                # changing the foreground color of family section
                color = QtGui.QColor()
                color.setRgb(43,140,190) # 255, 0, 0 red
                return QtGui.QBrush(color)

        if role != Qt.DisplayRole:
            return None

        # print(f"role {role} {Qt.DecorationRole}")

        return item.data(index.column())

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags

        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.rootItem.data(section)

        return None

    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parent_item = self.rootItem
        else:
            parent_item = parent.internalPointer()

        child_item = parent_item.child(row)
        if child_item:
            return self.createIndex(row, column, child_item)
        else:
            return QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()

        child_item = index.internalPointer()
        parent_item = child_item.parent()

        if parent_item == self.rootItem:
            return QModelIndex()

        return self.createIndex(parent_item.row(), 0, parent_item)

    def rowCount(self, parent):
        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parent_item = self.rootItem
        else:
            parent_item = parent.internalPointer()

        return parent_item.child_count()


class AnalysisTreeApp(QWidget):
    """

    """
    def __init__(self, parent, config_handler, to_parameters_button=None):
        """

        Args:
            to_parameters_button: QButton that when clicked, will open the window with the widgets
            allowing the user to fill the parameters of the selected analysis
        """
        super().__init__()
        self.config_handler = config_handler
        self.dataView = None
        self.analysis_tree_model = None
        self.parent = parent
        self.created_analysis_package_object = []

        # used in self.doubleClickedItem()
        self.copied_data = None

        # will be initialized when the param section will have been created
        self.analysis_overview = None

        self.init_ui()
        to_parameters_button.clicked.connect(self.load_arguments_parameters_section)

        screen_geometry = QApplication.desktop().screenGeometry()
        # making sure the window is not bigger than the dimension of the screen
        width_window = min(550, screen_geometry.width() / 1.5)
        self.setMinimumSize(width_window, self.height())
        self.setProperty("tree", "True")
        # self.resize(width_window, self.height())

    def invalidate_all_items(self):
        """
        invalidate all items if the tree
        Returns:

        """

        self.analysis_tree_model.rootItem.invalidate_all_items()

    def set_data(self, data_to_analyse, data_format):
        """
        Give to the tree the data that the analysis classes will be given to analyze.
        Allows the tree to inactivate the analyses for which the data don't fulfill the requierements
        Args:
            data_to_analyse: a list of data in a given format (could be nwb or other)
            data_format: format of the data, must be a string. So far only "nwb" is supported

        Returns: None

        """
        # start_time = time()
        self.analysis_tree_model.rootItem.set_data(data_to_analyse, data_format)
        # stop_time = time()
        # print(f"Time set_data AnalysisTreeApp: "
        #       f"{np.round(stop_time - start_time, 3)} s")

    def doubleClickedItem(self, idx):
        """
        Method called when the user double click in the tree
        Args:
            idx: Index of the branch clicked

        Returns:

        """
        if not idx.isValid():
            return
        # idx is an instance of PyQt5.QtCore.QModelIndex

        # getting the TreeItem that has been double-clicked
        tree_item = idx.internalPointer()
        if tree_item.family_section is not None:
            # means the user clicked on the family name
            return

        if tree_item.cicada_analysis is not None and tree_item.data_valid:
            # Copy the object so each analysis has its own object
            self.copied_data = tree_item.cicada_analysis.copy()
            self.copied_data.set_arguments_for_gui()
            # using the id of the object instead, so no chance to have a double, adding 'a' so the variable don't start
            # by a numerical value
            random_id = "a" + str(id(self.copied_data))
            # Create analysis window
            analysis_package = AnalysisPackage(cicada_analysis=self.copied_data,
                                               analysis_name=str(tree_item.item_data[0]),
                                               name=random_id, main_window=self.parent, parent=self,
                                               config_handler=self.config_handler)
            setattr(self, random_id, analysis_package)
            self.created_analysis_package_object.append(analysis_package)
            self.parent.object_created.append(analysis_package)

            self.analysis_overview.add_analysis_overview(self.copied_data, random_id,
                                                         getattr(self, random_id))

    def load_arguments_parameters_section(self):
        """
        Used to load the parameters section with widgets, based on the current selection in the tree.
        If the selection is not on any valid tree item, nothing will happen
        Returns: None

        """
        q_model_index = self.dataView.currentIndex()
        self.doubleClickedItem(q_model_index)

    def init_ui(self):
        """
        Set some of the elements used to build the tree
        Returns:

        """
        self.analysis_tree_model = self.create_tree_model()

        self.dataView = QAnalysisTreeView(tree_item=self.analysis_tree_model.rootItem,
                                          config_handler=self.config_handler)
        # self.dataView.setRootIsDecorated(False)
        self.dataView.setAlternatingRowColors(False)
        self.dataView.doubleClicked.connect(self.doubleClickedItem)

        mainLayout = QVBoxLayout()
        # self.scrollArea = QScrollArea()
        # # ScrollBarAlwaysOff = 1
        # # ScrollBarAlwaysOn = 2
        # # ScrollBarAsNeeded = 0
        # self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        # self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        # self.scrollArea.setWidgetResizable(True)
        # mainLayout.addWidget(self.scrollArea)
        #
        # self.scroll_area_widget_contents = QWidget()
        # self.scrollArea.setWidget(self.scroll_area_widget_contents)
        # self.layout = QVBoxLayout(self.scroll_area_widget_contents)
        # self.layout.addWidget(self.dataView)

        mainLayout.addWidget(self.dataView)

        self.dataView.setModel(self.analysis_tree_model)

        # we expand all by default
        self.dataView.expandAll()
        # put the right size for the first & 2nd column (Analysis - Description)
        self.dataView.resizeColumnToContents(0)
        self.dataView.resizeColumnToContents(1)
        # resize the column when expending
        self.dataView.expanded.connect(lambda x: self.dataView.resizeColumnToContents(0))
        self.dataView.clicked.connect(lambda x: self.dataView.resizeColumnToContents(0))
        self.dataView.expanded.connect(lambda x: self.dataView.resizeColumnToContents(1))
        self.dataView.clicked.connect(lambda x: self.dataView.resizeColumnToContents(1))

        # opacity_effect = QGraphicsOpacityEffect()
        # opacity_effect.setOpacity(0.1)
        # self.setGraphicsEffect(opacity_effect)

        self.setLayout(mainLayout)

        self.show()

    # TODO: Create a function in order to update the tree after initialization with new analyses
    def create_tree_model(self):
        """
        Create the tree model
        Returns: the tree model, an instance of QAnalysisTreeModel

        """
        # TODO: a system that either read a yaml file or a dir and load automatically analysis function
        # TODO: don't load classed if the method get_params_for_gui return None ?
        # https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path

        modules = glob.glob(os.path.join(os.path.dirname(__file__), "..", "analysis", "ci_analyses", "*.py"))
        all_modules = [os.path.basename(f)[:-3] for f in modules if os.path.isfile(f) and not f.startswith(".")
                       and not f.endswith('__init__.py')]
        all_classes = [module_name_to_class_name(m) for m in all_modules]

        # module_name_to_class_name(module_name)
        analysis_instances = []
        for class_index, class_name in enumerate(all_classes):
            # module_name = class_name_to_module_name(class_name=class_name)
            module_name = all_modules[class_index]
            module_imported = importlib.import_module("cicada.analysis.ci_analyses." + module_name)
            class_instance = getattr(module_imported, class_name)
            # class_instance = getattr(test_cicada_test_paul, class_name)
            analysis_instances.append(class_instance(config_handler=self.config_handler))

        # it's a dict that contains other dicts.
        # dict key represents the name of the family. Instances in the dict with "zzz" are the ones
        # with no family
        # dict values is a list containing either dict (new family) or instances of CicadaAnalysis
        tree_family_dict = SortedDict()
        for analysis_instance in analysis_instances:
            family_ids = analysis_instance.family_id
            if family_ids is None:
                # "zzz" represents the instances without family
                if "zzz" not in tree_family_dict:
                    tree_family_dict["zzz"] = []
                tree_family_dict["zzz"].append(analysis_instance)
                continue

            if isinstance(family_ids, str):
                if family_ids not in tree_family_dict:
                    tree_family_dict[family_ids] = []
                tree_family_dict[family_ids].append(analysis_instance)
                continue

            # otherwise it's a list representing the a hierarchy
            dict_to_fill = tree_family_dict
            for index, family_id in enumerate(family_ids):
                if family_id not in dict_to_fill:
                    dict_to_fill[family_id] = []
                if index == len(family_ids) - 1:
                    dict_to_fill[family_id].append(analysis_instance)
                else:
                    # first we search if there is not already a dict with next family_id on it
                    for element in dict_to_fill[family_id]:
                        if isinstance(element, dict):
                            if family_ids[index + 1] in element:
                                dict_to_fill = element
                                continue
                    new_dict = dict()
                    dict_to_fill[family_id].append(new_dict)
                    dict_to_fill = new_dict

        root_tree = TreeItem()
        fill_tree_item_with_dict(root_tree, tree_family_dict)
        # temporary, will be called by set_data one the first part of GUI will be ready
        # root_tree.check_data()

        model = QAnalysisTreeModel(tree_item=root_tree)
        return model


def fill_tree_item_with_dict(root_tree, instances_dict):
    """
    Recursive function that fills the root_tree according to data in instances_dict.
    :param root_tree: instance of TreeItem
    :param instances_dict: Contains instance of cicada_analysis, in a hierarchy similar to the one we want
    the tree to be
    :return:
    """
    for key, value in instances_dict.items():
        if key == "zzz":
            # value is a list of CicadaAnalysis instance
            for analysis_instance in value:
                analysis_tree = TreeItem(cicada_analysis=analysis_instance, parent=root_tree)
                root_tree.append_child(analysis_tree)
            continue
        family_title_tree = TreeItem(family_section=key, parent=root_tree)
        root_tree.append_child(family_title_tree)
        # value is a list of dict or instance of CicadaAnalysis
        analysis_to_add = []
        for element in value:
            if isinstance(element, dict):
                fill_tree_item_with_dict(family_title_tree, element)
            else:
                analysis_to_add.append(element)

        for analysis_instance in analysis_to_add:
            analysis_tree = TreeItem(cicada_analysis=analysis_instance, parent=family_title_tree)
            family_title_tree.append_child(analysis_tree)
