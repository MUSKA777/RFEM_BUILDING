from dataclasses import dataclass

@dataclass
class GradeS275:
    E = 205000  # Modulus of elasticity N/mm2
    G = 78846.2  # Shear modulus N/mm2
    v = 0.3  # Poisson's ratio
    specific_weight = 78.50  # kN/m3
    mass_density = 78.50  # kN/m3
    coefficient_of_thermal_ex = 0.000012  # 1/°C


@dataclass
class C20Slash25:
    E = 30000  # Modulus of elasticity N/mm2
    G = 12500  # Shear modulus N/mm2
    v = 0.2  # Poisson's ratio
    specific_weight = 25  # kN/m3
    mass_density = 2500  # kN/m3
    coefficient_of_thermal_ex = 0.00001  # 1/°C

@dataclass
class B500S_A:
    E = 200000  # Modulus of elasticity N/mm2
    G = 76923.1  # Shear modulus N/mm2
    v = 0.3  # Poisson's ratio
    specific_weight = 78.50  # kN/m3
    mass_density = 7850.00  # kN/m3
    coefficient_of_thermal_ex = 0.00001  # 1/°C

@dataclass
class MaterialName:
    grade_s275 = GradeS275()
    c20_slash_25= C20Slash25()
    b500s_a = B500S_A()

@dataclass
class MaterialType:
    basic: str = "Basic"
    reinforcing_steel: str = "Reinforcing Steel"


@dataclass
class MaterialModel:
    isotropic_linear_elastic = "Isotropic | Linear Elastic"
    surface_orthotropic_linear_elastic = "Orthotropic | Linear Elastic (Surfaces)"
    solids_orthotropic_linear_elastic = "Orthotropic | Linear Elastic (Solids)"

