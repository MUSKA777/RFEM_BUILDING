from RFEM.BasicObjects.node import Node
from dataclasses import dataclass, field
from typing import List, Optional, Dict
from utils.def_data_classes.common import get_new_max_id

@dataclass
class DefNode:
    coordinate_X: float
    coordinate_Y: float
    coordinate_Z: float
    id: Optional[int] = field(default=None)


@dataclass
class AllNodes:
    all_ids: List[int] = field(default_factory=list)
    all_def_nodes: List[DefNode] = field(default_factory=list)

    def create_node(self,
                    coordinate_X: float,
                    coordinate_Y: float,
                    coordinate_Z: float,
                    id: Optional[int] = None):
        new_id = get_new_max_id(all_ids=self.all_ids, id=id)
        self.all_ids.append(new_id)
        Node(coordinate_X=coordinate_X,
             coordinate_Y=coordinate_Y,
             coordinate_Z=coordinate_Z,
             no=new_id)
        new_def_node = DefNode(coordinate_X=coordinate_X,
                    coordinate_Y=coordinate_Y,
                    coordinate_Z=coordinate_Z,
                    id=new_id)
        self.all_def_nodes.append(new_def_node)
        return new_def_node


def get_node_id_using_coordinates(all_nodes: AllNodes,
                                  coordinate_X: float,
                                  coordinate_Y: float,
                                  coordinate_Z: float) -> Optional[int]:
    for def_node in all_nodes.all_def_nodes:
        if def_node.coordinate_X != coordinate_X:
            continue

        elif def_node.coordinate_Y != coordinate_Y:
            continue

        elif def_node.coordinate_Z == coordinate_Z:
            return def_node.id

    return None
