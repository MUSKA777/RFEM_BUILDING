#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
#
# baseName = os.path.basename(__file__)
# dirName = os.path.dirname(__file__)
# sys.path.append(dirName + r'/../..')
from utils.skeleton import get_node_grid
from utils.def_data_classes.node import AllNodes
from utils.def_data_classes.line import AllLines
from utils.def_data_classes.surface import AllSurfaces
from utils.def_data_classes.opening import AllOpening
from utils.def_data_classes.material import AllMaterial
from utils.def_data_classes.thickness import AllThicknesses
from utils.def_data_classes.section import AllSections
from utils.def_data_classes.member import AllMembers
from RFEM.initModel import Model
from floor.first_floor import FirstFloor
from floor.second_floor import SecondFloor
from dataclasses import asdict


class MyModel:
    all_nodes = AllNodes()
    all_lines = AllLines()
    all_surfaces = AllSurfaces()
    all_openings = AllOpening()
    all_materials = AllMaterial()
    all_thicknesses = AllThicknesses()
    all_sections = AllSections()
    all_members = AllMembers()

    def set_all_materials(self):
        for _material in asdict(self.all_materials).keys():
            def_material = getattr(self.all_materials, _material)
            create_material = getattr(def_material, "create_material")
            create_material()

    def set_all_thicknesses(self):
        for _thickness in asdict(self.all_thicknesses).keys():
            def_thickness = getattr(self.all_thicknesses, _thickness)
            create_thickness = getattr(def_thickness, "create_thickness")
            create_thickness()

    def set_all_sections(self):
        for _section in asdict(self.all_sections).keys():
            def_section = getattr(self.all_sections, _section)
            create_section = getattr(def_section, "create_section")
            create_section()

    def __call__(self, *args, **kwargs):

        get_node_grid(list_coordinates_x=[0, 5, 10, 15, 20, 25],
                      list_coordinates_y=[0, 4, 6.5, 11],
                      list_coordinates_z=[0, -3.34, -6.68],
                      all_nodes=self.all_nodes)
        self.set_all_materials()
        self.set_all_thicknesses()
        self.set_all_sections()

        first_floor = FirstFloor(all_nodes=self.all_nodes,
                                 all_lines=self.all_lines,
                                 all_surfaces=self.all_surfaces,
                                 all_opening=self.all_openings,
                                 all_material=self.all_materials,
                                 all_thicknesses=self.all_thicknesses,
                                 all_sections=self.all_sections,
                                 all_members=self.all_members)
        first_floor()
        second_floor = SecondFloor(all_nodes=self.all_nodes,
                                   all_lines=self.all_lines,
                                   all_surfaces=self.all_surfaces,
                                   all_opening=self.all_openings,
                                   all_material=self.all_materials,
                                   all_thicknesses=self.all_thicknesses,
                                   all_sections=self.all_sections,
                                   all_members=self.all_members)
        second_floor()


if __name__ == '__main__':
    Model(True, "MyModel")
    Model.clientModel.service.begin_modification()

    my_model = MyModel()
    my_model()

    Model.clientModel.service.finish_modification()
