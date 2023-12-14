from dataclasses import dataclass, field
from typing import List, Optional

from RFEM.BasicObjects.member import Member

from utils.def_data_classes.common import get_new_max_id
from utils.def_data_classes.node import AllNodes, DefNode, get_node_id_using_coordinates
from utils.def_data_classes.section import DefSection


@dataclass
class DefMember:
    id: int
    nodes_def_member: List[DefNode]  # [start_node, end_node]
    sections_def_member: List[DefSection]  # [start_section, end_section]
    rotation_angle: float = field(default=0.0)


@dataclass
class AllMembers:
    all_ids: List[int] = field(default_factory=list)
    all_def_members: List[DefMember] = field(default_factory=list)

    def create_member_by_coordinates(
        self,
        nodes_coordinates: List[DefNode],
        list_sections: List[DefSection],
        all_nodes: AllNodes,
        id: Optional[int] = None,
    ):
        new_id = get_new_max_id(all_ids=self.all_ids, id=id)
        self.all_ids.append(new_id)
        all_nodes_id: List[int] = []
        nodes_def_member: List[DefNode] = []
        for _node in nodes_coordinates:
            node_id = get_node_id_using_coordinates(
                all_nodes=all_nodes,
                coordinate_x=_node.coordinate_x,
                coordinate_y=_node.coordinate_y,
                coordinate_z=_node.coordinate_z,
            )
            if not node_id:
                new_node = all_nodes.create_node(
                    coordinate_x=_node.coordinate_x,
                    coordinate_y=_node.coordinate_y,
                    coordinate_z=_node.coordinate_z,
                )
                node_id = new_node.id
            all_nodes_id.append(node_id)
            nodes_def_member.append(
                DefNode(
                    id=node_id,
                    coordinate_x=_node.coordinate_x,
                    coordinate_y=_node.coordinate_y,
                    coordinate_z=_node.coordinate_z,
                )
            )
        new_def_member = DefMember(
            nodes_def_member=nodes_def_member,
            sections_def_member=list_sections,
            id=new_id,
        )

        Member(
            start_node_no=all_nodes_id[0],
            end_node_no=all_nodes_id[1],
            start_section_no=list_sections[0].id,
            end_section_no=list_sections[1].id,
            no=new_id,
        )
        self.all_def_members.append(new_def_member)
        return new_def_member
