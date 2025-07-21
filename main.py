import random

def setAge():
    return random.randint(18, 50) # Assuming possible age between 18 and 50


class Unit:
    def __init__(self, type, power, training_gain, training_cost):
        self.type = type
        self.power = power
        self.training_gain = training_gain
        self.training_cost = training_cost
        self.age = setAge()

    def __str__(self):
        return f"{self.type} (Power: {self.power}, Age: {self.age})"


class Pikeman(Unit):
    
    def __init__(self):
        super().__init__("Pikeman", 5, 3, 10)
        self.transform_cost = 30

    def transform(self):
        self.type = "Archer"
        self.power = 10
        self.training_gain = 7
        self.training_cost = 20
        self.transform_cost = 40
        return self
 
class Archer(Unit):
    
    def __init__(self):
        super().__init__("Archer", 10, 7, 20)
        self.transform_cost = 40

    def transform(self):
        self.type = "Knight"
        self.power = 20
        self.training_gain = 10
        self.training_cost = 30
        self.transform_cost = 50
        return self

class Knight(Unit):
    
    def __init__(self):
        super().__init__("Knight", 20, 10, 30)

    def transform(self):
        return 0


class Army:
    def __init__(self,civilization):
        self.gold = 1000
        self.civilization = civilization
        self.history = []
        self.units = self.setUnits()
    @property
    def force(self):
        return sum(unit.power for unit_list in self.units.values() for unit in unit_list)


    def __str__(self):
        result = f"Army of {self.civilization} with {self.gold} gold.\n Historic:{self.history} \n Units:\n"
        for unit_type, unit_list in self.units.items():
            result += f"  {unit_type} ({len(unit_list)}):\n"
            for unit in unit_list:
                result += f"    - {unit}\n"
        return result

    def setUnits(self):
        if(self.civilization == "Chinese"):
            return {
                "Pikemen": [Pikeman() for i in range(2)],
                "Archers": [Archer() for i in range(25)],
                "Knights": [Knight() for i in range(2)]
            }
        elif(self.civilization == "English"):
            return {
                "Pikemen": [Pikeman() for i in range(10)],
                "Archers": [Archer() for i in range(10)],
                "Knights": [Knight() for i in range(10)]
            }
        elif(self.civilization == "Byzantine"):
            return {
                "Pikemen": [Pikeman() for i in range(5)],
                "Archers": [Archer() for i in range(8)],
                "Knights": [Knight() for i in range(15)]
            }
        
    def trainUnit(self, unit):
        if self.gold >= unit.training_cost:
            self.gold = self.gold - unit.training_cost
            unit.power = unit.power + unit.training_gain


    def transformUnit(self, unit):
        if unit.type != "Knight":
            if self.gold >= unit.transform_cost:
                self.gold = self.gold - unit.transform_cost
                if (unit.type == "Pikeman"):
                    self.units["Pikemen"].remove(unit)
                    self.units["Archers"].append(unit.transform())
                else:
                    self.units["Archers"].remove(unit)
                    self.units["Knights"].append(unit.transform())

    

    def battle(self, enemy_army):
        if self.force > enemy_army.force:
            self.win_battle()
            enemy_army.lose_battle()
        elif self.force < enemy_army.force:
            self.lose_battle()
            enemy_army.win_battle()
        else:
            self.draw_battle()
            enemy_army.draw_battle()    
        
    def win_battle(self):
        self.gold = self.gold + 100
        self.history.append("Victory")


    def lose_battle(self):
        self.history.append("Defeat")
        for i in range(2):
            most_powerful_unit = None
            max_power = 0
            max_list = None

            for unit_list in self.units.values():
                for unit in unit_list:
                    if unit.power > max_power:
                        max_power = unit.power
                        most_powerful_unit = unit
                        max_list = unit_list

            max_list.remove(most_powerful_unit)


    
    def draw_battle(self): # The older unit and the one with less power is removed
        self.history.append("Draw")
        older_unit = None
        max_age = 0
        older_list = None
        for unit_list in self.units.values():
            for unit in unit_list:
                if unit.age > max_age:
                    max_age = unit.age
                    older_unit = unit
                    older_list = unit_list
                elif unit.age == max_age and unit.power < older_unit.power:
                    max_age = unit.age
                    older_unit = unit
                    older_list = unit_list
        older_list.remove(older_unit)







                    
    



