from dataclasses import dataclass, field
from typing import Optional

from RFEM.BasicObjects.section import Section

from utils.def_data_classes.material import AllMaterial


@dataclass
class SectionType:
    parametric_massive_I: str = "Parametric - Massive I"
    standardized_steel: str = "Standardized - Steel"


@dataclass
class ManufacturingType:
    hot_rolled: str = "Hot rolled"
    cold_formed: str = "Cold formed"


@dataclass
class DefSection:
    id: int
    material: AllMaterial.__name__
    section_type: SectionType.__name__
    section_name: str
    manufacturing_type: Optional[str] = field(default=None)
    name: Optional[str] = field(default=None)

    def __post_init__(self):
        self.name = f"{self.id} - {self.section_name} | {self.material.name}"

    def create_section(self):
        Section(no=self.id, name=self.section_name, material_no=self.material.id)


@dataclass
class AllSections:
    r_m1_240_slash_240_c20_slash_25: DefSection = DefSection(
        id=1,
        material=AllMaterial.c20_slash_25_isotropic_linear_elastic,
        section_type=SectionType.parametric_massive_I,
        section_name="R_M1 0.240/0.240",
    )
    r_m1_240_slash_500_c20_slash_25: DefSection = DefSection(
        id=2,
        material=AllMaterial.c20_slash_25_isotropic_linear_elastic,
        section_type=SectionType.parametric_massive_I,
        section_name="R_M1 0.240/0.500",
    )
    ipe_80_slash_1_grade_s355: DefSection = DefSection(
        id=3,
        material=AllMaterial.grade_S355_isotropic_linear_elastic,
        section_type=SectionType.standardized_steel,
        manufacturing_type=ManufacturingType.hot_rolled,
        section_name="IPE 80",
    )
    chc_60dot3x3_slash_1_grade_s355: DefSection = DefSection(
        id=4,
        material=AllMaterial.grade_S355_isotropic_linear_elastic,
        section_type=SectionType.standardized_steel,
        manufacturing_type=ManufacturingType.cold_formed,
        section_name="CHC 60.3x3.0",
    )
    ipe_200_slash_1_grade_s355: DefSection = DefSection(
        id=5,
        material=AllMaterial.grade_S355_isotropic_linear_elastic,
        section_type=SectionType.standardized_steel,
        manufacturing_type=ManufacturingType.hot_rolled,
        section_name="IPE 200",
    )
    he_100_A_slash_1_grade_s355: DefSection = DefSection(
        id=6,
        material=AllMaterial.grade_S355_isotropic_linear_elastic,
        section_type=SectionType.standardized_steel,
        manufacturing_type=ManufacturingType.hot_rolled,
        section_name="HE 100 A",
    )
