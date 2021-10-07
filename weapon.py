

class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        # self.weapon_choices = []

    # def weapon_builder(self):
    #     weapon1 = Weapon("Sword", 33)
    #     weapon2 = Weapon("AR-15", 24)
    #     weapon3 = Weapon("Knife", 15)
    #     self.weapon_choices.append[weapon1]
    #     self.weapon_choices.append[weapon2]
    #     self.weapon_choices.append[weapon3]
    #     for item in self.weapon_choices:
    #         print(item)

    
    def __str__(self):
        return ("Type: " + self.name)


# new = Weapon("mike", 22)
# new.weapon_builder()

