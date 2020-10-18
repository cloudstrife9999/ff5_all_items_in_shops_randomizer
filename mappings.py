from typing import Dict, Union, List



shop_types: Dict[str, int] = {
    "magic": 0x00,
    "weapon": 0x01,
    "armor": 0x02,
    "item": 0x03,
    "accessory": 0x04,
    "throwable": 0x05, # Weapons + Throwable items (flame/water/thunder scroll)
    "item_with_elixir": 0x06, # Items + Elixir
    "job": 0x07,
    "karnak_weapon_shop_before_getting_arrested": 0x81,
    "karnak_armor_shop_before_getting_arrested": 0x82,
    "cheap_item": 0x83
}


useful_shop_types: list = [0x00, 0x01, 0x02, 0x03, 0x04, 0x07]


weapon_codes: List[int] = [
    0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F,
    0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F,
    0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2A, 0x2B, 0x2C, 0x2D, 0x2E, 0x2F,
    0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x3A, 0x3B, 0x3C, 0x3D, 0x3E, 0x3F,
    0x40, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4A, 0x4B, 0x4C, 0x4D, 0x4E, 0x4F,
    0x50, 0x51, 0x52, 0x53, 0x54, 0x55, 0x56, 0x57, 0x58, 0x59, 0x5A, 0x5B, 0x5C, 0x5D, 0x5E, 0x5F,
    0x60, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6A, 0x6B, 0x6C, 0x6D, 0x6E
]


armor_codes: List[int] = [
    0x81, 0x82, 0x83, 0x84, 0x85, 0x86, 0x87, 0x88, 0x89, 0x8A, 0x8B, 0x8C, 0x8D, 0x8E, 0x8F, 0x90,
    0x91, 0x92, 0x93, 0x94, 0x95, 0x96, 0x97, 0x98, 0x99, 0x9A, 0x9B, 0x9C, 0x9D, 0x9E, 0x9F, 0xA0,
    0xA1, 0xA2, 0xA3, 0xA4, 0xA5, 0xA6, 0xA7, 0xA8, 0xA9, 0xAA, 0xAB, 0xAC, 0xAD, 0xAE, 0xB9, 0xBB,
    0xBF, 0xC3, 0xC4, 0xC6, 0xC7, 0xC8, 0xCB, 0xCC, 0xCD, 0xCE, 0xCF
]


accessory_codes: List[int] = [
    0xAF, 0xB0, 0xB1, 0xB2, 0xB3, 0xB4, 0xB5, 0xB6, 0xB7, 0xB8, 0xBA, 0xBC, 0xBD, 0xBE, 0xC0, 0xC1,
    0xC2, 0xC5, 0xC9, 0xCA, 0xD0
]


item_codes: List[int] = [
    0xE0, 0xE1, 0xE2, 0xE3, 0xE4, 0xE5, 0xE6, 0xE7, 0xE8, 0xE9, 0xEA, 0xEB, 0xEC, 0xED, 0xEF, 0xF0,
    0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE
]


# 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10, 0x11
magic_codes: List[int] = [
    0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F, 0x20,
    0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2A, 0x2B, 0x2C, 0x2D, 0x2E, 0x2F, 0x30,
    0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x3A, 0x3B, 0x3C, 0x3D, 0x3E, 0x3F, 0x40,
    0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4A, 0x4B, 0x4C, 0x4D, 0x4E, 0x4F, 0x50,
    0x51, 0x52, 0x53, 0x54, 0x55, 0x56, 0x57, 0x58, 0x59, 0x5A, 0x5B, 0x5C, 0x5D, 0x5E, 0x82, 0x83,
    0x84, 0x85, 0x86, 0x87, 0x88, 0x89, 0x8A, 0x8B, 0x8C, 0x8D, 0x8E, 0x8F, 0x90, 0x91, 0x92, 0x93,
    0x94, 0x95, 0x96, 0x97, 0x98, 0x99, 0x9A, 0x9B, 0x9C, 0x9D, 0x9E, 0x9F
]


job_codes: List[int] = [
    0x89, 0x8A, 0x8B, 0x8C, 0x8D, 0x8E, 0x8F, 0x90, 0x91, 0x92, 0x93, 0x94, 0x95, 0x96, 0x97, 0x98,
    0x99, 0x9A, 0x9B, 0x9C, 0x9D, 0x9E
]


weapons: Dict["str", Dict["str", int]] = {
    "knives": {
        "sabre": 0x54, # Dummied out, and not equippable by any job class. Attack power --> unknown.
        "knife": 0x02,
        "dagger": 0x03,
        "mythril_dagger": 0x04,
        "mage_masher": 0x06,
        "guardian": 0x07, # main_gauche
        "orialcon": 0x09, # orichalcon
        "dancing_dagger": 0x6D,
        "air_lance": 0x0A, # air lancet
        "thief_knife": 0x6C,
        "assassin": 0x0B,
        "chicken_knife": 0x63
    },

    "ninja_swords": {
        "kunai": 0x05,
        "kodachi": 0x08,
        "hardened": 0x0C # sakuke
    },

    "swords": {
        "broadsword": 0x0D,
        "regal_cut": 0x0E, # long sword
        "mythril_sword": 0x0F,
        "coral_sword": 0x10,
        "ancient_sword": 0x11,
        "slumber": 0x13, # Not a mistake --> the order is inverted.
        "rune__edge": 0x56,
        "epee": 0x12, # Not a mistake --> the order is inverted.
        "excailbur": 0x5C, # excalipoor
        "enhancer": 0x6E
    },

    "knight_swords": {
        "flametongue": 0x57,
        "icebrand": 0x58,
        "drain_sword": 0x55, # blood sword
        "defender": 0x14,
        "excalibur": 0x15,
        "ragnarok": 0x16,
        "brave_blade": 0x61
    },

    "spears": {
        "spear": 0x18,
        "mythril_spear": 0x19,
        "trident": 0x1A,
        "wind_spear": 0x1B,
        "gungnir": 0x1D,
        "javelin": 0x17,
        "partisan": 0x1C,
        "holy_lance": 0x1F,
        "dragoon_lance": 0x20
    },

    "axes": {
        "battle_axe": 0x21,
        "ogre_killer": 0x23,
        "doom_cut": 0x69, # death sickle
        "venom_axe": 0x25,
        "rune_axe": 0x27,
        "giants_axe": 0x6A # titan axe - double axe
    },

    "hammers": {
        "mythril_hammer": 0x22,
        "war_hammer": 0x24,
        "earth_hammer": 0x26,
        "thor_hammer": 0x28
    },

    "katanas": {
        "katana": 0x29, # ashura
        "air_blade": 0x2A,
        "bizen": 0x2C, # Not a mistake --> the order is inverted. Also known as osafune.
        "kotetsu": 0x2B, # Not a mistake --> the order is inverted.
        "forged": 0x2D, # ichimonchi
        "murasame": 0x2E,
        "masamune": 0x2F,
        "tempest": 0x30 # murakumo
    },

    "rods" : {
        "wonder_wand": 0x60,
        "rod": 0x31,
        "fire_rod": 0x32,
        "ice_rod": 0x33,
        "thunder_rod": 0x34,
        "lilith_rod": 0x36, # Not a mistake --> the order is inverted.
        "venom_rod": 0x35, # Not a mistake --> the order is inverted.
        "wizard_rod": 0x37
    },

    "staves": {
        "power_staff": 0x3A,
        "healing_staff": 0x3B,
        "staff": 0x38,
        "mythril_staff": 0x39,
        "staff_of_light": 0x3C,
        "sages_staff": 0x3D,
        "judgement_staff": 0x3E
    },

    "bows": {
        "antimagic_bow": 0x67,
        "silver_bow": 0x65,
        "fire_bow": 0x3F,
        "ice_bow": 0x40,
        "thunder_bow": 0x41,
        "darkness_bow": 0x42,
        "killer_bow": 0x43,
        "elven_bow": 0x44,
        "gale_bow": 0x66,
        "avis_killer": 0x68,
        "yoichi_bow": 0x45,
        "artemis_bow": 0x46
    },

    "harps": {
        "silver_harp": 0x47,
        "dream_harp": 0x48,
        "lamias_harp": 0x49,
        "apollos_harp": 0x4A
    },

    "whips": {
        "whip": 0x4B,
        "thunder_whip": 0x4D, # Not a mistake --> the order is inverted.
        "chain_whip": 0x4C, # Not a mistake --> the order is inverted.
        "beastkiller": 0x5D,
        "flame_whip": 0x4E,
        "dragon_whip": 0x4F,
    },

    "bells": {
        "giyaman": 0x50, # diamond bell
        "earth_bell": 0x51,
        "rune_chime": 0x52,
        "tinkerbell": 0x53,
    },

    "shurikens": { # Does not include the scrolls, as they are categorised as items.
        "soot": 0x62, # ash
        "shuriken": 0x5A,
        "pinwheel": 0x5B # fuma shuriken
    },

    "boomerangs": {
        "full_moon": 0x59,
        "rising_sun": 0x64,
        "double_lance": 0x1E
    },

    "maces": {
        "flail": 0x5E,
        "morning_star": 0x5F
    },

    "dancer_weapons": {
        "man_eater": 0x6B
    }
}


armors: Dict[str, Dict[str, Union[int, Dict[str, int]]]] = {
    "shields": {
        "heavy": {
            "cursed_shield": 0xCE,
            "leather_shield": 0x81,
            "bronze_shield": 0x82,
            "iron_shield": 0x83,
            "mythril_shield": 0x84,
            "golden_shield": 0x85,
            "aegis_shield": 0x86,
            "diamond_shield": 0x87,
            "flame_shield": 0xC4,
            "ice_shield": 0xCD,
            "crystal_shield": 0x88,
            "genji_shield": 0xC6
        }
    },
    "head": {
        "light": {
            "leather_cap": 0x89,
            "green_beret": 0x97,
            "bandana": 0x96,
            "tiger_mask": 0xC3,
            "darkhood": 0x98
        },
        "magic": {
            "goldpin": 0x94, # gold hairpin
            "plumed_hat": 0x90,
            "lamias_tiara": 0x99,
            "tricorn": 0x91,
            "coronet": 0xCB,
            "magus": 0x92,
            "circlet": 0x93,
            "ribbon": 0x95
        },
        "heavy": {
            "bronze_helm": 0x8A,
            "iron_helm": 0x8B,
            "mythril_helm": 0x8C,
            "golden_helm": 0x8D,
            "diamond_helm": 0x8E,
            "crystal_helm": 0x8F,
            "genji_helm": 0xC7,
            "thornlet": 0xCC
        }
    },
    "body": {
        "light": {
            "leather_armor": 0x9A,
            "copperplt": 0xA1,
            "training_suit": 0xA2,
            "silver_plate": 0xA3,
            "stealth_suit": 0xA4,
            "strength": 0xB9,
            "diamondplt": 0xA5,
            "mirage_vest": 0xAE,
            "darksuit": 0xA6,
            "rainbow_dress": 0xCF,
            "bonemail": 0xBF
        },
        "magic": {
            "cotton_robe": 0xA7,
            "silk_robe": 0xA8,
            "bards_surplice": 0xAA, # Not a mistake --> the order is inverted.
            "gaia_gear": 0xA9, # Not a mistake --> the order is inverted.
            "angel_gwn": 0xBB,
            "lumina_robe": 0xAB,
            "white_robe": 0xAD, # Not a mistake --> the order is inverted.
            "black_robe": 0xAC # Not a mistake --> the order is inverted.
        },
        "heavy": {
            "bronze_armor": 0x9B,
            "iron_armor": 0x9C,
            "mythril_armor": 0x9D,
            "golden_armor": 0x9E,
            "diamond_armor": 0x9F,
            "crystal_armor": 0xA0,
            "genji_armor": 0xC8
        }
    }
}


accessories: Dict[str, int] = {
    "guard_ring": 0xAF,
    "thiefs_glove": 0xB0,
    "giants_gloves": 0xB1,
    "elf_cape": 0xB2,
    "cursed_ring": 0xB3,
    "glasses": 0xB4,
    "running_shoes": 0xB5,
    "mythril_glove": 0xB6,
    "silver_armlet": 0xB7,
    "diamond_armlet": 0xB8,
    "power_wrist": 0xBA,
    "angel_ring": 0xBC,
    "flame_ring": 0xBD,
    "coral_ring": 0xBE,
    "leather_shoes": 0xC0,
    "kaiser_knuckles": 0xC1,
    "gauntlets": 0xC2,
    "cornajar": 0xC5,
    "genji_gloves": 0xC9,
    "wall_ring": 0xCA,
    "red_shoes": 0xD0
}


items: Dict[str, int] = {
    "potion": 0xE0,
    "hi-potion": 0xE1,
    "ether": 0xE2,
    "elixir": 0xE3,
    "phoenix_down": 0xE4,
    "maidens_kiss": 0xE5,
    "revivify": 0xE6,
    "turtleshell": 0xE7,
    "antidote": 0xE8,
    "eyedrop": 0xE9,
    "dragonfang": 0xEA,
    "darkmatter": 0xEB,
    "soft": 0xEC,
    "lockmallet": 0xED,
    "magic_lamp": 0xEF, # Not a mistake --> 0xEE is unused.
    "tent": 0xF0,
    "cabin": 0xF1,
    "giant_drink": 0xF2,
    "power_drink": 0xF3,
    "speed_drink": 0xF4,
    "protect_drink": 0xF5,
    "hero_drink": 0xF6,
    "dragon_crest": 0xF7,
    "omega_medal": 0xF8,
    "ramuh": 0xF9,
    "shoat": 0xFA,
    "golem": 0xFB,
    "flame_scroll": 0xFC,
    "water_scroll": 0xFD,
    "thunder_scroll": 0xFE
} # Not a mistake --> 0xFF is unused.


spells: Dict[str, Dict[str, int]] = {
    "white": {
        "cure": 0x12,
        "scan": 0x13,
        "antdt": 0x14,
        "mute": 0x15,
        "armor": 0x16, # protect
        "size": 0x17, # mini
        "cure_2": 0x18,
        "life": 0x19, #raise
        "charm": 0x1A,
        "image": 0x1B,
        "shell": 0x1C,
        "heal": 0x1D, # esuna
        "cure_3": 0x1E,
        "wall": 0x1F,
        "berserk": 0x20, # wall
        "life_2": 0x21, # arise
        "holy": 0x22,
        "dispel": 0x23

    },
    "black": {
        "fire": 0x24,
        "ice": 0x25,
        "bolt": 0x26,
        "venom": 0x27,
        "sleep": 0x28,
        "toad": 0x29,
        "fire_2": 0x2A,
        "ice_2": 0x2B,
        "bolt_2": 0x2C,
        "drain": 0x2D,
        "break": 0x2E,
        "bio": 0x2F,
        "fire_3": 0x30,
        "ice_3": 0x31,
        "bolt_3": 0x32,
        "flare": 0x33,
        "doom": 0x34,
        "psych": 0x35
    },
    "dimen": {
        "drag": 0x36,
        "slow": 0x37,
        "regen": 0x38,
        "void": 0x39,
        "haste": 0x3A,
        "float": 0x3B,
        "demi": 0x3C,
        "stop": 0x3D,
        "exit": 0x3E,
        "comet": 0x3F,
        "slow_2": 0x40,
        "return": 0x41,
        "qrter": 0x42, # demi 2
        "haste 2": 0x43,
        "old": 0x44,
        "meteo": 0x45,
        "quick": 0x46,
        "xzone": 0x47
    },
    ''' As we want to back-up all the missable shops, we do not have room for magic swords. After all, they already come with the corresponding spell.
    "magic_sword": {
        #"fire_sword": 0x00, We cannot place the fire sword in a shop, because 0x00 will be interpreted as "nothing more"
        "ice_sword": 0x01,
        "bolt_sword": 0x02,
        "venom_sword": 0x03,
        "mute_sword": 0x04,
        "sleep_sword": 0x05,
        "fire_2_sword": 0x06,
        "ice_2_sword": 0x07,
        "bolt_2_sword": 0x08,
        "drain_sword": 0x09,
        "break_sword": 0x0A,
        "bio_sword": 0x0B,
        "fire_3_sword": 0x0C,
        "ice_3_sword": 0x0D,
        "bolt_3_sword": 0x0E,
        "holy_sword": 0x0F,
        "flare_sword": 0x10,
        "psych_sword": 0x11
    },
    '''
    "summons": {
        "chocobo": 0x48,
        "sylph": 0x49,
        "remora": 0x4A,
        "shiva": 0x4B,
        "ifrit": 0x4D, # Not a mistake --> the order is inverted.
        "ramuh": 0x4C, # Not a mistake --> the order is inverted.
        "titan": 0x4E,
        "golem": 0x4F,
        "shoat": 0x50,
        "carbuncle": 0x51,
        "syldra": 0x52,
        "odin": 0x53,
        "phoenix": 0x54,
        "leviathan": 0x55,
        "bahamut": 0x56
    },
    "blue": {
        "condemn": 0x82,
        "roulette": 0x83,
        "aquarake": 0x84,
        "l5_doom": 0x85,
        "l4_qrter": 0x86,
        "l2_old": 0x87,
        "l3_flare": 0x88,
        "frogsong": 0x89,
        "tinysong": 0x8A,
        "flash": 0x8B,
        "timeslip": 0x8C, # time sleep
        "moonflut": 0x8D, # moon flute
        "dethclaw": 0x8E, # death claw
        "aero": 0x8F,
        "aero_2": 0x90,
        "aero_3": 0x91,
        "emission": 0x92,
        "gblinpnch": 0x93, # goblin punch
        "drkschock": 0x94, # dark shock
        "guardoff": 0x95,
        "fusion": 0x96,
        "mindblst": 0x97, # mind blast
        "vampire": 0x98,
        "hammer": 0x99,
        "mgthygrd": 0x9A, # mighty guard
        "exploder": 0x9B,
        "????": 0x9C,
        "blowfish": 0x9D,
        "whitewind": 0x9E,
        "missile": 0x9F
    },
    "songs": {
        "power_song": 0x57,
        "speed_song": 0x58,
        "vitality_song": 0x59,
        "magic_song": 0x5A,
        "hero_song": 0x5B,
        "requiem": 0x5C,
        "love_song": 0x5D,
        "charm_song": 0x5E
    }
}


jobs: Dict[str, int] = {
    "knight": 0x89,
    "monk": 0x8A,
    "thief": 0x8B,
    "dragoon": 0x8C,
    "ninja": 0x8D,
    "samurai": 0x8E,
    "berserker": 0x8F,
    "hunter": 0x90,
    "mystic_knight": 0x91,
    "white_mage": 0x92,
    "black_mage": 0x93,
    "time_mage": 0x94,
    "summoner": 0x95,
    "blue_mage": 0x96,
    "red_mage": 0x97,
    "mediator": 0x98,
    "chemist": 0x99,
    "geomancer": 0x9A,
    "bard": 0x9B,
    "dancer": 0x9C,
    "mimic": 0x9D,
    "freelancer": 0x9E
}


shop_goods_mappings: Dict[str, str] = {
    "magic": magic_codes,
    "weapon": weapon_codes,
    "armor": armor_codes,
    "item": item_codes,
    "accessory": accessory_codes,
    "job": job_codes
}


# The purchasable goods are located in the memory range [<address + 1> to <address + 9>] (extremes included)
shop_type_flag_memory_locations: Dict[str, Dict[str, Union[int, Dict[str, int]]]] = {
    "tule": {
        "weapon": 0x112D40,
        "armor": 0x112D49,
        "item": 0x112D52,
        "magic": 0x112D5B
    },
    "carwen": {
        "weapon": 0x112D64,
        "armor": 0x112D6D,
        "item": 0x112D76,
        "magic": 0x112D7F
    },
    "walse": {
        "weapon": 0x112D88,
        "armor": 0x112D91,
        # item -> carwen item shop.
        "magic": 0x112D9A
    },
    "karnak": {
        "weapon_1": 0x112DA3, # Available after being arrested.
        "weapon_2": 0x112DAC, # Available after the Karnak castle blows up.
        "armor": 0x112DB5, # Available after being arrested.
        "item": 0x112DBE, # Available after being arrested.
        "black_magic": 0x112DC7, # Available after being arrested.
        "white_magic": 0x112DD0, # Available after being arrested.
        "dimen_magic": 0x112DD9, # Available after being arrested.
        "weapon_before_arrest": 0x112F6E,
        "armor_before_arrest": 0x112F77
    },
    "crescent": {
        "weapon": 0x112DE2,
        "armor": 0x112DEB,
        # item -> karnak item shop.
        # magic -> karnak black_magic shop.
    },
    "istory": {
        "accessory": 0x112DFD
        # item -> karnak item shop.
        # magic -> karnak dimen_magic shop.
    },
    "jacole": {
        "weapon": 0x112E18,
        "armor": 0x112E21,
        # item -> karnak item shop
        # magic -> karnak white_magic shop.
    },
    "lix": {
        "throwable": 0x112E33,
        "armor": 0x112E3C,
        "item": 0x112EF9,
        "magic": 0x112E45
    },
    "regole": {
        "weapon": 0x112E4E,
        "armor": 0x112E57,
        "item_1": 0x112E60,
        "item_2": 0x112E2A
        # magic_1 -> kelb magic_1 shop.
        # magic_2 -> kelb magic_2 shop.
        # magic_3 -> kelb magic_3 shop.
    },
    "bal": {
        "weapon": 0x112E69,
        "armor": 0x112E72,
        # item_1 -> regole item_1 shop.
        # item_2 -> regole item_2 shop.
        # magic_1 -> kelb magic_1 shop.
        # magic_2 -> kelb magic_2 shop.
        # magic_3 -> kelb magic_3 shop.
    },
    "kelb": {
        "weapon_1": 0x112E7B,
        # weapon_2 --> bal weapon shop.
        "armor_1": 0x112E84,
        # armor_2 --> bal armor shop.
        # item_1 -> regole item_1 shop.
        # item_2 -> regole item_2 shop.
        "white_magic": 0x112E8D,
        "black_magic": 0x112E96,
        "dimen_magic": 0x112E9F
    },
    "surgate": {
        "weapon": 0x112EA8,
        "armor": 0x112EB1
        # item_1 -> regole item_1 shop.
        # item_2 -> regole item_2 shop.
        # magic_1 -> kelb magic_1 shop.
        # magic_2 -> kelb magic_2 shop.
        # magic_3 -> kelb magic_3 shop.
    },
    "moore": {
        "weapon": 0x112EBA,
        "armor": 0x112EC3,
        # item_1 -> regole item_1 shop.
        # item_2 -> regole item_2 shop.
        "white_magic": 0x112ECC,
        "black_magic": 0x112ED5,
        "dimen_magic": 0x112EDE
    },
    "trench": {
        "weapon": 0x112F0B,
        "armor": 0x112F14
    },
    "mirage": {
        "weapon": 0x112F26,
        "throwable": 0x112F2F,
        "armor": 0x112F38,
        "accessory": 0x112F41,
        "level_6_magic": 0x112F4A, # Level 6 spells.
        "missable_magic": 0x112F53, # Level 1/2/3 spells and Level 1 summons.
        "item_top": 0x112F5C,
        "item_with_elixir": 0x112F65
    },
    "dummy": {
        "weapon": {
            "dummy_1": 0x112EE7
        },
        "armor": {
            "dummy_1": 0x112E06,
            "dummy_2": 0x112EF0
        },
        "item": {
            "dummy_1": 0x112F1D
        },
        "magic": {
            "dummy_1": 0x112DF4,
            "dummy_2": 0x112E0F,
            "dummy_3": 0x112F02
        }
    }
}


# Note: not all the shops that sell the same goods are shared - e.g., Bal's weapon shop vs Regole's weapon shop.
shared_shops: Dict[str, List[str]] = {
    "walse": [
        "originally: item - now: see carwen's original item shop"
    ],
    "crescent": [
        "originally: item - now: see karnak's original item shop",
        "originally: black_magic: - now: see karnak's original black_magic shop"
    ],
    "istory": [
        "originally: item - now: see karnak's original item shop",
        "originally: dimen_magic: - now: see karnak's original dimen_magic shop"
    ],
    "jacole": [
        "originally: item - now: see karnak's original item shop",
        "originally: white_magic: - now: see karnak's original white_magic shop"
    ],
    "regole": [
        "originally: white_magic - now: see kelb's original white_magic shop",
        "originally: black_magic - now: see kelb's original black_magic shop",
        "originally: dimen_magic - now: see kelb's original dimen_magic shop"
    ],
    "bal": [
        "originally: item_1 - now: see regole's original item_1 shop",
        "originally: item_2 - now: see regole's original item_2 shop",
        "originally: white_magic - now: see kelb's original white_magic shop",
        "originally: black_magic - now: see kelb's original black_magic shop",
        "originally: dimen_magic - now: see kelb's original dimen_magic shop"
    ],
    "kelb": [
        "originally: item_1 - now: see regole's original item_1 shop",
        "originally: item_2 - now: see regole's original item_2 shop",
        "originally: weapon_2 - now: see bal's original weapon_1 shop", # Not a mistake: weapon_2/weapon_1.
        "originally: armor_2 - now: see bal's original armor_1 shop" # Not a mistake: armor_2/armor_1.
    ],
    "surgate": [
        "originally: item_1 - now: see regole's original item_1 shop",
        "originally: item_2 - now: see regole's original item_2 shop",
        "originally: white_magic - now: see kelb's original white_magic shop",
        "originally: black_magic - now: see kelb's original black_magic shop",
        "originally: dimen_magic - now: see kelb's original dimen_magic shop"
    ],
    "moore": [
        "originally: item_1 - now: see regole's original item_1 shop",
        "originally: item_2 - now: see regole's original item_2 shop",
    ]
}


missable_shops_type_addresses: List[int] = list(shop_type_flag_memory_locations["walse"].values()) + list(shop_type_flag_memory_locations["istory"].values()) + list(shop_type_flag_memory_locations["lix"].values())
