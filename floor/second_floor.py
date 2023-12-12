from floor.common import CommonForFloor

class SecondFloor(CommonForFloor):

    def __call__(self, *args, **kwargs):
        self.create_base_with_offset(offset_z=-3.34)
        self.create_back_site_with_offset(offset_z=-3.34)
        self.create_back_site_with_offset(offset_z=-3.34, offset_y=11)
        self.create_first_left_side_with_offset(offset_z=-3.34)
        self.create_first_left_side_with_offset(offset_z=-3.34, offset_x=25)
        self.create_area_for_stairs_with_offset(offset_z=-3.34)
        # self.create_base_with_offset(offset_z=2*-3.34)
