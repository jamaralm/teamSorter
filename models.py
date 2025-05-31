class Player:
    def __init__(self, name, position, attributes):
        self.name = name
        self.position = position
        self.attributes = attributes
        self.overall = self.calculateOverall()

    def calculateOverall(self):
        weights = {
            "skill": 0.3,
            "speed": 0.15,
            "strength": 0.10,
            "vision": 0.2,
            "defense": 0.10,
            "attack": 0.10,
            "teamplay": 0.05,
        }

        overall = sum(self.attributes[_] * weights[_] for _ in weights)
        return round(overall, 2)

    def showStats(self):
        print("+" + "-"*38 + "+")
        print(f"| {'PLAYER STATS':^36} |")
        print("+" + "-"*38 + "+")
        print(f"| Name     : {self.name:<25} |")
        print(f"| Position : {self.position:<25} |")
        print(f"| Overall  : {self.overall:<25.2f} |")
        print("+" + "-"*38 + "+")
        print(f"| {'ATTRIBUTES':^36} |")
        print("+" + "-"*38 + "+")
        for attr, value in self.attributes.items():
            print(f"| {attr.capitalize():<10}: {value:<23} |")
        print("+" + "-"*38 + "+")