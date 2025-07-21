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
        self.historic = []
        self.units = self.setUnits()
        self.plane_units = [unit for unit_list in self.units.values() for unit in unit_list]
        self.power = self.getPower()

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

    def getPower(self):
        return sum(unit.power for unit_list in self.units.values() for unit in unit_list)


    def battle(self, enemy_army):
        if self.power > enemy_army.power:
            self.win_battle()
            self.historic.append("Victory against " + enemy_army.civilization)
            enemy_army.lose_battle()
            enemy_army.historic.append("Defeat against " + enemy_army.civilization)
        elif self.power < enemy_army.power:
            self.lose_battle()
            self.historic.append("Defeat against " + enemy_army.civilization)
            enemy_army.win_battle()
            enemy_army.historic.append("Victory against " + self.civilization)
        else:
            self.historic.append("Draw against " + enemy_army.civilization)
            enemy_army.historic.append("Draw against " + self.civilization)
        
    def win_battle(self):
        self.gold = self.gold + 100


    def lose_battle(self):
        

        

    def draw_battle(self):
        lost_unity = random.choice(self.units)
        print(f"Lost unit: {lost_unity}")
        self.units.remove(lost_unity)









army = Army("Chinese")
print(army)
x = army.units["Knights"][0]
print(x)
army.trainUnit(x)
print(x)
army.transformUnit(x)
print(x)
print(army)
army.lose_battle()
print(army)
                    
    



