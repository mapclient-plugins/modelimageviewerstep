'''
Created on Jun 18, 2015

@author: hsorby
'''
from PySide2 import QtCore, QtGui, QtWidgets

from mapclientplugins.modelimageviewerstep.view.ui_meshimagewidget import Ui_MeshImageWidget
from mapclientplugins.modelimageviewerstep.scene.meshimagescene import MeshImageScene

ANGLE_RANGE = 180


class MeshImageWidget(QtWidgets.QWidget):
    '''
    classdocs
    '''


    def __init__(self, model, parent=None):
        '''
        Constructor
        '''
        super(MeshImageWidget, self).__init__(parent)
        self._ui = Ui_MeshImageWidget()
        self._ui.setupUi(self)
        
        angle_initial_value = 0
        slider_range = [0, 2*ANGLE_RANGE]
        slider_initial_value = ANGLE_RANGE
        self._ui.lineEditAngle.setText(str(angle_initial_value))
        self._ui.horizontalSliderAngle.setMinimum(slider_range[0])
        self._ui.horizontalSliderAngle.setMaximum(slider_range[1])
        self._ui.horizontalSliderAngle.setValue(slider_initial_value)

        v = QtGui.QIntValidator(-ANGLE_RANGE, ANGLE_RANGE)
        self._ui.lineEditAngle.setValidator(v)
        self._ui.labelAngle.setText('Angle [{0}, {1}] (Degrees):'.format(-ANGLE_RANGE, ANGLE_RANGE))
        
        self._callback = None
       
        self._model = model
        self._scene = MeshImageScene(model)
        
        self._ui.widgetZinc.setContext(model.getContext())
        # self._ui.widgetZinc.setModel(model.getMarkerModel())
        # self._ui.widgetZinc.setPlaneAngle(angle_initial_value)
        # self._ui.widgetZinc.setSelectionfilter(model.getSelectionfilter())

        self._makeConnections()
        
    def _makeConnections(self):
        self._ui.pushButtonContinue.clicked.connect(self._continueExecution)
        self._ui.pushButtonViewAll.clicked.connect(self._viewAllButtonClicked)
        self._ui.horizontalSliderAngle.valueChanged.connect(self._angleSliderValueChanged)
        self._ui.widgetZinc.graphicsInitialized.connect(self._zincWidgetReady)
        self._ui.lineEditAngle.returnPressed.connect(self._angleLineEditTextEditFinished)
        self._ui.listWidget.itemChanged.connect(self._itemChanged)

    def getLandmarks(self):
        return self._model.getLandmarks()
        
    def setCoordinateDescription(self, coordinate_description):
        self._model.setCoordinateDescription(coordinate_description)
        
    def load_mesh(self, mesh):
        self._model.load_mesh(mesh)

    def load_images(self, images_dir):
        self._model.load_images(images_dir)

    def clear(self):
        self._model.clear()

    def initialise(self):
        self._model.initialise()
        self._scene.initialise()
        self._setupUi()
        
    def registerDoneExecution(self, done_exectution):
        self._callback = done_exectution

    def _setupUi(self):
        self._ui.listWidget.clear()
        region_names = self._model.getImageRegionNames()

        for region_name in region_names:
            item = QtGui.QListWidgetItem(self._ui.listWidget)
            item.setText(region_name)
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | item.flags())
            item.setCheckState(QtCore.Qt.Checked)

    def _itemChanged(self, item):
        region = item.text()
        self._model.setImageRegionVisibility(region, item.checkState() == QtCore.Qt.Checked)

    def _zincWidgetReady(self):
        pass
        # self._ui.widgetZinc.setSelectionfilter(self._model.getSelectionfilter())
        
    def _viewAllButtonClicked(self):
        self._ui.widgetZinc.viewAll()
        
    def _continueExecution(self):
        self._callback()
        
    def _angleSliderValueChanged(self, value):
        angle = value - ANGLE_RANGE
        self._ui.lineEditAngle.setText(str(angle))
        self._model.setRotationAngle(angle)

    def _angleLineEditTextEditFinished(self):
        angle = int(self._ui.lineEditAngle.text())
        self._ui.horizontalSliderAngle.setValue(angle + ANGLE_RANGE)
        self._model.setRotationAngle(angle)
