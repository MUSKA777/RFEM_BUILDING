from typing import List, Optional, Dict
from dataclasses import dataclass, field
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.opening import Opening
from utils.def_data_classes.line import DefLine, AllLines, get_line_id_using_coordinates
from utils.def_data_classes.node import DefNode, AllNodes
from utils.def_data_classes.common import get_new_max_id


@dataclass
class DefOpening:
    id: int
    boundary_lines_no: List[int]
    lines_def_surface: List[DefLine] = field(default_factory=list)

    def __post_init__(self):
        if self.boundary_lines_no:
            _nodes_no = []
            for line_id in self.boundary_lines_no:
                _line = Line.GetLine(line_id)
                for _str_value in _line.definition_nodes.split(" "):
                    _nodes_no.append(int(_str_value))
                _def_line = DefLine(
                    id=_line.no,
                    nodes_no=_nodes_no,
                )
                self.lines_def_surface.append(_def_line)

@dataclass
class AllOpening:
    all_ids: List[int] = field(default_factory=list)
    all_def_opening: List[DefOpening] = field(default_factory=list)
    def create_opening_by_nodes(self,
                                corners_of_the_opening: List[DefNode],
                                all_lines: AllLines,
                                all_nodes: AllNodes,
                                id: Optional[int] = None,
                                ):
        new_id = get_new_max_id(all_ids=self.all_ids, id=id)
        self.all_ids.append(new_id)
        boundary_lines_no = []
        lines_def_surface = []
        for _index, _def_node, in enumerate(corners_of_the_opening):
            if len(corners_of_the_opening) - 1 == _index:
                _coordinates = [_def_node, corners_of_the_opening[0]]
            else:
                _coordinates = [_def_node, corners_of_the_opening[_index + 1]]

            line_id = get_line_id_using_coordinates(
                all_lines=all_lines,
                start_coordinates=_coordinates[0],
                end_coordinates=_coordinates[1]
            )
            if not line_id and all_nodes:
                new_def_line = all_lines.create_line_by_coordinates(
                    nodes_coordinates=[_coordinates[0], _coordinates[1]],
                    all_nodes=all_nodes)
                line_id = new_def_line.id
                lines_def_surface.append(new_def_line)
            boundary_lines_no.append(line_id)

        new_def_opening = DefOpening(
            boundary_lines_no=boundary_lines_no,
            lines_def_surface=lines_def_surface,
            id=new_id)
        Opening(no=new_id, lines_no=str(boundary_lines_no)[1:-1])

        self.all_def_opening.append(new_def_opening)
        return new_def_opening

    def copy_and_offset(self, def_opening: DefOpening,
                        all_lines: AllLines,
                        all_nodes: AllNodes,
                        offset_x: float = 0.0,  # m
                        offset_y: float = 0.0,  # m
                        offset_z: float = 0.0,  # m
                        id: Optional[int] = None,):

        new_id = get_new_max_id(all_ids=self.all_ids, id=id)
        self.all_ids.append(new_id)
        corners_of_the_opening = []
        for _def_line in def_opening.lines_def_surface:
            for _node in _def_line.nodes_def_line:
                _def_node = DefNode(_node.coordinate_x + offset_x,
                                    _node.coordinate_y + offset_y,
                                    _node.coordinate_z + offset_z)
                if _def_node in corners_of_the_opening:
                    continue
                corners_of_the_opening.append(_def_node)
        new_def_opening = self.create_opening_by_nodes(corners_of_the_opening=corners_of_the_opening,
                                     all_nodes=all_nodes,
                                     all_lines=all_lines)
        return new_def_opening

