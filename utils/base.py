
from typing import Optional, List
from utils.data_classes import AllNodes, AllLines


def get_node_id_using_coordinates(all_nodes: AllNodes,
                             coordinate_X: float,
                             coordinate_Y: float,
                             coordinate_Z: float) -> Optional[int]:

    for def_node in all_nodes.all_def_nodes:
        if def_node.coordinate_X != coordinate_X:
            continue

        if not def_node.coordinate_Y != coordinate_Y:
            continue

        if def_node.coordinate_Z == coordinate_Z:
            return def_node.id

    return None

# def get_line_id_using_start_stop_coordinate(all_lines: AllLines,
#                                  start_xyz: List[int, int, int],
#                                 stop_xyz: List[int, int, int]):
#     for def_line in all_lines.all_def_lines:
#         if not



