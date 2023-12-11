from dataclasses import dataclass, field
from typing import List, Optional, Dict
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from utils.def_data_classes.common import get_new_max_id
from utils.def_data_classes.node import DefNode, AllNodes, get_node_id_using_coordinates


@dataclass
class DefLine:
    id: int
    nodes_def_line: List[DefNode] = field(default_factory=list)
    nodes_no: List[int] = field(default_factory=list)

    def __post_init__(self):
        if self.nodes_def_line and self.nodes_def_line[0].id:
            for _node in self.nodes_def_line:
                self.nodes_no.append(_node.id)

        if self.nodes_no:
            pair_def_node = []
            for node_id in self.nodes_no:
                _node = Node.GetNode(node_id)
                pair_def_node.append(DefNode(_node.coordinate_1, _node.coordinate_2, _node.coordinate_3))
            self.nodes_def_line.extend(pair_def_node)


@dataclass
class AllLines:
    all_ids: List[int] = field(default_factory=list)
    all_def_lines: List[DefLine] = field(default_factory=list)

    def create_line_by_no(self,
                          nodes_no: List[int],
                          id: Optional[int] = None,
                          ):
        new_id = get_new_max_id(all_ids=self.all_ids, id=id)
        self.all_ids.append(new_id)
        new_def_line = DefLine(
            nodes_no=nodes_no,
            id=new_id)
        Line(nodes_no=f"{nodes_no}",
             no=new_id)

        self.all_def_lines.append(new_def_line)
        return new_def_line

    def create_line_by_coordinates(self,
                                   nodes_coordinates: List[DefNode],
                                   all_nodes: AllNodes,
                                   id: Optional[int] = None):
        new_id = get_new_max_id(all_ids=self.all_ids, id=id)
        self.all_ids.append(new_id)
        nodes_no: List[int] = []

        for node in nodes_coordinates:
            node_id = get_node_id_using_coordinates(all_nodes=all_nodes,
                                                  coordinate_X=node.coordinate_X,
                                                  coordinate_Y=node.coordinate_Y,
                                                  coordinate_Z=node.coordinate_Z)
            if not node_id:
                new_node = all_nodes.create_node(coordinate_X=node.coordinate_X,
                                                 coordinate_Y=node.coordinate_Y,
                                                 coordinate_Z=node.coordinate_Z)
                node_id = new_node.id
            nodes_no.append(node_id)
        new_def_line = DefLine(
            nodes_no=nodes_no,
            id=new_id)
        Line(nodes_no=str(nodes_no)[1:-1],
             no=new_id)
        self.all_def_lines.append(new_def_line)
        return new_def_line


def are_node_coordinates_same(node_1: DefNode, node_2: DefNode) -> bool:
    if node_1.coordinate_X != node_2.coordinate_X:
        return False

    if node_1.coordinate_Y != node_2.coordinate_Y:
        return False

    if node_1.coordinate_Z == node_2.coordinate_Z:
        return True
    return False


def get_line_id_using_coordinates(all_lines: AllLines, start_coordinates: DefNode, end_coordinates: DefNode):
    for _def_line in all_lines.all_def_lines:
        are_checkpoints_met = [False, False]
        for _def_node in _def_line.nodes_def_line:

            if are_node_coordinates_same(_def_node, start_coordinates):
                are_checkpoints_met[0] = True

            elif are_node_coordinates_same(_def_node, end_coordinates):
                are_checkpoints_met[1] = True

            if set(are_checkpoints_met) == {True}:
                return _def_line.id
    return None