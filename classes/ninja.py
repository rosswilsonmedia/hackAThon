class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100

    def show_stats( self ):
        if self.health<0:
            self.health=0
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        return self
    def quickAttack( self , pirate ):
        if self.speed>pirate.speed:
            pirate.health-=5
            self.speed-=2
            print(f"Attack successful, you were quick as a ninja\n{self.name} loses two speed\n{pirate.name} loses five health\n")
        else:
            self.health-=pirate.strength
            print(f"Attack failed, you weren't quick enough\n{self.name} loses {pirate.strength} health\n")
        return self
    def heavyAttack( self , pirate ):
        if self.strength>pirate.strength:
            pirate.health -= 15
            self.strength-=5
            print(f"Attack successful, you were strong as a ninja\n{self.name} loses five strength\n{pirate.name} loses fifteen health\n")
        else:
            self.health-=pirate.strength
            print(f"Attack failed, you weren't strong enough\n{self.name} loses {pirate.strength} health\n")
        return self
    def recover(self):
        self.speed+=1
        self.strength+=1
        print(f'Recovering...\n{self.name} gains 1 speed\n{self.name} gains 1 strength\n')

class Elite(Ninja):
    def __init__( self , name ):
        self.name = name
        self.strength = 25
        self.speed = 15
        self.health = 100