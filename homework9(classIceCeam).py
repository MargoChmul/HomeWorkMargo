

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        pass
    def __str__(self) -> str:
        return f"Restaurant name: {self.restaurant_name} Cuisine type: {self.cuisine_type}"

class IceCreamStand( Restaurant ):
    
    def __init__(self, restaurant_name):
        super().__init__(restaurant_name, "Ice Cream")
        self.flavors = []
        self.containers = []
        self.sizes = []
    
    def __str__(self) -> str:
        return super().__str__() + f" flavors {self.flavors}, containers {self.containers}, sizes {self.sizes} "
    
stand = IceCreamStand("IceCream54thRestAvenue")
stand.sizes.append("S - one ball")
stand.sizes.append("M - two balls")
stand.sizes.append("L - three balls")
stand.sizes.append("XL - 5 balls")
stand.containers.append("IceCreamCone")
stand.containers.append("Cup")
stand.containers.append("Bowl")
stand.flavors.append("Ananas")
stand.flavors.append("Mokko")
stand.flavors.append("Lemon")
stand.flavors.append("Oreo")

print(stand)

