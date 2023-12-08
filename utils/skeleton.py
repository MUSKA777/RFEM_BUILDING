from typing import List, Any
from RFEM.BasicObjects.node import Node



def sort_coordinates_x_y_z(coordinates):
    # TODO: upravit na jiné vstupy!!!
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
                  all_nodes: Any
                  ):
    """
       create a node grid
    :param list_coordinates_x: [0, 5, 10, 15, 20, 25]
    :param list_coordinates_y: [0, 4, 6.5, 11]
    :param list_coordinates_z: [0, 3.34, 6.68]
    :param all_nodes:
    :return:
    """

    for x in list_coordinates_x:
        for y in list_coordinates_y:
            for z in list_coordinates_z:
                # max_id = max(all_nodes.all_ids) if all_nodes.all_ids else None
                # print(f"max_id: {max_id}")
                # _no = max_id if max_id else 0 + 1
                all_nodes.create_node(
                                      coordinate_X=x,
                                      coordinate_Y=y,
                                      coordinate_Z=z)

    # return all_nodes
