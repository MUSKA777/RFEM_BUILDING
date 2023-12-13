#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
#
# baseName = os.path.basename(__file__)
# dirName = os.path.dirname(__file__)
# sys.path.append(dirName + r'/../..')
from utils.skeleton import get_node_grid
from RFEM.initModel import Model, clearAttributes
from floor.first_floor import FirstFloor
from floor.second_floor import SecondFloor
from dataclasses import asdict
from utils.def_data_classes.base import AllBasicObjects



class MyModel:
    all_basic_objects = AllBasicObjects()

    def set_all_materials(self):
        for _material in asdict(self.all_basic_objects.all_materials).keys():
            def_material = getattr(self.all_basic_objects.all_materials, _material)
            create_material = getattr(def_material, "create_material")
            create_material()

    def set_all_thicknesses(self):
        for _thickness in asdict(self.all_basic_objects.all_thicknesses).keys():
            def_thickness = getattr(self.all_basic_objects.all_thicknesses, _thickness)
            create_thickness = getattr(def_thickness, "create_thickness")
            create_thickness()

    def set_all_sections(self):
        for _section in asdict(self.all_basic_objects.all_sections).keys():
            def_section = getattr(self.all_basic_objects.all_sections, _section)
            create_section = getattr(def_section, "create_section")
            create_section()

    def __call__(self, *args, **kwargs):

        get_node_grid(list_coordinates_x=[0, 5, 10, 15, 20, 25],
                      list_coordinates_y=[0, 4, 6.5, 11],
                      list_coordinates_z=[0, -3.34, -6.68],
                      all_nodes=self.all_basic_objects.all_nodes)
        self.set_all_materials()
        self.set_all_thicknesses()
        self.set_all_sections()

        first_floor = FirstFloor(all_basic_objects=self.all_basic_objects)
        first_floor()
        second_floor = SecondFloor(all_basic_objects=self.all_basic_objects)
        second_floor()


if __name__ == '__main__':
    Model(True, "MyModel", delete_all=True)
    Model.clientModel.service.begin_modification()

    my_model = MyModel()
    my_model()

    Model.clientModel.service.finish_modification()
