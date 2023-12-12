from floor.common import CommonForFloor
from utils.def_data_classes.section import AllSections
from RFEM.BasicObjects.member import Member
from utils.def_data_classes.node import DefNode


class SecondFloor(CommonForFloor):
    def create_bearing_pillars_first_floor(self):
        self.all_members.create_member_by_coordinates(
            nodes_coordinates=[DefNode(5, 6.5, 0), DefNode(5, 6.5, -3.34)],
            list_sections=[AllSections.r_m1_240_slash_240_c20_slash_25, AllSections.r_m1_240_slash_240_c20_slash_25],
            all_nodes=self.all_nodes
        )

        self.all_members.create_member_by_coordinates(
            nodes_coordinates=[DefNode(10, 6.5, 0), DefNode(10, 6.5, -3.34)],
            list_sections=[AllSections.r_m1_240_slash_240_c20_slash_25, AllSections.r_m1_240_slash_240_c20_slash_25],
            all_nodes=self.all_nodes
        )
        self.all_members.create_member_by_coordinates(
            nodes_coordinates=[DefNode(0, 6.5, -3.34), DefNode(15, 6.5, -3.34)],
            list_sections=[AllSections.r_m1_240_slash_500_c20_slash_25, AllSections.r_m1_240_slash_500_c20_slash_25],
            all_nodes=self.all_nodes)

    def create_bearing_pillars_with_offset(self,
                                           offset_x: float = 0.0,  # m
                                          offset_y: float = 0.0,  # m
                                          offset_z: float = 0.0,  # m
                                           ) -> None:
        # upper
        upper_line_nodes_coordinates = self.get_corners_of_the_surface_with_offset(
            [DefNode(5, 0, -6.68), DefNode(5, 11, -6.68)], offset_x, offset_y, offset_z)
        self.all_members.create_member_by_coordinates(
            nodes_coordinates=upper_line_nodes_coordinates,
            list_sections=[AllSections.he_100_A_slash_1_grade_s355, AllSections.he_100_A_slash_1_grade_s355],
            all_nodes=self.all_nodes
        )

        # bottom 01
        bottom_01_line_nodes_coordinates = self.get_corners_of_the_surface_with_offset(
            [DefNode(5, 0, -6.68), DefNode(5, 3.25, -5.93)], offset_x, offset_y, offset_z)
        self.all_members.create_member_by_coordinates(
            nodes_coordinates=bottom_01_line_nodes_coordinates,
            list_sections=[AllSections.he_100_A_slash_1_grade_s355, AllSections.he_100_A_slash_1_grade_s355],
            all_nodes=self.all_nodes
        )
        # bottom 02
        bottom_02_line_nodes_coordinates = self.get_corners_of_the_surface_with_offset(
            [DefNode(5, 3.25, -5.93), DefNode(5, 6.5, -6.68)], offset_x, offset_y, offset_z)
        self.all_members.create_member_by_coordinates(
            nodes_coordinates=bottom_02_line_nodes_coordinates,
            list_sections=[AllSections.he_100_A_slash_1_grade_s355, AllSections.he_100_A_slash_1_grade_s355],
            all_nodes=self.all_nodes
        )
        # bottom 03
        bottom_03_line_nodes_coordinates = self.get_corners_of_the_surface_with_offset(
            [DefNode(5, 6.5, -6.68), DefNode(5, 8.75, -5.93)], offset_x, offset_y, offset_z)
        self.all_members.create_member_by_coordinates(
            nodes_coordinates=bottom_03_line_nodes_coordinates,
            list_sections=[AllSections.he_100_A_slash_1_grade_s355, AllSections.he_100_A_slash_1_grade_s355],
            all_nodes=self.all_nodes
        )
        # bottom 04
        bottom_04_line_nodes_coordinates = self.get_corners_of_the_surface_with_offset(
            [DefNode(5, 8.75, -5.93), DefNode(5, 11, -6.68)], offset_x, offset_y, offset_z)
        self.all_members.create_member_by_coordinates(
            nodes_coordinates=bottom_04_line_nodes_coordinates,
            list_sections=[AllSections.he_100_A_slash_1_grade_s355, AllSections.he_100_A_slash_1_grade_s355],
            all_nodes=self.all_nodes
        )

        # bottom line 01
        bottom_center_01_nodes_coordinates = self.get_corners_of_the_surface_with_offset(
            [DefNode(5, 3.25, -5.93), DefNode(5, 6.5, -5.93)], offset_x, offset_y, offset_z)
        self.all_members.create_member_by_coordinates(
            nodes_coordinates=bottom_center_01_nodes_coordinates,
            list_sections=[AllSections.he_100_A_slash_1_grade_s355, AllSections.he_100_A_slash_1_grade_s355],
            all_nodes=self.all_nodes
        )
        # bottom line 02
        bottom_center_02_nodes_coordinates = self.get_corners_of_the_surface_with_offset(
            [DefNode(5, 6.5, -5.93), DefNode(5, 8.75, -5.93)], offset_x, offset_y, offset_z)
        self.all_members.create_member_by_coordinates(
            nodes_coordinates=bottom_center_02_nodes_coordinates,
            list_sections=[AllSections.he_100_A_slash_1_grade_s355, AllSections.he_100_A_slash_1_grade_s355],
            all_nodes=self.all_nodes
        )

        pillar_01_nodes_coordinates = self.get_corners_of_the_surface_with_offset(
            [DefNode(5, 3.25, -5.93), DefNode(5, 3.25, -6.68)], offset_x, offset_y, offset_z)
        self.all_members.create_member_by_coordinates(
            nodes_coordinates=pillar_01_nodes_coordinates,
            list_sections=[AllSections.chc_60dot3x3_slash_1_grade_s355, AllSections.chc_60dot3x3_slash_1_grade_s355],
            all_nodes=self.all_nodes
        )
        pillar_02_nodes_coordinates = self.get_corners_of_the_surface_with_offset(
            [DefNode(5, 6.5, -5.93), DefNode(5, 6.5, -6.68)], offset_x, offset_y, offset_z)
        self.all_members.create_member_by_coordinates(
            nodes_coordinates=pillar_02_nodes_coordinates,
            list_sections=[AllSections.chc_60dot3x3_slash_1_grade_s355, AllSections.chc_60dot3x3_slash_1_grade_s355],
            all_nodes=self.all_nodes
        )
        pillar_03_nodes_coordinates = self.get_corners_of_the_surface_with_offset(
            [DefNode(5, 8.75, -5.93), DefNode(5, 8.75, -6.68)], offset_x, offset_y, offset_z)
        self.all_members.create_member_by_coordinates(
            nodes_coordinates=pillar_03_nodes_coordinates,
            list_sections=[AllSections.chc_60dot3x3_slash_1_grade_s355, AllSections.chc_60dot3x3_slash_1_grade_s355],
            all_nodes=self.all_nodes
        )

    def create_basic_pillars(self):
        self.all_members.create_member_by_coordinates(
            nodes_coordinates=[DefNode(15, 0, -6.68), DefNode(15, 6.5, -6.68)],
            list_sections=[AllSections.ipe_200_slash_1_grade_s355, AllSections.ipe_200_slash_1_grade_s355],
            all_nodes=self.all_nodes
        )

        self.all_members.create_member_by_coordinates(
            nodes_coordinates=[DefNode(20, 0, -6.68), DefNode(20, 6.5, -6.68)],
            list_sections=[AllSections.ipe_200_slash_1_grade_s355, AllSections.ipe_200_slash_1_grade_s355],
            all_nodes=self.all_nodes
        )

    def __call__(self):
        self.create_back_site_with_offset(offset_z=-3.34)
        self.create_back_site_with_offset(offset_z=-3.34, offset_y=11)
        self.create_first_left_side_with_offset(offset_z=-3.34)
        self.create_first_left_side_with_offset(offset_z=-3.34, offset_x=25)
        self.create_area_for_stairs_with_offset(offset_z=-3.34)
        self.create_bearing_pillars_with_offset()
        self.create_bearing_pillars_with_offset(offset_x=5)
        self.create_basic_pillars()
        self.create_bearing_pillars_first_floor()
        self.create_base_with_offset(offset_z=2*-3.34)
