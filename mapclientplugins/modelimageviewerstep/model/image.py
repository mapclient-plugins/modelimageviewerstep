'''
Created on May 21, 2015

@author: hsorby
'''
import os
import re

from opencmiss.zinc.field import Field
from opencmiss.zinc.status import OK

from opencmiss.utils.image import extractImageCorners
from opencmiss.utils.zinc import createFiniteElementField, \
    create2DFiniteElement
from opencmiss.utils.maths.algorithms import calculatePlaneNormal

IMAGE_AXIS_DEFAULT = 1


class ImageModel(object):
    '''
    classdocs
    '''

    def __init__(self, context):
        '''
        Constructor
        '''
        self._context = context
        self.clear()

    def getContext(self):
        return self._context

    def clear(self):
        self._image_data = {}
        self._images = []

    def initialise(self, region):
        self._createImageRegion(region)
        self._computeImages(IMAGE_AXIS_DEFAULT)

    def setImageData(self, image_data, axis=IMAGE_AXIS_DEFAULT):
        self._image_data[axis] = image_data

    def getImages(self):
        return self._images

    def getPlane(self, region):
        regions = [image.getRegion() for image in self._images]
        plane_point = None
        plane_normal = None
        if region in regions:
            fieldmodule = region.getFieldmodule()
            fieldcache = fieldmodule.createFieldcache()
            coordinate_field = fieldmodule.findFieldByName('coordinates')
            nodeset = fieldmodule.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_NODES)
            nodesetiterator = nodeset.createNodeiterator()

            node = nodesetiterator.next()
            locations = []
            count = 0
            while node.isValid() and count < 3:
                fieldcache.setNode(node)
                result, location = coordinate_field.evaluateReal(fieldcache, 3)
                if result == OK:
                    locations.append(location)
                node = nodesetiterator.next()
                count += 1

            if len(locations) == 3:
                plane_point = locations[0]
                plane_normal = calculatePlaneNormal(locations[0], locations[1], locations[2])

        return plane_point, plane_normal

    def getRegionNames(self):
        return [image.getRegion().getName() for image in self._images]

    def setRegionVisibility(self, region_name, state):
        region_names = self.getRegionNames()
        if region_name in region_names:
            index = region_names.index(region_name)
            self._images[index].setVisibility(state)

    def _computeImages(self, axis):
        directory = self._image_data[axis].location()
        files = os.listdir(directory)
        files.sort(key=alphanum_key)
        files = [image_file for image_file in files if image_file not in ['.hg', '.git', 'annotation.rdf']]
        # Assuming these images are DICOMs
        im_count = 0
        for filename in files:
            im_count += 1
            region = self._region.findChildByName('IM_{0:03d}'.format(im_count))
            if not region.isValid():
                region = self._region.createChild('IM_{0:03d}'.format(im_count))

            self._images.append(ImageTexture(self, directory, filename, region))

    def _createImageRegion(self, region):
        """
        Creates a child region of the root region called 'image'.  Stores
        a handle to the region in the class attribute '_region'.
        """
        self._region = region.createChild('image_region')


class ImageTexture(object):

    def __init__(self, parent, directory, filename, region):
        self._parent = parent
        self._name = region.getName()
        self._region = region

        fieldmodule = region.getFieldmodule()
        self._coordinate_field = createFiniteElementField(region)
        corners = extractImageCorners(directory, filename)
        print('corners', corners)
        create2DFiniteElement(fieldmodule, self._coordinate_field, corners)
        self._image_field = self._createImageField(fieldmodule, os.path.join(directory, filename))
        self._material = self._createMaterialUsingImageField(self._image_field)

    def _createMaterialUsingImageField(self, image_field):
        ''' 
        Use an image field in a material to create an OpenGL texture.  Returns the
        created material.
        '''
        # create a graphics material from the graphics module, assign it a name
        # and set flag to true
        materials_module = self._parent.getContext().getMaterialmodule()
        material = materials_module.createMaterial()

        spectrummodule = self._parent.getContext().getSpectrummodule()
        spectrum = spectrummodule.createSpectrum()
        component = spectrum.createSpectrumcomponent()
        component.setColourMappingType(component.COLOUR_MAPPING_TYPE_MONOCHROME)
        component.setRangeMinimum(0)
        component.setRangeMaximum(1)
        material.setTextureField(1, image_field)

        return material

    def _createImageField(self, fieldmodule, absolute_filename):
        image_field = fieldmodule.createFieldImage()
        image_field.setName('image_field')
        image_field.setFilterMode(image_field.FILTER_MODE_LINEAR)

        # Create a stream information object that we can use to read the
        # image file from disk
        stream_information = image_field.createStreaminformationImage()

        # We are reading in a file from the local disk so our resource is a file.
        if os.path.isfile(absolute_filename):
            # SWIG cannot handle unicode strings or rather the Zinc interface
            # files cannot handle unicode strings so we convert them to ascii
            # here.
            # if isinstance(absolute_filename, unicode):
            #     absolute_filename = absolute_filename.encode('ascii', 'ignore')
            stream_information.createStreamresourceFile(absolute_filename)

        # Actually read in the image file into the image field.
        image_field.read(stream_information)

        return image_field

    def getCoordinateField(self):
        return self._coordinate_field

    def getRegion(self):
        return self._region

    def getName(self):
        return self._name

    def getMaterial(self):
        return self._material

    def setVisibility(self, state):
        self._region.getScene().setVisibilityFlag(state)

    def free(self):
        fieldmodule = self._region.getFieldmodule()
        for dimension in [3, 2, 1]:
            mesh = fieldmodule.findMeshByDimension(dimension)
            mesh.destroyAllElements()
        nodeset = fieldmodule.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_NODES)
        nodeset.destroyAllNodes()
        it = fieldmodule.createFielditerator()
        field = it.next()
        while field.isValid():
            if field.isManaged():
                field.setManaged(False)
                # must reset iterator
                it = fieldmodule.createFielditerator()
            field = it.next()

        self._region = None
        self._coordinate_field = None
        self._image_field = None
        self._material = None


def tryint(s):
    try:
        return int(s)
    except:
        return s


def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
    "z23a" -> ["z", 23, "a"]
    """
    return [tryint(c) for c in re.split('([0-9]+)', s)]
