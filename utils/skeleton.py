from typing import Any, List


def get_node_grid(
    list_coordinates_x: List[float],
    list_coordinates_y: List[float],
    list_coordinates_z: List[float],
    all_nodes: Any,
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
                all_nodes.create_node(coordinate_x=x, coordinate_y=y, coordinate_z=z)
