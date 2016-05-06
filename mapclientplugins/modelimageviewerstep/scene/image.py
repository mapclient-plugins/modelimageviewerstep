'''
Created on May 22, 2015

@author: hsorby
'''
from mapclientplugins.heartsurfacesegmenterstep.definitions import ELEMENT_OUTLINE_GRAPHIC_NAME,\
    IMAGE_PLANE_GRAPHIC_NAME
from opencmiss.zinc.glyph import Glyph
from opencmiss.zinc.field import Field

class ImageScene(object):
    '''
    classdocs
    '''


    def __init__(self, model):
        '''
        Constructor
        '''
        self._model = model
        self.clear()
        
    def initialise(self):
        self._setupVisualisation()
        
    def clear(self):
        self._outline = {}

    def _createTextureSurface(self, region, coordinate_field):
        scene = region.getScene()

        fm = region.getFieldmodule()
        xi = fm.findFieldByName('xi')
        scene.beginChange()
        # Create a surface graphic and set it's coordinate field
        # to the finite element coordinate field.
        graphic = scene.createGraphicsSurfaces()
        graphic.setCoordinateField(coordinate_field)
        graphic.setTextureCoordinateField(xi)
#         iso_graphic.setIsoscalarField(iso_scalar_field)
#         iso_graphic.setListIsovalues(0.0)
        graphic.setName(IMAGE_PLANE_GRAPHIC_NAME)

        scene.endChange()

        return graphic

    def _createOutline(self, region, finite_element_field):
        scene = region.getScene()

        scene.beginChange()
        # Create a surface graphic and set it's coordinate field
        # to the finite element coordinate field.
        outline = scene.createGraphicsLines()
        outline.setCoordinateField(finite_element_field)
        outline.setName(ELEMENT_OUTLINE_GRAPHIC_NAME)
        scene.endChange()
#         graphic = scene.createGraphicsPoints()
#         graphic.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
#         graphic.setCoordinateField(finite_element_field)
#         attributes = graphic.getGraphicspointattributes()
#         attributes.setGlyphShapeType(Glyph.SHAPE_TYPE_SPHERE)
#         attributes.setBaseSize([1.0])
#         surface = scene.createGraphicsSurfaces()
#         surface.setCoordinateField(finite_element_field)
        return outline

    def _setupVisualisation(self):
        images = self._model.getImages()
        for image in images:
            name = image.getName()
            region = image.getRegion()
            coordinate_field = image.getCoordinateField()
            material = image.getMaterial()
            self._outline[name] = self._createOutline(region, coordinate_field)
            self._image = self._createTextureSurface(region, coordinate_field)
            self._image.setMaterial(material)
