
'''
MAP Client Plugin Step
'''
from PySide2 import QtGui

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint

from mapclientplugins.modelimageviewerstep.model.meshimagemodel import MeshImageModel
from mapclientplugins.modelimageviewerstep.view.meshimagewidget import MeshImageWidget


class ModelImageViewerStep(WorkflowStepMountPoint):
    '''
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    '''

    def __init__(self, location):
        super(ModelImageViewerStep, self).__init__('Model Image Viewer', location)
        self._configured = True  # A step cannot be executed until it has been configured.
        self._category = 'Model Viewer'
        # Add any other initialisation code here:
        self._icon = QtGui.QImage(':/modelimageviewerstep/images/model-viewer.png')
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#images'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#mesh_points_elements'))
        # Port data:
        self._portData0 = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#images
        self._portData1 = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#coordinate_description

        self._view = None

    def execute(self):
        '''
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        '''
        # Put your execute step code here before calling the '_doneExecution' method.
        if self._view is None:
            model = MeshImageModel()
            # model.setLocation(os.path.join(self._location, self._config['identifier']))
            self._view = MeshImageWidget(model)
            self._view.registerDoneExecution(self._doneExecution)
        else:
            self._view.clear()

        self._view.load_mesh(self._portData1)
        self._view.load_images(self._portData0)

        self._view.initialise()

        self._setCurrentWidget(self._view)

    def setPortData(self, index, dataIn):
        '''
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.
        '''
        if index == 0:
            self._portData0 = dataIn  # http://physiomeproject.org/workflow/1.0/rdf-schema#images
        elif index == 1:
            self._portData1 = dataIn  # http://physiomeproject.org/workflow/1.0/rdf-schema#coordinate_description

    def configure(self):
        '''
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        '''
        pass

    def getIdentifier(self):
        '''
        The identifier is a string that must be unique within a workflow.
        '''
        return 'ModelImageViewer'  # TODO: The string must be replaced with the step's unique identifier

    def setIdentifier(self, identifier):
        '''
        The framework will set the identifier for this step when it is loaded.
        '''
        pass  # TODO: Must actually set the step's identifier here

    def serialize(self):
        '''
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        '''
        pass

    def deserialize(self, string):
        '''
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.
        '''
        pass

