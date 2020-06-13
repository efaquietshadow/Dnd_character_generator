import random
from data import *


input('Welcome adventurer, enter your name: \n')


# Basic species, class and background
# Lists
race_list = data["races"]
class_list = data["classes"]
background_list = data["backgrounds"]
# background_list = ['Acolyte', 'Charlatan', 'Criminal', 'Entertainer', 'Folk Hero', 'Guild Artisan', 'Hermit', 'Noble', 'Outlander', 'Sage', 'Sailor', 'Soldier', 'Urchin']

# Random from lists
random_race = choose_race()
race_name = random_race['name']
first_letter_race = race_name[0:1].lower()
random_class = choose_class()
class_name = random_class['name']
random_background = choose_background()
background_name = random_background['name']
first_letter_background = background_name[0:1].lower()

# Making things work with a/an
output_string_race = "You are "
output_string_race += "an" if first_letter_race in ['a', 'e', 'i', 'o', 'u'] else "a"

output_string_background = "You grew up as "
output_string_background += "an" if first_letter_background in ['a', 'e', 'i', 'o', 'u'] else "a"

# output of basic section
your_character_basics = f"{output_string_race} {race_name} {class_name}. {output_string_background} {background_name}."

print(your_character_basics)


# Stat section
# Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma

player_stats = {
  "str": roll_stat(),
  "dex": roll_stat(),
  "con": roll_stat(),
  "int": roll_stat(),
  "wis": roll_stat(),
  "cha": roll_stat(),
}

# add bonus stats

race_bonus_list = []

race_bonuses = random_race['race_bonuses']
for stat, bonus in race_bonuses.items():
  if stat in stats_list:
    player_stats[stat] += bonus
    race_bonus_list.append(f"{stat.upper()} +{bonus}")  


# printing section fir stats
total_stats = str(player_stats["str"]).center(5) + str(player_stats["dex"]).center(5) + str(player_stats["con"]).center(5) + str(player_stats["int"]).center(5) + str(player_stats["wis"]).center(5) + str(player_stats["cha"]).center(5)

print("STR".center(5) + "DEX".center(5) + "CON".center(5) + "INT".center(5) + "WIS".center(5) + "CHA".center(5))
print(total_stats +"\n")

# print race gave you +bonus stat
print(f" Your {race_name} race bonus gave you {', '.join(race_bonus_list)}.\n") 

# TODO Pre generated stories down here



# descriptions of race and class

class_description = random_class["description"]

class_proficiencies = random_class["proficiencies"]

class_armor = class_proficiencies["armor"]

print(f" Your class is {class_name}, {class_description}")

print(f"Your proficiencies are: \n Armor: {class_armor}")