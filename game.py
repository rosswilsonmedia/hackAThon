from classes.ninja import Ninja, Elite
from classes.pirate import Pirate

print("\nNinjas vs Pirates\n")
character=''
while character=='':
    character=input('Choose your ninja, Michelangelo or Donatello?\n')
    character=character.lower()
    if character=='michelangelo':
        character=Ninja("Michelanglo")
    elif character=='donatello':
        character=Elite("Donatello")
    else:
        print('Not a valid command, please try again\n')
        character=''

jack_sparrow = Pirate("Jack Sparrow")

print(f"Greetings {character.name}! Welcome to our deserted island! Feel free to explore the area!\n")
character.show_stats()
print("A drunken pirate appears, making fun of you. He calls himself 'Captain Jack Sparrow' though no ship or crew seem to be present. He continues stumbling towards you, saying that he's going to kill you!\n")
jack_sparrow.show_stats()

while character.health>0 and jack_sparrow.health>0:
    attack=input('Would you like to quick attack(Q) or heavy attack(H) the pirate?\n')
    if attack.upper()=='Q':
        character.quickAttack(jack_sparrow)
    elif attack.upper()=='H':
        character.heavyAttack(jack_sparrow)
    else:
        print('Not a valid command, please try again\n')
        continue
    character.recover()
    character.show_stats()
    jack_sparrow.show_stats()
if jack_sparrow.health<=0:
    print('You have defeated the pirate! Live long and prosper!')
else:
    print('You have lost, the ninja turtles shall miss you')