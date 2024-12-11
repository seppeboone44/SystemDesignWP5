



class Material:
    def __init__(self, id, name, tensile_strength, shear_strength,elastic_modulus, thermal_coef, density):

        self.id = id 
        self.name = name 
        self.tensile_strength = tensile_strength
        self.shear_strength = shear_strength
        self.elastic_modulus = elastic_modulus
        self.thermal_coef = thermal_coef
        self.density = density
        

    def __repr__(self):
        """
        Provide a string representation of the material for easy viewing.
        """
        return (f"Material {self.id}: {self.name}\n"
                f"  Tensile Yield Strength: {self.tensile_strength} MPa\n"
                f"  Shear Yield Strength: {self.shear_strength} MPa\n"
                f"  Elastic Modulus: {self.elastic_modulus} \n"
                f"  Thermal Coefficient: {self.thermal_coef} MPa\n"
                f"  Density: {self.density} kg/m³\n")


# Defining the 4 materials
materials = [
    Material(0, "7075 T6 Alluminium Alloy", 483*10**6, 331*10**6, 71.7*10**9, 23.6*10**(-6), 2810),   # properties
    Material(1, "2014 T6 Alluminium Alloy", 400*10**6, 290*10**6, 73.1*10**9, 23.6*10**(-6), 2800),
    Material(2, "SAE-AISI 4340 Steel", 470*10**6, 430*10**6, 200*10**9, 12.3*10**(-6), 7800),
    Material(3, "Aged Grade 250 Maraging Steel", 1740*10**6, 1060*10**6, 190*10**9, 10.1*10**(-6), 8200),
]



#print(materials[0].tensile_strength)