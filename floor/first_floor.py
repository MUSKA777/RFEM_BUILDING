from utils.def_data_classes.node import DefNode
from floor.common import CommonForFloor
from utils.def_data_classes.section import AllSections
from RFEM.BasicObjects.member import Member
from utils.def_data_classes.node import DefNode, get_node_id_using_coordinates


class FirstFloor(CommonForFloor):
    #
    def create_bearing_pillars(self):
        self.all_lines.create_line_by_coordinates(
            nodes_coordinates=[DefNode(5, 6.5, 0), DefNode(5, 6.5, -3.34)],
            all_nodes=self.all_nodes)

        self.all_members.create_member_by_coordinates(
            nodes_coordinates=[DefNode(5, 6.5, 0), DefNode(5, 6.5, -3.34)],
            list_sections=[AllSections.r_m1_240_slash_240_c20_slash_25, AllSections.r_m1_240_slash_240_c20_slash_25],
            all_nodes=self.all_nodes
        )
        # Member(start_node_no=line_01.nodes_def_line[0].id,
        #        end_node_no=line_01.nodes_def_line[1].id,
        #        start_section_no=AllSections.r_m1_240_slash_240_c20_slash_25.id,
        #        end_section_no=AllSections.r_m1_240_slash_240_c20_slash_25.id,
        #        no=1)

        self.all_lines.create_line_by_coordinates(
            nodes_coordinates=[DefNode(10, 6.5, 0), DefNode(10, 6.5, -3.34)],
            all_nodes=self.all_nodes)
        self.all_members.create_member_by_coordinates(
            nodes_coordinates=[DefNode(10, 6.5, 0), DefNode(10, 6.5, -3.34)],
            list_sections=[AllSections.r_m1_240_slash_240_c20_slash_25, AllSections.r_m1_240_slash_240_c20_slash_25],
            all_nodes=self.all_nodes
        )

        self.all_lines.create_line_by_coordinates(
            nodes_coordinates=[DefNode(0, 6.5, -3.34), DefNode(15, 6.5, -3.34)],
            all_nodes=self.all_nodes)
        self.all_members.create_member_by_coordinates(
            nodes_coordinates=[DefNode(0, 6.5, -3.34), DefNode(15, 6.5, -3.34)],
            list_sections=[AllSections.r_m1_240_slash_500_c20_slash_25, AllSections.r_m1_240_slash_500_c20_slash_25],
            all_nodes=self.all_nodes
        )

    def create_front_site(self) -> None:
        self.create_back_site_without_door_with_offset(offset_y=11)

        front_door_corners_of_the_opening = [DefNode(15.75, 11, -0.15),
                                             DefNode(19.25, 11, -0.15),
                                             DefNode(19.25, 11, -2.75),
                                             DefNode(15.75, 11, -2.75)]
        self.create_window_with_glass(corners_of_the_opening=front_door_corners_of_the_opening)

    def create_mezzanine_base(self):
        self.all_surfaces.create_surface_by_nodes(
            corners_of_the_surface=[DefNode(0, 0, -3.34),
                                    DefNode(25, 0, -3.34),
                                    DefNode(25, 11, -3.34),
                                    DefNode(20, 11, -3.34),
                                    DefNode(20, 6.5, -3.34),
                                    DefNode(15, 6.5, -3.34),
                                    DefNode(15, 11, -3.34),
                                    DefNode(0, 11, -3.34),
                                    ],
            all_lines=self.all_lines,
            all_nodes=self.all_nodes,
            thickness=self.all_thicknesses.uniform_d_300_c20slash25.id,
        )

    def __call__(self) -> None:
        self.create_base_with_offset()
        self.create_first_left_side_with_offset()
        self.create_front_site()
        self.create_area_for_stairs_with_offset()
        self.create_first_left_side_with_offset(offset_x=25)
        # self.create_bearing_pillars()
        self.create_back_site_with_offset()
        self.create_mezzanine_base()
