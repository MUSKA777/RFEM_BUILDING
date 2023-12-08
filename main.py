#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')
from utils.skeleton import get_node_grid
from utils.data_classes import AllNodes, AllLines, AllSurfaces, DefNode
from RFEM.enums import NodalSupportType, MemberRotationSpecificationType
from RFEM.initModel import Model, clearAttributes, insertSpaces
from utils.base import get_node_id_using_coordinates
from dataclasses import asdict
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.line import Line
from RFEM.TypesForNodes.nodalSupport import NodalSupport

if __name__ == '__main__':

    Model(True, "MyModel")
    Model.clientModel.service.begin_modification()
    all_nodes = AllNodes()
    all_lines = AllLines()
    all_surfaces = AllSurfaces()
    get_node_grid(list_coordinates_x=[0, 5, 10, 15, 20, 25],
                  list_coordinates_y=[0, 4, 6.5, 11],
                  list_coordinates_z=[0, -3.34, -6.68],
                  all_nodes=all_nodes)
    all_lines.create_line_by_coordinates(
        nodes_coordinates=[DefNode(0, 0, 0), DefNode(25, 0, 0)],
        all_nodes=all_nodes)



    # # clearAttributes()
    # list_coordinates_x = [0, 5, 10, 15, 20, 25]
    # list_coordinates_y = [0, 4, 6.5, 11]
    # list_coordinates_z = [0, -3.34, -6.68]
    #
    # id = 1
    # node_coordinates = []
    # for x in list_coordinates_x:
    #     for y in list_coordinates_y:
    #         for z in list_coordinates_z:
    #             id += 1
    #             node_coordinates.append([id, x, y, z])
    #             Node(id, x, y, z)
    #
    # line_01 = Line(1,"1 2", )
    Model.clientModel.service.finish_modification()
