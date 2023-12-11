from typing import List, Optional, Dict
from dataclasses import dataclass, field
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.line import Line
from utils.def_data_classes.line import DefLine, AllLines, get_line_id_using_coordinates
from utils.def_data_classes.node import DefNode, AllNodes
from utils.def_data_classes.common import get_new_max_id

@dataclass
class DefSurface:
    id: int
    boundary_lines_no: List[int]
    thickness: int
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
class AllSurfaces:
    all_ids: List[int] = field(default_factory=list)
    all_def_surfaces: List[DefSurface] = field(default_factory=list)

    def create_surface_by_no(self,
                             boundary_lines_no: List[int],
                             thickness: int,
                             id: Optional[int] = None) -> DefSurface:
        new_id = get_new_max_id(all_ids=self.all_ids, id=id)
        self.all_ids.append(new_id)
        new_def_surface = DefSurface(
            boundary_lines_no=boundary_lines_no,
            thickness=thickness,
            id=new_id)
        Surface(boundary_lines_no=str(boundary_lines_no)[1:-1],
                thickness=thickness,
                no=new_id)
        self.all_def_surfaces.append(new_def_surface)
        return new_def_surface

    def create_surface_by_nodes(self,
                                corners_of_the_surface: List[DefNode],
                                all_lines: AllLines,
                                thickness: int,
                                id: Optional[int] = None,
                                all_nodes: Optional[AllNodes] = None) -> DefSurface:
        new_id = get_new_max_id(all_ids=self.all_ids, id=id)
        self.all_ids.append(new_id)
        boundary_lines_no = []
        for _index, _def_node, in enumerate(corners_of_the_surface):
            if len(corners_of_the_surface)-1 == _index:
                _coordinates = [_def_node, corners_of_the_surface[0]]
            else:
                _coordinates = [_def_node, corners_of_the_surface[_index+1]]
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

            boundary_lines_no.append(line_id)

        new_def_surface = DefSurface(
            boundary_lines_no=boundary_lines_no,
            thickness=thickness,
            id=new_id)
        Surface(boundary_lines_no=str(boundary_lines_no)[1:-1],
                thickness=thickness,
                no=new_id)
        self.all_def_surfaces.append(new_def_surface)
        return new_def_surface

    def copy_and_offset(self, def_surface: DefSurface,
                        all_lines: AllLines,
                        all_nodes: AllNodes,
                        offset_x: float = 0.0,  # m
                        offset_y: float = 0.0,  # m
                        offset_z: float = 0.0,  # m
                        id: Optional[int] = None, ):

        new_id = get_new_max_id(all_ids=self.all_ids, id=id)
        self.all_ids.append(new_id)
        corners_of_the_surface = []
        for _def_line in def_surface.lines_def_surface:
            for _node in _def_line.nodes_def_line:
                _def_node = DefNode(_node.coordinate_X + offset_x,
                                    _node.coordinate_Y + offset_y,
                                    _node.coordinate_Z + offset_z)
                if _def_node in corners_of_the_surface:
                    continue
                corners_of_the_surface.append(_def_node)
        new_def_opening = self.create_surface_by_nodes(corners_of_the_surface=corners_of_the_surface,
                                                       thickness=def_surface.thickness,
                                                       all_nodes=all_nodes,
                                                       all_lines=all_lines)
        return new_def_opening

