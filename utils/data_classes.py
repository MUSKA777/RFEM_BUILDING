from dataclasses import dataclass, field
from typing import List, Optional, Dict
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.line import Line


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
        self.all_def_nodes.append(
            DefNode(coordinate_X=coordinate_X,
                    coordinate_Y=coordinate_Y,
                    coordinate_Z=coordinate_Z,
                    id=new_id)
        )


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
            for node_id in self.nodes_no:
                _node = Node.GetNode(node_id)
                self.nodes_def_line.append(DefNode(_node.coordinate_1, _node.coordinate_2, _node.coordinate_3))


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
            nodes_no.append(get_node_id_using_coordinates(all_nodes=all_nodes,
                                                  coordinate_X=node.coordinate_X,
                                                  coordinate_Y=node.coordinate_Y,
                                                  coordinate_Z=node.coordinate_Z))
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

    if not node_1.coordinate_Y != node_2.coordinate_Y:
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



@dataclass
class AllSurfaces:
    all_ids: List[int] = field(default_factory=list)
    all_def_surfaces: List[DefSurface] = field(default_factory=list)

    def create_surface_by_no(self,
                             boundary_lines_no: List[int],
                             thickness: int,
                             id: Optional[int] = None):
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

    # def create_surface_by_coordinates(self,
    #                                   lines_coordinates: List[DefLine],
    #                                   all_lines: AllLines,
    #                                   id: Optional[int] = None):
    #     new_id = get_new_max_id(all_ids=self.all_ids, id=id)
    #     self.all_ids.append(new_id)
    #     boundary_lines_no = []
    #     for _line in lines_coordinates:
    #         boundary_lines_no.append(get_line_id_using_coordinates())
    #
    #     new_def_surface = DefSurface(
    #         boundary_lines_no=boundary_lines_no,
    #         thickness=thickness,
    #         id=new_id)
    #     Surface(boundary_lines_no=str(boundary_lines_no)[1:-1],
    #             thickness=thickness,
    #             no=new_id)
    #

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
