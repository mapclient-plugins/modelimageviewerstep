from math import cos, sin, pi

from opencmiss.zinc.context import Context

from mapclientplugins.modelimageviewerstep.model.image import ImageModel
from opencmiss.utils.geometry.plane import ZincPlane
from opencmiss.utils.maths.algorithms import calculateExtents
from opencmiss.utils.maths.vectorops import mxvectormult
from opencmiss.utils.zinc import createFiniteElementField, createIsoScalarField, createVisibilityFieldForPlane,\
    defineStandardVisualisationTools, createNodes, createElements


class MeshImageModel(object):

    def __init__(self):
        self._coordinate_description = None
        self._file_location = None
        self._location = None
        self._context = Context("MeshImage")
        defineStandardVisualisationTools(self._context)

        self._image_model = ImageModel(self._context)
        # First create coordinate field
        self._elements = None
        self._nodes = None
        self._rotation_axis = [0, 1, 0]
        self._reference_normal = [0, 0, 1]
        self._region = self._context.getDefaultRegion()
        self._coordinate_field = createFiniteElementField(self._region)
        self._plane = self._setupDetectionPlane(self._region, self._coordinate_field)
        self._iso_scalar_field = createIsoScalarField(self._region, self._coordinate_field, self._plane)
        self._visibility_field = createVisibilityFieldForPlane(self._region, self._coordinate_field, self._plane)

    def load_mesh(self, mesh):
        self._nodes = mesh['points']
        self._elements = mesh['elements']
        self._createMesh(self._nodes, self._elements)
        extents = calculateExtents(self._nodes)
        mid_point = [(extents[1] + extents[0])/2.0, (extents[3] + extents[2])/2.0, (extents[5] + extents[4])/2.0]
        self._plane.setRotationPoint(mid_point)

    def load_images(self, images_dir):
        self._image_model.setImageData(images_dir)

    def clear(self):
        return
        self._image_model.clear()
        self._region = None

    def initialise(self):
        # return
        # self._region = self._context.createRegion()
        self._image_model.initialise(self._region)

    def getImageModel(self):
        return self._image_model

    def getContext(self):
        return self._context

    def getCoordinateField(self):
        return self._coordinate_field

    def getRegion(self):
        return self._region

    def getVisibilityField(self):
        return self._visibility_field

    def getImageRegionNames(self):
        return self._image_model.getRegionNames()

    def setImageRegionVisibility(self, region_name, state):
        self._image_model.setRegionVisibility(region_name, state)

    def getIsoScalarField(self):
        return self._iso_scalar_field

    def setRotationAngle(self, angle):
        c = cos(angle*pi/180.0)
        s = sin(angle*pi/180.0)
        C = 1 - c
        x = self._rotation_axis[0]
        y = self._rotation_axis[1]
        z = self._rotation_axis[2]

        Q = [[x*x*C+c,   x*y*C-z*c, x*z*C+y*s],
             [y*x*C+z*s, y*y*C+c,   y*z*C-x*s ],
             [z*x*C-y*s, z*y*C+x*s, z*z*C+c]]

        n = mxvectormult(Q, self._reference_normal)

        self._plane.setNormal(n)

    def _setupDetectionPlane(self, region, coordinate_field):
        '''
        Adds a single finite element to the region and keeps a handle to the
        fields created for the finite element in the following attributes(
        self-documenting names):
            '_coordinate_field'
            '_scale_field'
            '_scaled_coordinate_field'
            '_iso_scalar_field'
        '''
        fieldmodule = region.getFieldmodule()
        fieldmodule.beginChange()

        plane = ZincPlane(fieldmodule)

        fieldmodule.endChange()

        return plane

    def _createMesh(self, nodes, elements):
        """
        Create a mesh from data extracted from a VRML file.
        The nodes are given as a list of coordinates and the elements
        are given as a list of indexes into the node list..
        """
        # First create all the required nodes
        createNodes(self._coordinate_field, self._nodes)
        # then define elements using a list of node indexes
        createElements(self._coordinate_field, self._elements)
        # Define all faces also
        fieldmodule = self._coordinate_field.getFieldmodule()
        fieldmodule.defineAllFaces()

