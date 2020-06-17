import random

data = {
    "races": {
        "dwarf": {
            "name": "Dwarf",
            "age": [13, 350],
            "alignment": ["lawful good", "lawful neutral", "lawful evil" "lawful good", "neutral good", "chaotic good"],
            "size": {
                "height": [4, 5],
                "weight": [100, 200],
            },
            "speed": 25,
            "appearance": {
                "hair": ["black", "gray", "brown", "red"],
                "skin": ["light brown", "deep tan", "deep brown", "pale tinged with red"],
            },
            "race_bonuses": {
                "con": 2
            },
            "sub_races": {
                "hill_dwarf": {
                    "sub_name": "Hill",
                    "race_bonuses": {
                        "wis": 1
                    },
                    "passive abilities": {
                        "dwarven_toughness": "Dwarven Toughness: Your hit point maximum increases by 1, and it increases by 1 every time you gain a level"
                    }
                },
                "mountain_dwarf": {
                    "sub_name": "Mountain",
                    "race_bonuses": {
                        "str": 2
                    },
                    "proficiencies": {
                        "armor": ["light armor", "medium armor"]
                    }
                }
            },
            "proficiencies": {
                "weapons": ['Battleaxe', 'Handaxe', 'Throwing hammer', 'Warhammer'],
                "tools": ['Smiths tools', 'Masons tools', 'Brewers supplies'],
                "languages": 'Dwarvish'
            },
            "darkvision": "true",
            "abilities": {
                "dwarven_resilience": "Dwarven Resilience: advantage on saving throws against poison, and resistance against poison damage",
                "stonecunning": " Stonecunning: Whenever you make an Intelligence (history) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus"
            },
        },
        "elf": {
            "name": "Elf",
            "age": [13, 750],
            "alignment": ["chaotic good", "chaotic neutral", "chaotic evil", "lawful good", "neutral good", "chaotic good"],
            "size": {
                "height": [5, 6.7],
            },
            "race_bonuses": {
                "dex": 2
            },
            "speed": 30,
            "sub_races": {
                "high_elf": {
                    "sub_name": "High",
                    "sub_race": {
                        "moon": {
                            "appearance": {
                                "hair": ["copper", "black", "golden blonde"],
                                "skin": "bronze",
                                "eyes": ["golden", "silver", "black"],
                            },
                        },
                        "sun": {
                            "appearance": {
                                "hair": ["silver-white", "black", "blue", "blonde", "brown", "red"],
                                "skin": ["alabaster", "alabaster tinged with blue"],
                                "eyes": ["blue", "green", "blue flecked with gold", "green flecked with gold"],
                            },
                        },
                    },
                    "race_bonuses": {
                        "int": 1
                    },
                    "proficiencies": {
                        "weapons": ["longsword", "shortsword", "shortbow", "longbow"],
                        # "languages": one of choice
                    },
                    "spells": {
                        # "cantip": one from wizard spell list
                    },
                },
                "wood_elf": {
                    "sub_name": "Wood",
                    "speed": 35,
                    "appearance": {
                        "hair": ["brown", "black", "copper", "blonde"],
                        "skin": ["copper", "copper with trace of green"],
                        "eyes": ["green", "brown", "hazel"]
                    },
                    "race_bonuses": {
                        "wis": 1
                    },
                    "proficiencies": {
                        "weapons": ["longsword", "shortsword", "shortbow", "longbow"]
                    },
                    "abilities": {
                        "mask_of_the_wild": "Mask of the Wild: You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist and other natural phenomena"
                    }
                },
                "dark_elf": {
                    "sub_name": "Drow",
                    "alignment": ["lawful evil", "neutral evil", "chaotic evil"],
                    "appearance": {
                        "hair": ["stark white", "pale yellow"],
                        "skin": "black",
                        "eyes": ["lilac", "silver", "pink", "pale red", "pale blue"]
                    },
                    "race_bonuses": {
                        "cha": 1
                    },
                    "proficiencies": {
                        "weapons": ["rapier", "shortsword", "hand crossbow"]
                    },
                    "abilities": {
                        "superior_darkvision": "Superior Darkvision: Your darkvision has a radius of 120 feet",
                        "sunlight_sensitivity": "Sunlight Sensitivity: You have disadvantage on attack rolls and on Wisdom (perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight"
                    },
                    "spells": {
                        "cantrips": {
                            # "dancing_lights":
                            # "faerie_fire":
                            # "darkness":
                        },
                    }
                }
            },
            "darkvision": "true",
            "proficiencies": {
                "skills": "Perception",
                "languages": 'Elvish'
            },
            "abilities": {
                "fey_ancestry": "Fey Ancestry: advantage on saving throws against being charmed, and magic can't put you to sleep",
                "trance": "Trance: elves don't need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.",
            }
        },
        "halfling": {
            "name": "Halfling",
            "age": [13, 150],
            "alignment": ["lawful good"],
            "size": {
                "height": 3,
                "weight": [40, 45],
                "size": "small"
            },
            "speed": 25,
            "appearance": {
                "hair": ["brown", "sandy brown"],
                "skin": ["tan", "pale with a ruddy cast"],
                "eyes": ["brown", "hazel"]
            },
            "race_bonuses": {
                "dex": 2
            },
            "sub_races": {
                "lightfoot": {
                    "sub_name": "Lightfoot",
                    "race_bonuses": {
                        "cha": 1
                    },
                    "abilities": {
                        "naturally_stealthy": "Naturally Stealthy: You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you"
                    }
                },
                "stout": {
                    "sub_name": "Stout",
                    "race_bonuses": {
                        "con": 1
                    },
                    "abilities": {
                        "stout_resilience": "Stout Resilience: You have advantage on saving throws against poison, and you have resistance against poison damage"
                    }
                }
            },
            "proficiencies": {
                "languages": 'Halfling'
            },
            "abilities": {
                "lucky": "Lucky: when you roll a 1 on an attack roll, ability check, or saving throw, you can reroll the die and must use the new roll",
                "halfling_nimbleness": "Hafling Nimbleness: You can move through the space of any creature that is of a size larger than yours",
            }
        },
        "human": {
            "name": "Human",
            "age": [13, 90],
            "alignment": [],
            "size": {
                "height": [4.8, 7],
            },
            "speed": 30,
            "appearance": {
                "hair": ["dusky brown", "brown", "blonde", "almost black", "raven black", "red", "light brown", "dark brown", "black"],
                "skin": ["dusky brown", "tawny", "fair", "amber", "dusky", "yellowish-bronze", "dark mahogany"],
                "eyes": ["dusky brown", "green", "brown", "blue", "steely gray", "hazel", "dark"]
            },
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
            "age": [4, 80],
            "alignment": ["lawful good", "neutral good", "chaotic good", "lawful evil", "neutral evil", "chaotic evil"],
            "size": {
                "height": 6,
                "weight": 250
            },
            "speed": 30,
            "race_bonuses": {
                "str":2,
                "cha":1
            },
            "draconic_ancestry": {
                "black": {
                    "name": "Black",
                    "damage_type": "Acid",
                    "breath_weapon": "5 by 30 ft line (dex. save)"
                },
                "blue": {
                    "name": "Blue",
                    "damage_type": "Lightning",
                    "breath_weapon": "5 by 30 ft line (dex. save)"
                },
                "brass": {
                    "name": "Brass",
                    "damage_type": "fire",
                    "breath_weapon": "5 by 30 ft line (dex save)"
                },
                "bronze": {
                    "name": "Bronze",
                    "damage_type": "Lightning",
                    "breath_weapon": "5 by 30 ft line (dex save)"
                },
                "copper": {
                    "name": "Copper",
                    "damage_type": "Acid",
                    "breath_weapon": "5 by 30 ft line (dex save)"
                },
                "gold": {
                    "name": "Gold",
                    "damage_type": "Fire",
                    "breath_weapon": "15 ft cone (dex save)"
                },
                "green": {
                    "name": "Green",
                    "damage_type": "Poison",
                    "breath_weapon": "15 ft cone (con save)"
                },
                "red": {
                    "name": "Red",
                    "damage_type": "Fire",
                    "breath_weapon": "15 ft cone (dex save)"
                },
                "Silver": {
                    "name": "Silver",
                    "damage_type": "Cold",
                    "breath_weapon": "15 ft cone (con save)"
                },
                "White": {
                    "name": "White",
                    "damage_type": "Cold",
                    "breath_weapon": "15 ft cone (con save)"
                },
            },
            "proficiencies": {
                "languages": 'Draconic'
            },
            "abilities": {
                "breath_weapon": "Breath Weapon: You can use your action to exhale destructive energy. Your dragonic ancestery determines the size, shape, and damage type of the exhalation. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw. The DC for this saving throw equals 8+ your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increases to 3d6 at 6th level, 4d6 at 11th level, and 5d6 at 16th level. After you use your breath weapon, you can't use it again until you complete a short or long rest",
                "damage resistance": "You have resistance to the damage type associated with your draconic ancestry"
            },
        },
        "gnome": {
            "name": "Gnome",
            "age": [13, 500],
            "alignment": ["lawful good", "neutral good", "chaotic good"],
            "size": {
                "height": [3, 4],
                "weight": [40, 45],
                "size": "small"
            },
            "appearance": {
                "skin": ["tan", "brown"],
                "hair": "fair",
                "eyes": "bright",
            },
            "speed": 25,
            "race_bonuses": {
                "int":2
            },
            "sub_races": {
                "forest_gnome": {
                    "sub_name": "Forest",
                    "race_bonuses": {
                        "dex": 1
                    },
                    "abilities": {
                        "speak_with_small_beasts": "Speak with small beasts: Through sounds and gestures, you can communicate simple ideas with Small or smaller beasts. Forest gnomes love animals and often keep squirrels, badgers, rabbits, moles, woodpeckers, and other creatures as beloved pets",
                    },
                    "spells": {
                        # "cantrips": minor illusion
                    }
                },
                "rock_gnome": {
                    "sub_name": "Rock",
                    "race_bonuses": {
                        "con": 1
                    },
                    "abilities": {
                        "artificers_lore": "Artificer's Lore: Whenever you make an Intellgence (history) check related to magic items, alchemical objects or technological devices, you can add twice your proficiency bonus, instead of any proficiency bonus you normally apply",
                        "tinker": "Tinker: You have proficiency with artisan's tools(tinkers tools). Using these tools, you can spend 1 hour and 10gp worth of materials to construct a Tiny clockwork device(AC 5, 1hp). The device ceases to function after 24 hours (unles you spend 1 hour repairing it to keep the device functioning), or when you use your action to dismantle it; at that time, you can reclaim the materials used to create it. You can have up to three such devices active at a time. \n when you create a device, choose one of the following options: \n Clockwork Toy. This toy is a clockwork animal, monster, or person, such as a frog, mouse, bird, dragon, or soldier. When placed on the ground, the toy moved 5 feet across the ground on each of your turns in a random direction. It makes noises as appropriate to the creature it represents. \n Fire Starter. The device produces a miniature flame, which you can use to light a candle, torch, or campire. Using the device requires your action. \n Music Box. When opened, this music box plays a single song at a moderate volume. The box stops playing when it reaches the song's end or when it is closed.",
                    }
                }
            },
            "darkvision": "true",
            "proficiencies": {
                "languages": 'Gnomish'
            },
            "abilities": {
                "gnome_cunning": "Gnome Cunning: You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic",
            },
        },
        "half-elf": {
            "name": "Half-elf",
            "age": [13, 180],
            "alignment": ["chaotic good", "chaotic neutral", "chaotic evil"],
            "size": {
                "height": [4.5, 6],
                "weight": [100, 180]
            },
            "speed": 30,
            "appearance": {
                "hair": ["copper","silver-white", "blue", "red" "black", "golden blonde", "dusky brown", "brown", "blonde", "almost black", "raven black", "red", "light brown", "dark brown", "black", "stark white", "pale yellow"],
                "skin": ["bronze", "alabaster", "alabaster tinged with blue", "black" ,"dusky brown", "tawny", "fair", "amber", "dusky", "yellowish-bronze", "dark mahogany", "copper", "copper with trace of green"],
                "eyes": ["golden", "silver", "black", "blue flecked with gold", "green flecked with gold", "dusky brown", "green", "brown", "blue", "steely gray", "hazel", "dark", "lilac", "silver", "pink", "pale red", "pale blue"],
            },
            "race_bonuses": {
                "cha": 2,
                "choice": [1, 1]
            },
            "darkvision": "true",
            "proficiencies": {
                # "skills": two of choice
                "languages": "elvish" #one of choice 
            },
            "abilities": {
                "fey_ancestry": "Fey ancestry: You have advantage on saving throws against being charmed, and magic can't put you to sleep"
            }
        },
        "half-orc": {
            "name": "Half-orc",
            "age": [10, 75],
            "alignment": ["chaotic good", "chaotic neutral", "chaotic evil", "neutral", "lawful neutral", "chaotic neutral", "lawful evil", "neutral evil", "chaotic evil"],
            "size": {
                "height": [5, 7],
                "weight": [180, 250]
            },
            "speed": 30,
            "race_bonuses": {
                "str": 2,
                "con": 1
            },
            "darvision": "true",
            "proficiencies": {
                "skills": "intimidation",
                "languages": "orc"
            },
            "abilities": {
                "relentless_endurance": "Relentless Endurance: When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can't use this featurea again until you finish a long rest.",
                "savage_attacks": "Savage Attacks: When you score a critical hit with a melle weapon attack, you can roll one of the weapons damage dice one additional time and add it to the extra damage of the critical hit."
            }
        },
        "tiefling": {
            "name": "Tiefling",
            "age": [13, 100],
            "alignment": ["lawful evil", "neutral evil", "chaotic evil", "chaotic good", "chaotic neutral", "chaotic evil"],
            "speed": 30,
            "appearance": {
                "hair": ["black", "brown", "dark red", "blue", "purple"],
                "skin": ["red", "pale red", "dark red", "dusky brown", "tawny", "fair", "amber", "dusky", "yellowish-bronze", "dark mahogany"],
                "eyes": ["black", "red", "white", "silver", "gold"]
            },
            "race_bonuses": {
                "int": 1,
                "cha": 2
            },
            "darkvision": "true",
            "proficiencies": {
                "languages": "infernal"
            },
            "abilities": {
                "hellish_resistance": "Hellish Resistance: You have resistance to fire damage"
            },
            "spells": {
                # thaumaturgry, hellish rebuke, darkness
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
            "proficiencies": {
                "armor": "light armor",
                "weapons": ["simple weapons", "hand crossbows", "longswords", "rapiers", "shortswords"],
                # "tools": three musical instruments
            }
        },
        "cleric": {
            "name":"Cleric",
            "description":"a priestly champion who wields divine magic in service of a higher power",
            "proficiencies": {
                "armor": ["light armor", "medium armor", "shields"],
                "weapons": "simple weapons"
            }
        },
        "druid": {
            "name":"Druid",
            "description":"a priest of the Old Faith, wielding the powers of nature-moonlight and plant growth, fire and lightning-and adopting animal forms ",
            "proficiencies": {
                "armor": ["light armor", "medium armor", "shields"], #nothing metal
                "weapons": ["clubs", "daggers", "darts", "javelins", "maces", "quarterstaffs", "scimitars", "sickles", "slings", "spears"],
                "tools": "herbalism kit"
            }
        },
        "fighter": {
            "name":"Fighter",
            "description":"a master of martial combal, skilled with a variety of weapons and armor",
            "proficiencies": {
                "armor": ["all armor", "shields"],
                "weapons": ["simple weapons", "martial weapons"]
            }
        },
        "monk": {
            "name":"Monk",
            "description":"a master of martial arts, harnessing the power of the body in pursuit of physical and spiritual perfection",
            "proficiencies": {
                "weapons":["simple weapons", "shortswords"],
                # "tools": one artisan or one musical instrument
            }
        },
        "paladin": {
            "name":"Paladin",
            "description":"a holy warrior bound to a sacred oath",
            "proficiencies": {
                "armor": ["all armor", "shields"],
                "weapons": ["simple weapons", "martial weapons"]
            }
        },
        "ranger": {
            "name":"Ranger",
            "description":"a warrior who uses martial prowess and nature magic to combat threats on the edges of civilization",
            "proficiencies": {
                "armor": ["light armor", "medium armor", "shields"],
                "weapons": ["simple weapons", "martial weapons"]
            }
        },
        "rouge": {
            "name":"Rouge",
            "description":"a scoundrel who uses stealth and trickery to overcome obstaces and enemies",
            "proficiencies": {
                "armor": "light armor",
                "weapons": ["simple weapons", "hand crossbows", "longswords", "rapiers", "shortswords"],
                "tools": "thieves tools"
            }
        },
        "sorcerer": {
            "name":"Sorcerer",
            "description":"a spellcasler who draws on inherent magic from a gift or bloodline",
            "proficiencies": {
                "weapons": ["daggers", "darts", "slings", "quarterstaffs", "light crossbows"]
            }
        },
        "warlock": {
            "name":"Warlock",
            "description":"a wielder of magic that is derived from a bargain with an extraplanar entity",
            "proficiencies": {
                "armor": "light armor",
                "weapons": "simple weapons"
            }
        },
        "wizard": {
            "name":"Wizard",
            "description":"a scholarly magic-user capable of manipulating the structures of reality",
            "proficiencies": {
                "weapons": ["daggers", "darts", "slings", "quarterstaffs", "light crossbows"]
            }
        }
    },
    "backgrounds": {
        "acolyte": {
            "name":"Acolyte",
            "proficiencies": {
                "skills": ["insight", "religion"],
                # two languages
            }
        },
        "charlatan": {
            "name":"Charlatan",
            "proficiencies": {
                "skills": ["deception", "sleight of hand"],
                "tools": ["disguise kit", "forgery kit"]
            }
        },
        "criminal": {
            "name":"Criminal",
            "proficiencies": {
                "skills": ["deception", "stealth"],
                "tools": ["thieves tools"] #one gaming set
            }
        },
        "entertainer": {
            "name":"Entertainer",
            "proficiencies": {
                "skills": ["acrobatics", "performance"],
                "tools": ["disguise kit"] #one musical instrament
            }
        },
        "folk_hero": {
            "name":"Folk Hero",
            "proficiencies": {
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
            "proficiencies": {
                "skills": ["athletics", "intimidation"],
                "tools": ["vehicles(land)"] #gaming set
            }
        },
        "urchin": {
            "name":"Urchin",
            "proficiencies": {
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