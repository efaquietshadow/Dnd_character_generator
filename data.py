import random

data = {
    "races": {
        "dwarf": {
            "name": "Dwarf",
            "race_bonuses": {
                "con": 2
            },
            "sub_races": {
                "hill_dwarf": {
                    "sub_name": "Hill",
                    "race_bonuses": {
                        "wis": 1
                    }
                },
                "mountain_dwarf": {
                    "sub_name": "Mountain",
                    "race_bonuses": {
                        "str": 2
                    }
                }
            },
            "proficiencies": {
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
            "sub_races": {
                "high_elf": {
                    "sub_name": "High",
                    "race_bonuses": {
                        "int": 1
                    },
                    "proficiencies": {
                        "weapons": ["longsword", "shortsword", "shortbow", "longbow"],
                        # "languages": one of choice
                    }
                },
                "wood_elf": {
                    "sub_name": "Wood",
                    "race_bonuses": {
                        "wis": 1
                    },
                    "proficiencies": {
                        "weapons": ["longsword", "shortsword", "shortbow", "longbow"]
                    }
                },
                "dark_elf": {
                    "sub_name": "Drow",
                    "race_bonuses": {
                        "cha": 1
                    },
                    "proficiencies": {
                        "weapons": ["rapier", "shortsword", "hand crossbow"]
                    }
                }
            },
            "proficiencies": {
                "skills": "Perception",
                "languages": 'Elvish'
            }
        },
        "halfling": {
            "name": "Halfling",
            "race_bonuses": {
                "dex": 2
            },
            "sub_races": {
                "lightfoot": {
                    "sub_name": "Lightfoot",
                    "race_bonuses": {
                        "cha": 1
                    }
                },
                "stout": {
                    "sub_name": "Stout",
                    "race_bonuses": {
                        "con": 1
                    }
                }
            },
            "proficiencies": {
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
            "proficiencies": {
                # "languages": maybe randomize between all the languages? Cause humans get to choose 1
            }
        },
        "dragonborn": {
            "name": "Dragonborn",
            "race_bonuses": {
                "str":2,
                "cha":1
            },
            "proficiencies": {
                "languages": 'Draconic'
            }
        },
        "gnome": {
            "name": "Gnome",
            "race_bonuses": {
                "int":2
            },
            "sub_races": {
                "forest_gnome": {
                    "sub_name": "Forest",
                    "race_bonuses": {
                        "dex": 1
                    }
                },
                "rock_gnome": {
                    "sub_name": "Rock",
                    "race_bonuses": {
                        "con": 1
                    }
                }
            },
            "proficiencies": {
                "languages": 'Gnomish'
            }
        },
        "half-elf": {
            "name": "Half-elf",
            "race_bonuses": {
                "cha": 2,
                "choice": [1, 1]
            },
            "proficiencies": {
                # "skills": two of choice
                "languages": "elvish" #one of choice 
            }
        },
        "half-orc": {
            "name": "Half-orc",
            "race_bonuses": {
                "str": 2,
                "con": 1
            },
            "proficiencies": {
                "skills": "intimidation",
                "languages": "orc"
            }
        },
        "tiefling": {
            "name": "Tiefling",
            "race_bonuses": {
                "int": 1,
                "cha": 2
            },
            "proficiencies": {
                "languages": "infernal"
            }
        }
    },
    "classes": {
        "barbarian": {
            "name":"Barbarian",
            "description":"a fierce warrior of primitive background who can enter a battle rage",
            "proficiencies": {
                "armor": ["light armor", "medium armor", "shields"],
                "weapons": ["simple weapons", "martial weapons"]
            }
        },
        "bard": {
            "name":"Bard",
            "description":"an inspiring magician whose power echoes the music of creation",
            "proficiences": {
                "armor": "light armor",
                "weapons": ["simple weapons", "hand crossbows", "longswords", "rapiers", "shortswords"],
                # "tools": three musical instruments
            }
        },
        "cleric": {
            "name":"Cleric",
            "description":"a priestly champion who wields divine magic in service of a higher power",
            "proficiences": {
                "armor": ["light armor", "medium armor", "shields"],
                "weapons": "simple weapons"
            }
        },
        "druid": {
            "name":"Druid",
            "description":"a priest of the Old Faith, wielding the powers of nature-moonlight and plant growth, fire and lightning-and adopting animal forms ",
            "proficiences": {
                "armor": ["light armor", "medium armor", "shields"], #nothing metal
                "weapons": ["clubs", "daggers", "darts", "javelins", "maces", "quarterstaffs", "scimitars", "sickles", "slings", "spears"],
                "tools": "herbalism kit"
            }
        },
        "fighter": {
            "name":"Fighter",
            "description":"a master of martial combal, skilled with a variety of weapons and armor",
            "proficiences": {
                "armor": ["all armor", "shields"],
                "weapons": ["simple weapons", "martial weapons"]
            }
        },
        "monk": {
            "name":"Monk",
            "description":"a master of martial arts, harnessing the power of the body in pursuit of physical and spiritual perfection",
            "proficiences": {
                "weapons":["simple weapons", "shortswords"],
                # "tools": one artisan or one musical instrument
            }
        },
        "paladin": {
            "name":"Paladin",
            "description":"a holy warrior bound to a sacred oath",
            "proficiences": {
                "armor": ["all armor", "shields"],
                "weapons": ["simple weapons", "martial weapons"]
            }
        },
        "ranger": {
            "name":"Ranger",
            "description":"a warrior who uses martial prowess and nature magic to combat threats on the edges of civilization",
            "proficiences": {
                "armor": ["light armor", "medium armor", "shields"],
                "weapons": ["simple weapons", "martial weapons"]
            }
        },
        "rouge": {
            "name":"Rouge",
            "description":"a scoundrel who uses stealth and trickery to overcome obstaces and enemies",
            "proficiences": {
                "armor": "light armor",
                "weapons": ["simple weapons", "hand crossbows", "longswords", "rapiers", "shortswords"],
                "tools": "thieves tools"
            }
        },
        "sorcerer": {
            "name":"Sorcerer",
            "description":"a spellcasler who draws on inherent magic from a gift or bloodline",
            "proficiences": {
                "weapons": ["daggers", "darts", "slings", "quarterstaffs", "light crossbows"]
            }
        },
        "warlock": {
            "name":"Warlock",
            "description":"a wielder of magic that is derived from a bargain with an extraplanar entity",
            "proficiences": {
                "armor": "light armor",
                "weapons": "simple weapons"
            }
        },
        "wizard": {
            "name":"Wizard",
            "description":"a scholarly magic-user capable of manipulating the structures of reality",
            "proficiences": {
                "weapons": ["daggers", "darts", "slings", "quarterstaffs", "light crossbows"]
            }
        }
    },
    "backgrounds": {
        "acolyte": {
            "name":"Acolyte",
            "proficiences": {
                "skills": ["insight", "religion"],
                # two languages
            }
        },
        "charlatan": {
            "name":"Charlatan",
            "proficiences": {
                "skills": ["deception", "sleight of hand"],
                "tools": ["disguise kit", "forgery kit"]
            }
        },
        "criminal": {
            "name":"Criminal",
            "proficiences": {
                "skills": ["deception", "stealth"],
                "tools": ["thieves tools"] #one gaming set
            }
        },
        "entertainer": {
            "name":"Entertainer",
            "proficiences": {
                "skills": ["acrobatics", "performance"],
                "tools": ["disguise kit"] #one musical instrament
            }
        },
        "folk_hero": {
            "name":"Folk Hero",
            "proficiences": {
                "skills": ["animal handling", "survival"],
                "tools": ["vehicles(land"] # one artisan tools
            }
        },
        "guild_artisan": {
            "name":"Guild Artisan",
            "proficiencies": {
                "skills": ["insight", "persuasion"],
                # tools, one of choice
                # languages one of choice
            }
        },
        "hermit": {
            "name":"Hermit",
            "proficiencies": {
                "skills": ["medicine", "religion"],
                "tools": "herbalism kit",
                # one language
            }
        },
        "noble": {
            "name":"Noble",
            "proficiencies": {
                "skills": ["history", "persuasion"],
                # one gaming set
                # one language
            }
        },
        "outlander": {
            "name":"Outlander",
            "proficiencies": {
                "skills": ["athletics", "survival"],
                # one musical instrument
                # one language
            }
        },
        "sage": {
            "name":"Sage",
            "proficiencies": {
                "skills": ["arcana", "history"],
                # two languages
            }
        },
        "sailor": {
            "name":"Sailor",
            "proficiencies": {
                "skills": ["athletics", "perception"],
                "tools": ["navigators tools", "vehicles(water)"]
            }
        },
        "soldier": {
            "name":"Soldier",
            "proficiences": {
                "skills": ["athletics", "intimidation"],
                "tools": ["vehicles(land)"] #gaming set
            }
        },
        "urchin": {
            "name":"Urchin",
            "proficiences": {
                "skills": ["sleight of hand", "stealth"],
                "tools": ["disguise kit", "thieves tools"]
            }
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