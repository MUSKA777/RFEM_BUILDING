from dataclasses import dataclass, field
from typing import List, Optional, Dict
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.opening import Opening


def get_new_max_id(all_ids: List[int], id: int) -> int:
    if not all_ids:
        if id:
            return id
        return 1
    if id and id not in all_ids:
        return id
    return max(all_ids) + 1


def get_material_name() -> str:
    pass


@dataclass
class DefMaterial:
    id: int
    material_type: str
    material_model: str
    name: str

    def __post_init__(self):
        Material(
            no=self.id,
            name=self.name,
        )


@dataclass
class AllMaterials:
    all_ids: List[int] = field(default_factory=list)
    all_materials: List[Dict[str, DefMaterial]] = field(default_factory=list)


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
                _def_node = DefNode(_node.coordinate_X+offset_x,
                            _node.coordinate_Y+offset_y,
                            _node.coordinate_Z+offset_z)
                if _def_node in corners_of_the_opening:
                    continue
                corners_of_the_opening.append(_def_node)
        new_def_opening = self.create_opening_by_nodes(corners_of_the_opening=corners_of_the_opening,
                                     all_nodes=all_nodes,
                                     all_lines=all_lines)
        return new_def_opening













# @dataclass
# class AllIds:
#     materials: Optional[List[int]] = field(default=None)
#     sections: Optional[List[int]] = field(default=None)
#     thicknesses: Optional[List[int]] = field(default=None)
#     nodes: Optional[List[int]] = field(default=None)
#     lines: Optional[List[int]] = field(default=None)
#     members: Optional[List[int]] = field(default=None)
#     surfaces: Optional[List[int]] = field(default=None)
#     openings: Optional[List[int]] = field(default=None)
#
#     def add_node(self, coordinate_X: float, coordinate_Y: float, coordinate_Z: float, no: Optional[int]):
#         self.nodes = self.nodes.append(max(self.nodes)+1)
#         DefNode(coordinate_X=coordinate_X,
#                        coordinate_Y=coordinate_Y,
#                        coordinate_Z=coordinate_Z,
#                        no=no if no else max(self.nodes))
