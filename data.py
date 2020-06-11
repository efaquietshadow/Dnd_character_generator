import random

data = {
    "races": {
        "dwarf": {
            "name": "Dwarf",
            "race_bonuses": {
                "con": 2
            },
            "proficiencys": {
                "weapons": ['Battleaxe', 'Handaxe', 'Throwing hammer', 'Warhammer'],
                "tools": ['Smiths tools', 'Masons tools', 'Brewers supplies'],
                "languages": 'Dwarvish'
            }
        },
        "elf": {
            "name": "Elf",
            "race_bonuses": {
                "dex": 2
            },
            "proficiencys": {
                "skills": "Perception",
                "languages": 'Elvish'
            }
        },
        "halfling": {
            "name": "Halfling",
            "race_bonuses": {
                "dex": 2
            },
            "proficiencys": {
                "languages": 'Halfling'
            }
        },
        "human": {
            "name": "Human",
            "race_bonuses": {
                "str":1,
                "dex":1,
                "con":1,
                "wis":1,
                "int":1,
                "cha":1
            },
            "proficiencys": {
                # "languages": maybe randomize between all the languages? Cause humans get to choose 1
            }
        },
        "dragonborn": {
            "name": "Dragonborn",
            "race_bonuses": {
                "str":2,
                "cha":1
            },
            "proficiencys": {
                "languages": 'Draconic'
            }
        },
        "gnome": {
            "name": "Gnome",
            "race_bonuses": {
                "int":2
            }
        },
        "half-elf": {
            "name": "Half-elf",
            "race_bonuses": {
                "cha": 2,
                "choice": [1, 1]
            }
        },
        "half-orc": {
            "name": "Half-orc",
            "race_bonuses": {
                "str": 2,
                "con": 1
            }
        },
        "tiefling": {
            "name": "Tiefling",
            "race_bonuses": {
                "int": 1,
                "cha": 2
            }
        }
    },
    "classes": {
        "barbarian": {
            "name":"Barbarian",
            "description":"This is a description of the Barbarian"
        },
        "bard": {
            "name":"Bard",
            "description":"This is a description of the Bard"
        },
        "cleric": {
            "name":"Cleric",
            "description":"This is a description of the Cleric"
        },
        "druid": {
            "name":"Druid",
            "description":"This is a description of the Druid"
        },
        "fighter": {
            "name":"Fighter",
            "description":"This is a description of the Fighter"
        },
        "monk": {
            "name":"Monk",
            "description":"This is a description of the Monk"
        },
        "paladin": {
            "name":"Paladin",
            "description":"This is a description of the Paladin"
        },
        "ranger": {
            "name":"Ranger",
            "description":"This is a description of the Ranger"
        },
        "rouge": {
            "name":"Rouge",
            "description":"This is a description of the Rouge"
        },
        "sorcerer": {
            "name":"Sorcerer",
            "description":"This is a description of the Sorcerer"
        },
        "warlock": {
            "name":"Warlock",
            "description":"This is a description of the Warlock"
        },
        "wizard": {
            "name":"Wizard",
            "description":"This is a description of the Wizard"
        }
    },
    "backgrounds": {
        "acolyte": {
            "name":"Acolyte"
        },
        "charlatan": {
            "name":"Charlatan"
        },
        "criminal": {
            "name":"Criminal"
        },
        "entertainer": {
            "name":"Entertainer"
        },
        "folk_hero": {
            "name":"Folk Hero"
        },
        "guild_artisan": {
            "name":"Guild Artisan"
        },
        "hermit": {
            "name":"Hermit"
        },
        "noble": {
            "name":"Noble"
        },
        "outlander": {
            "name":"Outlander"
        },
        "sage": {
            "name":"Sage"
        },
        "sailor": {
            "name":"Sailor"
        },
        "soldier": {
            "name":"Soldier"
        },
        "urchin": {
            "name":"Urchin"
        }
    }
}

stats_ch_map = {
    "s": "str",
    "d": "dex",
    "c": "con",
    "i": "int",
    "w": "wis",
    "h": "cha"
}

stats_list = ["str", "dex", "con", "int", "wis", "cha"]


def roll(num_sides):
    return random.randint(1,num_sides)

def roll_stat():
    rolls = []
    for _ in range(4):
        rolls.append(roll(6))
    return sum(rolls) - min(rolls)

def choose_race():
    return data["races"][random.choice(list(data["races"].keys()))]

def choose_class():
    return data["classes"][random.choice(list(data["classes"].keys()))]

def choose_background():
    return data["backgrounds"][random.choice(list(data["backgrounds"].keys()))]