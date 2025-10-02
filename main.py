from pokemon import Pokemon
from moves import Move

# Create moves
tackle = Move("Tackle", 10)
ember = Move("Ember", 12)
vine_whip = Move("Vine Whip", 12)
water_gun = Move("Water Gun", 12)

# Create Pokemon
bulbasaur = Pokemon("Bulbasaur", "Grass", moves=[tackle, vine_whip])
charmander = Pokemon("Charmander", "Fire", moves=[tackle, ember])
squirtle = Pokemon("Squirtle", "Water", moves=[tackle, water_gun])


# Battle test
bulbasaur.attack(charmander, vine_whip)
charmander.attack(bulbasaur, ember)

print(bulbasaur.info())
print(charmander.info())