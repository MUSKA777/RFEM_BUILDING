from dataclasses import dataclass, field
from typing import List, Optional

from RFEM.BasicObjects.node import Node

from utils.def_data_classes.common import get_new_max_id


@dataclass
class DefNode:
    coordinate_x: float
    coordinate_y: float
    coordinate_z: float
    id: Optional[int] = field(default=None)

    def __post_init__(self):
        pass


@dataclass
class AllNodes:
    all_ids: List[int] = field(default_factory=list)
    all_def_nodes: List[DefNode] = field(default_factory=list)

    def create_node(
        self,
        coordinate_x: float,
        coordinate_y: float,
        coordinate_z: float,
        id: Optional[int] = None,
    ):
        new_id = get_new_max_id(all_ids=self.all_ids, id=id)
        self.all_ids.append(new_id)
        Node(
            coordinate_X=coordinate_x,
            coordinate_Y=coordinate_y,
            coordinate_Z=coordinate_z,
            no=new_id,
        )
        new_def_node = DefNode(
            coordinate_x=coordinate_x,
            coordinate_y=coordinate_y,
            coordinate_z=coordinate_z,
            id=new_id,
        )
        self.all_def_nodes.append(new_def_node)
        return new_def_node


def get_node_id_using_coordinates(
    all_nodes: AllNodes, coordinate_x: float, coordinate_y: float, coordinate_z: float
) -> Optional[int]:
    for def_node in all_nodes.all_def_nodes:
        if def_node.coordinate_x != coordinate_x:
            continue

        elif def_node.coordinate_y != coordinate_y:
            continue

        elif def_node.coordinate_z == coordinate_z:
            return def_node.id

    return None
