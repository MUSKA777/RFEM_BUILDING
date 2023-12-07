from typing import List
from RFEM.BasicObjects.node import Node


def sort_coordinates_x_y_z(coordinates):
    """
    id, x, y, z
    :param coordinates:
    :return:
    """
    all_nos = []
    all_x = []
    all_y = []
    all_z = []
    for element in coordinates:
        all_nos.append(element[0])
        all_x.append(element[1])
        all_y.append(element[2])
        all_z.append(element[3])

    return {"all_nos": all_nos, "all_x": all_x, "all_y": all_y, "all_z": all_z}



def get_node_grid(list_coordinates_x: List[float],
                  list_coordinates_y: List[float],
                  list_coordinates_z: List[float],
                  ):

    """
    create a node grid
    :param x: [0, 5, 10, 15, 20, 25]
    :param y: [0, 4, 6.5, 11]
    :param z: [0, 3.34, 6.68]
    :return:
    """
    no = 1
    node_coordinates = []
    for x in list_coordinates_x:
        for y in list_coordinates_y:
            for z in list_coordinates_z:
                no += 1
                node_coordinates.append([no, x, y, z])
                Node(no, x, y, z)

    return node_coordinates


