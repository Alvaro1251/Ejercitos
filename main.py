import random

def setAge():
    return random.randint(18, 50) # I assume possible age between 18 and 50

class Pikeman:
    
    def __init__(self):
        self.type = "Pikeman"
        self.power = 5
        self.age = setAge()

    def __str__(self):
        return f"{self.type} (Power: {self.power}, Age: {self.age})"
 
class Archer:
    
    def __init__(self):
        self.type = "Archer"
        self.power = 10
        self.age = setAge()
    
    def __str__(self):
        return f"{self.type} (Power: {self.power}, Age: {self.age})"

class Knight:
    
    def __init__(self):
        self.type = "Knight"
        self.power = 20
        self.age = setAge()
    
    def __str__(self):
        return f"{self.type} (Power: {self.power}, Age: {self.age})"


class Army:
    def __init__(self,civilization):
        self.gold = 1000
        self.civilization = civilization
        self.historic = []
        self.units = self.setUnits()

    def __str__(self):
        result = f"Army of {self.civilization} with {self.gold} gold.\n Units:\n"
        for unit_type, unit_list in self.units.items():
            result += f"  {unit_type} ({len(unit_list)}):\n"
            for unit in unit_list:
                result += f"    - {unit}\n"
        return result

    def setUnits(self):
        if(self.civilization == "Chinese"):
            return {
                "Pikemen": [Pikeman() for _ in range(2)],
                "Archers": [Archer() for _ in range(25)],
                "Knights": [Knight() for _ in range(2)]
            }
        if(self.civilization == "English"):
            return {
                "Pikemen": [Pikeman() for _ in range(10)],
                "Archers": [Archer() for _ in range(10)],
                "Knights": [Knight() for _ in range(10)]
            }
        if(self.civilization == "Byzantine"):
            return {
                "Pikemen": [Pikeman() for _ in range(5)],
                "Archers": [Archer() for _ in range(8)],
                "Knights": [Knight() for _ in range(15)]
            }
        elif self.civilization == "English":
            return {
                "Pikemen": [Pikeman() for _ in range(10)],
                "Archers": [Archer() for _ in range(10)],
                "Knights": [Knight() for _ in range(10)]
            }
        elif self.civilization == "Byzantine":
            return {
                "Pikemen": [Pikeman() for _ in range(5)],
                "Archers": [Archer() for _ in range(8)],
                "Knights": [Knight() for _ in range(15)]
            }



