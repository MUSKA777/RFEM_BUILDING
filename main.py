#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')


from RFEM.enums import NodalSupportType, MemberRotationSpecificationType
from RFEM.initModel import Model, clearAttributes, insertSpaces
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.line import Line
from RFEM.TypesForNodes.nodalSupport import NodalSupport

if __name__ == '__main__':

    Model(True, "MyModel")
    Model.clientModel.service.begin_modification()


    # clearAttributes()
    list_coordinates_x = [0, 5, 10, 15, 20, 25]
    list_coordinates_y = [0, 4, 6.5, 11]
    list_coordinates_z = [0, -3.34, -6.68]

    id = 1
    node_coordinates = []
    for x in list_coordinates_x:
        for y in list_coordinates_y:
            for z in list_coordinates_z:
                id += 1
                node_coordinates.append([id, x, y, z])
                Node(id, x, y, z)

    line_01 = Line(1,"1 2", )



    print(f"node_coordinates: {node_coordinates}")
    Model.clientModel.service.finish_modification()
