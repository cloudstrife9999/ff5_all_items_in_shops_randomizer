from typing import List



def fixed_mod(ff5_bytes: List[int]) -> List[int]:
    # Tule Weapon Shop
    ff5_bytes[0x112D40] = 0x01 # Weapon Shop
    ff5_bytes[0x112D41] = 0x54 # Sabre
    ff5_bytes[0x112D42] = 0x02 # Knife
    ff5_bytes[0x112D43] = 0x03 # Dagger
    ff5_bytes[0x112D44] = 0x0D # Broadsword
    ff5_bytes[0x112D45] = 0x31 # Rod
    ff5_bytes[0x112D46] = 0x38 # Staff
    ff5_bytes[0x112D47] = 0x3A # Power Staff
    ff5_bytes[0x112D48] = 0x3B # Healing Staff

    # Tule Armor Shop
    ff5_bytes[0x112D49] = 0x02 # Armor Shop
    ff5_bytes[0x112D4A] = 0xCE # Cursed Shield
    ff5_bytes[0x112D4B] = 0x81 # Leather Shield
    ff5_bytes[0x112D4C] = 0x89 # Leather Cap
    ff5_bytes[0x112D4D] = 0x9A # Leather Armor
    ff5_bytes[0x112D4E] = 0x90 # Plumed Hat
    ff5_bytes[0x112D4F] = 0xA7 # Cotton Robe
    ff5_bytes[0x112D50] = 0x8A # Bronze Helmet
    ff5_bytes[0x112D51] = 0x9B # Bronze Armor

    # Tule Item Shop
    ff5_bytes[0x112D52] = 0x03 # Item Shop
    ff5_bytes[0x112D53] = 0xE0 # Potion
    ff5_bytes[0x112D54] = 0xE4 # Phoenix Down
    ff5_bytes[0x112D55] = 0xE8 # Antidote
    ff5_bytes[0x112D56] = 0xE9 # Eye Drop
    ff5_bytes[0x112D57] = 0xE5 # Maiden's Kiss
    ff5_bytes[0x112D58] = 0xeD # Cornucopia
    ff5_bytes[0x112D59] = 0xEC # Soft
    ff5_bytes[0x112D5A] = 0xF0 # Tent

    # Tule Magic Shop
    ff5_bytes[0x112D5B] = 0x00 # Magic Shop
    ff5_bytes[0x112D5C] = 0x12 # Cure
    ff5_bytes[0x112D5D] = 0x13 # Scan
    ff5_bytes[0x112D5E] = 0x14 # Antidot
    ff5_bytes[0x112D5F] = 0x15 # Mute
    ff5_bytes[0x112D60] = 0x24 # Fire
    ff5_bytes[0x112D61] = 0x25 # Ice
    ff5_bytes[0x112D62] = 0x26 # Bolt
    ff5_bytes[0x112D63] = 0x27 # Venom

    # Carwen Weapon Shop
    ff5_bytes[0x112D64] = 0x01 # Weapon Shop
    ff5_bytes[0x112D65] = 0x0E # RegalCut
    ff5_bytes[0x112D66] = 0x5E # Flail
    ff5_bytes[0x112D67] = 0x67 # Antimagic Bow
    ff5_bytes[0x112D68] = 0x62 # Soot
    ff5_bytes[0x112D69] = 0x04 # Mithril Dagger
    ff5_bytes[0x112D6A] = 0x39 # Mythril Staff
    ff5_bytes[0x112D6B] = 0x18 # Spear
    ff5_bytes[0x112D6C] = 0x50 # Giyaman

    # Carwen Armor Shop
    ff5_bytes[0x112D6D] = 0x02 # Armor Shop
    ff5_bytes[0x112D6E] = 0x82 # Bronze Shield
    ff5_bytes[0x112D6F] = 0x83 # Iron Shield
    ff5_bytes[0x112D70] = 0x97 # Green Beret
    ff5_bytes[0x112D71] = 0xA1 # Copper Plate
    ff5_bytes[0x112D72] = 0x99 # Lamia's Tiara
    ff5_bytes[0x112D73] = 0xA8 # Silk Robe
    ff5_bytes[0x112D74] = 0x8B # Iron Helmet
    ff5_bytes[0x112D75] = 0x9C # Iron Armor

    # Carwen/Walse Item Shop
    ff5_bytes[0x112D76] = 0x03 # Item Shop
    ff5_bytes[0x112D77] = 0xE1 # Hi-Potion
    ff5_bytes[0x112D78] = 0xE2 # Ether
    ff5_bytes[0x112D79] = 0xE6 # Revivify
    ff5_bytes[0x112D7A] = 0xE7 # Turtle Shell
    ff5_bytes[0x112D7B] = 0xEA # Dragon Fang
    ff5_bytes[0x112D7C] = 0xEB # Dark Matter
    ff5_bytes[0x112D7D] = 0xE3 # Elixir
    ff5_bytes[0x112D7E] = 0xF1 # Cabin

    # Carwen Magic Shop
    ff5_bytes[0x112D7F] = 0x00 # Magic Shop
    ff5_bytes[0x112D80] = 0x16 # Armor
    ff5_bytes[0x112D81] = 0x17 # Size
    ff5_bytes[0x112D82] = 0x28 # Sleep
    ff5_bytes[0x112D83] = 0x29 # Toad
    ff5_bytes[0x112D84] = 0x48 # Chocobo
    ff5_bytes[0x112D85] = 0x49 # Sylph
    ff5_bytes[0x112D86] = 0x4A # Remora
    ff5_bytes[0x112D87] = 0x57 # Power Song

    # Walse Weapon Shop --> MISSABLE --> backed up in Mirage Village Weapon Shop
    ff5_bytes[0x112D88] = 0x01 # Weapon Shop
    ff5_bytes[0x112D89] = 0x0F # Mythril Sword
    ff5_bytes[0x112D8A] = 0x19 # Mythril Spear
    ff5_bytes[0x112D8B] = 0x21 # Battle Axe
    ff5_bytes[0x112D8C] = 0x32 # Fire Rod
    ff5_bytes[0x112D8D] = 0x33 # Ice Rod
    ff5_bytes[0x112D8E] = 0x34 # Thunder Rod
    ff5_bytes[0x112D8F] = 0x06 # Mage Masher
    ff5_bytes[0x112D90] = 0x05 # Kunai

    # Walse Armor Shop --> MISSABLE --> backed up in Mirage Village Armor Shop
    ff5_bytes[0x112D91] = 0x02 # Armor Shop
    ff5_bytes[0x112D92] = 0x84 # Mythril Shield
    ff5_bytes[0x112D93] = 0x85 # Golden Shield
    ff5_bytes[0x112D94] = 0x96 # Bandana
    ff5_bytes[0x112D95] = 0xA2 # Training Suit
    ff5_bytes[0x112D96] = 0x91 # Tricorn
    ff5_bytes[0x112D97] = 0xAA # Bard's Supplice
    ff5_bytes[0x112D98] = 0x8C # Mythril Helmet
    ff5_bytes[0x112D99] = 0x9D # Mythril Armor

    # Walse Magic Shop --> MISSABLE --> backed up in Mirage Village Missable Magic Shop
    ff5_bytes[0x112D9A] = 0x00 # Magic Shop
    ff5_bytes[0x112D9B] = 0x36 # Drag
    ff5_bytes[0x112D9C] = 0x37 # Slow
    ff5_bytes[0x112D9D] = 0x38 # Regen
    ff5_bytes[0x112D9E] = 0x39 # Void
    ff5_bytes[0x112D9F] = 0x3A # Haste
    ff5_bytes[0x112DA0] = 0x3B # Float
    ff5_bytes[0x112DA1] = 0x58 # Speed Song
    ff5_bytes[0x112DA2] = 0x59 # Vitality Song

    # Karnak Weapon_1 Shop
    ff5_bytes[0x112DA3] = 0x01 # Weapon Shop
    ff5_bytes[0x112DA4] = 0x10 # Coral Sword
    ff5_bytes[0x112DA5] = 0x22 # Mythril Hammer
    ff5_bytes[0x112DA6] = 0x07 # Guardian
    ff5_bytes[0x112DA7] = 0x65 # Silver Bow
    ff5_bytes[0x112DA8] = 0x3F # Fire Bow
    ff5_bytes[0x112DA9] = 0x40 # Ice Bow
    ff5_bytes[0x112DAA] = 0x41 # Thunder Bow
    ff5_bytes[0x112DAB] = 0x4B # Whip

    # Karnak Weapon_2 Shop
    ff5_bytes[0x112DAC] = 0x01 # Weapon Shop
    ff5_bytes[0x112DAD] = 0x59 # Full Moon
    ff5_bytes[0x112DAE] = 0x47 # Silver Harp
    ff5_bytes[0x112DAF] = 0x09 # Orialcon
    ff5_bytes[0x112DB0] = 0x11 # Ancient Sword
    ff5_bytes[0x112DB1] = 0x1A # Trident
    ff5_bytes[0x112DB2] = 0x29 # Katana
    ff5_bytes[0x112DB3] = 0x23 # Ogre Killer
    ff5_bytes[0x112DB4] = 0x36 # Lilith Rod

    # Karnak Armor Shop
    ff5_bytes[0x112DB5] = 0x02 # Armor Shop
    ff5_bytes[0x112DB6] = 0x86 # Aegis Shield
    ff5_bytes[0x112DB7] = 0x87 # Diamond Shield
    ff5_bytes[0x112DB8] = 0xA3 # Silver Plate
    ff5_bytes[0x112DB9] = 0xA4 # Stealth Suit
    ff5_bytes[0x112DBA] = 0xCB # Coronet
    ff5_bytes[0x112DBB] = 0xA9 # Gaia Gear
    ff5_bytes[0x112DBC] = 0x8D # Golden Helm
    ff5_bytes[0x112DBD] = 0x9E # Golden Armor

    # Karnak/Crescent/Istory/Jacole Item Shop
    ff5_bytes[0x112DBE] = 0x03 # Item Shop
    ff5_bytes[0x112DBF] = 0xF7 # Dragon Crest
    ff5_bytes[0x112DC0] = 0xF8 # Omega Medal
    ff5_bytes[0x112DC1] = 0xF9 # Ramuh
    ff5_bytes[0x112DC2] = 0xFA # Shoat
    ff5_bytes[0x112DC3] = 0xFB # Golem
    ff5_bytes[0x112DC4] = 0xFC # Flame Scroll
    ff5_bytes[0x112DC5] = 0xFD # Water Scroll
    ff5_bytes[0x112DC6] = 0xFE # Thunder Scroll

    # Karnak/Crescent Black Magic Shop
    ff5_bytes[0x112DC7] = 0x00 # Magic Shop
    ff5_bytes[0x112DC8] = 0x2A # Fire 2
    ff5_bytes[0x112DC9] = 0x2B # Ice 2
    ff5_bytes[0x112DCA] = 0x2C # Bolt 2
    ff5_bytes[0x112DCB] = 0x2D # Drain
    ff5_bytes[0x112DCC] = 0x2E # Break
    ff5_bytes[0x112DCD] = 0x2F # Bio
    ff5_bytes[0x112DCE] = 0x5A # Magic Song
    ff5_bytes[0x112DCF] = 0x5B # Hero Song

    # Karnak/Jacole White Magic Shop
    ff5_bytes[0x112DD0] = 0x00 # Magic Shop
    ff5_bytes[0x112DD1] = 0x18 # Cure 2
    ff5_bytes[0x112DD2] = 0x19 # Life
    ff5_bytes[0x112DD3] = 0x1A # Charm
    ff5_bytes[0x112DD4] = 0x1B # Image
    ff5_bytes[0x112DD5] = 0x1C # Shell
    ff5_bytes[0x112DD6] = 0x1D # Heal
    ff5_bytes[0x112DD7] = 0x5C # Requiem
    ff5_bytes[0x112DD8] = 0x5D # Love Song

    # Karnak/Istory Dimen Magic Shop
    ff5_bytes[0x112DD9] = 0x00 # Magic Shop
    ff5_bytes[0x112DDA] = 0x3C # Demi
    ff5_bytes[0x112DDB] = 0x3D # Stop
    ff5_bytes[0x112DDC] = 0x3E # Exit
    ff5_bytes[0x112DDD] = 0x3F # Comet
    ff5_bytes[0x112DDE] = 0x40 # Slow 2
    ff5_bytes[0x112DDF] = 0x41 # Reset
    ff5_bytes[0x112DE0] = 0x4B # Shiva
    ff5_bytes[0x112DE1] = 0x5E # Charm Song

    # Karnak Cheap Weapon Shop before arrest
    ff5_bytes[0x112F6E] = 0x81 # Cheap Weapon Shop
    ff5_bytes[0x112F6F] = 0x00 # Nothing
    ff5_bytes[0x112F70] = 0x00 # Nothing
    ff5_bytes[0x112F71] = 0x00 # Nothing
    ff5_bytes[0x112F72] = 0x00 # Nothing
    ff5_bytes[0x112F73] = 0x00 # Nothing
    ff5_bytes[0x112F74] = 0x00 # Nothing
    ff5_bytes[0x112F75] = 0x00 # Nothing
    ff5_bytes[0x112F76] = 0x00 # Nothing

    # Karnak Cheap Armor Shop before arrest
    ff5_bytes[0x112F77] = 0x82 # Cheap Armor Shop
    ff5_bytes[0x112F78] = 0x00 # Nothing
    ff5_bytes[0x112F79] = 0x00 # Nothing
    ff5_bytes[0x112F7A] = 0x00 # Nothing
    ff5_bytes[0x112F7B] = 0x00 # Nothing
    ff5_bytes[0x112F7C] = 0x00 # Nothing
    ff5_bytes[0x112F7D] = 0x00 # Nothing
    ff5_bytes[0x112F7E] = 0x00 # Nothing
    ff5_bytes[0x112F7F] = 0x00 # Nothing

    # Crescent Weapon Shop
    ff5_bytes[0x112DE2] = 0x01 # Weapon Shop
    ff5_bytes[0x112DE3] = 0x0A # Air Lance
    ff5_bytes[0x112DE4] = 0x56 # Rune Edge
    ff5_bytes[0x112DE5] = 0x1D # Gungnir
    ff5_bytes[0x112DE6] = 0x69 # Doom Cut
    ff5_bytes[0x112DE7] = 0x3C # Staff of Light
    ff5_bytes[0x112DE8] = 0x43 # Killer Bow
    ff5_bytes[0x112DE9] = 0x48 # Dream Harp
    ff5_bytes[0x112DEA] = 0x35 # Venom Rod

    # Crescent Armor Shop
    ff5_bytes[0x112DEB] = 0x02 # Armor Shop
    ff5_bytes[0x112DEC] = 0x88 # Crystal Shield
    ff5_bytes[0x112DED] = 0xC6 # Genji Shield
    ff5_bytes[0x112DEE] = 0xC3 # Tiger Mask
    ff5_bytes[0x112DEF] = 0xAE # Mirage Vest
    ff5_bytes[0x112DF0] = 0x94 # Goldpin
    ff5_bytes[0x112DF1] = 0xAB # Lumina Robe
    ff5_bytes[0x112DF2] = 0x8F # Crystal Helm
    ff5_bytes[0x112DF3] = 0xA0 # Crystal Armor

    # Istory Accessory Shop --> MISSABLE --> backed up in Mirage Village Accessory Shop
    ff5_bytes[0x112DFD] = 0x04 # Accessory Shop
    ff5_bytes[0x112DFE] = 0xC0 # Leather Shoes
    ff5_bytes[0x112DFF] = 0xB4 # Glasses
    ff5_bytes[0x112E00] = 0xB2 # Elf Cape
    ff5_bytes[0x112E01] = 0xB6 # Mythril Glove
    ff5_bytes[0x112E02] = 0xB7 # Silver Armlet
    ff5_bytes[0x112E03] = 0xBD # Flame Ring
    ff5_bytes[0x112E04] = 0xBE # Coral Ring
    ff5_bytes[0x112E05] = 0xBC # Angel Ring

    # Jacole Weapon Shop
    ff5_bytes[0x112E18] = 0x01 # Weapon Shop
    ff5_bytes[0x112E19] = 0x6D # Dancing Dagger
    ff5_bytes[0x112E1A] = 0x13 # Slumber
    ff5_bytes[0x112E1B] = 0x1B # Wind Spear
    ff5_bytes[0x112E1C] = 0x24 # War Hammer
    ff5_bytes[0x112E1D] = 0x2A # Air Blade
    ff5_bytes[0x112E1E] = 0x42 # Darkness Bow
    ff5_bytes[0x112E1F] = 0x4D # Thunder Whip
    ff5_bytes[0x112E20] = 0x51 # Earth Bell

    # Jacole Armor Shop
    ff5_bytes[0x112E21] = 0x02 # Armor Shop
    ff5_bytes[0x112E22] = 0xC4 # Flame Shield
    ff5_bytes[0x112E23] = 0xCD # Ice Shield
    ff5_bytes[0x112E24] = 0xB9 # Strength
    ff5_bytes[0x112E25] = 0xA5 # Diamond Plate
    ff5_bytes[0x112E26] = 0x92 # Magus
    ff5_bytes[0x112E27] = 0xBB # AngelGwn
    ff5_bytes[0x112E28] = 0x8E # Diamond Helm
    ff5_bytes[0x112E29] = 0x9F # Diamond Armor

    # Lix Throwable Shop --> MISSABLE --> backed up in Mirage Village Throwable Shop
    ff5_bytes[0x112E33] = 0x05 # Weapon/Throwable Shop
    ff5_bytes[0x112E34] = 0x5A # Shuriken
    ff5_bytes[0x112E35] = 0x6C # Thief Knife
    ff5_bytes[0x112E36] = 0x12 # Epee
    ff5_bytes[0x112E37] = 0x08 # Kodachi
    ff5_bytes[0x112E38] = 0x17 # Javelin
    ff5_bytes[0x112E39] = 0x25 # Venom Axe
    ff5_bytes[0x112E3A] = 0x2C # Bizen
    ff5_bytes[0x112E3B] = 0x44 # Elven Bow

    # Lix Armor Shop --> MISSABLE --> backed up in Mirage Village Elixir Shop
    ff5_bytes[0x112E3C] = 0x02 # Armor Shop
    ff5_bytes[0x112E3D] = 0x98 # Dark Hood
    ff5_bytes[0x112E3E] = 0xA6 # Dark Suit
    ff5_bytes[0x112E3F] = 0xCF # Raibnbow Dress
    ff5_bytes[0x112E40] = 0x93 # Circlet
    ff5_bytes[0x112E41] = 0xAD # White Robe
    ff5_bytes[0x112E42] = 0xAC # Black Robe
    ff5_bytes[0x112E43] = 0xC7 # Genji Helmet
    ff5_bytes[0x112E44] = 0xC8 # Genji Armor

    # Lix Cheap Item Shop --> MISSABLE --> backed up in Mirage Village Item Shop
    ff5_bytes[0x112EF9] = 0x03 # Item Shop
    ff5_bytes[0x112EFA] = 0xEF # Magic Lamp
    ff5_bytes[0x112EFB] = 0xF2 # Giant Drink
    ff5_bytes[0x112EFC] = 0xF3 # Power Drink
    ff5_bytes[0x112EFD] = 0xF4 # Speed Drink
    ff5_bytes[0x112EFE] = 0xF5 # Protect Drink
    ff5_bytes[0x112EFF] = 0xF6 # Hero Drink
    ff5_bytes[0x112F00] = 0x00 # Nothing
    ff5_bytes[0x112F01] = 0x00 # Nothing

    # Lix Magic Shop --> MISSABLE --> backed up in Mirage Village Level 6 Magic Shop
    ff5_bytes[0x112E45] = 0x00 # Magic Shop
    ff5_bytes[0x112E46] = 0x4D # Ifrit
    ff5_bytes[0x112E47] = 0x4C # Ramuh
    ff5_bytes[0x112E48] = 0x4E # Titan
    ff5_bytes[0x112E49] = 0x4F # Golem
    ff5_bytes[0x112E4A] = 0x50 # Shoat
    ff5_bytes[0x112E4B] = 0x51 # Carbuncle
    ff5_bytes[0x112E4C] = 0x52 # Syldra
    ff5_bytes[0x112E4D] = 0x53 # Odin

    # Regole Weapon Shop
    ff5_bytes[0x112E4E] = 0x01 # Weapon Shop
    ff5_bytes[0x112E4F] = 0x5C # Excailbur
    ff5_bytes[0x112E50] = 0x55 # Drain Sword
    ff5_bytes[0x112E51] = 0x1C # Partisan
    ff5_bytes[0x112E52] = 0x2B # Kotetsu
    ff5_bytes[0x112E53] = 0x64 # Rising Sun
    ff5_bytes[0x112E54] = 0x66 # Gale Bow
    ff5_bytes[0x112E55] = 0x4C # Chain Whip
    ff5_bytes[0x112E56] = 0x49 # Lamia's Harp

    # Regole Armor Shop
    ff5_bytes[0x112E57] = 0x02 # Armor Shop
    ff5_bytes[0x112E58] = 0xCC # Thornlet
    ff5_bytes[0x112E59] = 0x95 # Ribbon
    ff5_bytes[0x112E5A] = 0xBF # Bonemail
    ff5_bytes[0x112E5B] = 0x00 # Nothing
    ff5_bytes[0x112E5C] = 0x00 # Nothing
    ff5_bytes[0x112E5D] = 0x00 # Nothing
    ff5_bytes[0x112E5E] = 0x00 # Nothing
    ff5_bytes[0x112E5F] = 0x00 # Nothing

    # Regole/Bal/Kelb/Surgate/Moore Item_1 Shop
    ff5_bytes[0x112E60] = 0x07 # Job Shop
    ff5_bytes[0x112E61] = 0x89 # Knight
    ff5_bytes[0x112E62] = 0x8A # Monk
    ff5_bytes[0x112E63] = 0x8B # Thief
    ff5_bytes[0x112E64] = 0x92 # White Mage
    ff5_bytes[0x112E65] = 0x93 # Black Mage
    ff5_bytes[0x112E66] = 0x96 # Blue Mage
    ff5_bytes[0x112E67] = 0x9E # Freelancer
    ff5_bytes[0x112E68] = 0x9D # Mime

    # Regole/Bal/Kelb/Surgate/Moore Item_2 Shop
    ff5_bytes[0x112E2A] = 0x07 # Job Shop
    ff5_bytes[0x112E2B] = 0x91 # Mystic Knight
    ff5_bytes[0x112E2C] = 0x8F # Berserker
    ff5_bytes[0x112E2D] = 0x95 # Summoner
    ff5_bytes[0x112E2E] = 0x94 # Time Mage
    ff5_bytes[0x112E2F] = 0x97 # Red Mage
    ff5_bytes[0x112E30] = 0x9A # Geomancer
    ff5_bytes[0x112E31] = 0x98 # Beastmaster
    ff5_bytes[0x112E32] = 0x8D # Ninja

    # Bal/Kelb Weapon Shop
    ff5_bytes[0x112E69] = 0x01 # Weapon Shop
    ff5_bytes[0x112E6A] = 0x0B # Assassin
    ff5_bytes[0x112E6B] = 0x5F # Morning Star
    ff5_bytes[0x112E6C] = 0x57 # Flame Tongue
    ff5_bytes[0x112E6D] = 0x58 # Ice Brand
    ff5_bytes[0x112E6E] = 0x26 # Earth Hammer
    ff5_bytes[0x112E6F] = 0x2D # Forged
    ff5_bytes[0x112E70] = 0x68 # Avis Killer
    ff5_bytes[0x112E71] = 0x5D # BeastKiller

    # Bal/Kelb Armor Shop
    ff5_bytes[0x112E72] = 0x07 # Job Shop
    ff5_bytes[0x112E73] = 0x9B # Bard
    ff5_bytes[0x112E74] = 0x90 # Hunter
    ff5_bytes[0x112E75] = 0x8C # Dragoon
    ff5_bytes[0x112E76] = 0x8E # Samurai
    ff5_bytes[0x112E77] = 0x99 # Chemist
    ff5_bytes[0x112E78] = 0x9C # Dancer
    ff5_bytes[0x112E79] = 0x00 # Nothing
    ff5_bytes[0x112E7A] = 0x00 # Nothing

    # Kelb Weapon_1 Shop
    ff5_bytes[0x112E7B] = 0x01 # Weapon Shop
    ff5_bytes[0x112E7C] = 0x6B # Man Eater
    ff5_bytes[0x112E7D] = 0x0C # Hardened
    ff5_bytes[0x112E7E] = 0x6E # Enhancer
    ff5_bytes[0x112E7F] = 0x14 # Defender
    ff5_bytes[0x112E80] = 0x1F # Holy Lance
    ff5_bytes[0x112E81] = 0x2E # Murasame
    ff5_bytes[0x112E82] = 0x27 # Rune Axe
    ff5_bytes[0x112E83] = 0x52 # Rune Chime

    # Kelb Armor_1 Shop
    ff5_bytes[0x112E84] = 0x04 # Accessory Shop
    ff5_bytes[0x112E85] = 0xB0 # Thief's Glove
    ff5_bytes[0x112E86] = 0xC2 # Gauntlets
    ff5_bytes[0x112E87] = 0xBA # Power Wrist
    ff5_bytes[0x112E88] = 0xC5 # CornaJar
    ff5_bytes[0x112E89] = 0xC9 # Genji Gloves
    ff5_bytes[0x112E8A] = 0xCA # Wall Ring
    ff5_bytes[0x112E8B] = 0xB8 # Diamond Armlet
    ff5_bytes[0x112E8C] = 0xB3 # Cursed Ring

    # Regole/Bal/Kelb/Surgate White Magic Shop
    ff5_bytes[0x112E8D] = 0x00 # Magic Shop
    ff5_bytes[0x112E8E] = 0x93 # Goblin Punch
    ff5_bytes[0x112E8F] = 0x8F # Aero
    ff5_bytes[0x112E90] = 0x98 # Vampire
    ff5_bytes[0x112E91] = 0x8B # Flash
    ff5_bytes[0x112E92] = 0x8D # Moon Flute
    ff5_bytes[0x112E93] = 0x89 # Frog Song
    ff5_bytes[0x112E94] = 0x9C # ????
    ff5_bytes[0x112E95] = 0x9B # Exploder

    # Regole/Bal/Kelb/Surgate Black Magic Shop
    ff5_bytes[0x112E96] = 0x00 # Magic Shop
    ff5_bytes[0x112E97] = 0x90 # Aero 2
    ff5_bytes[0x112E98] = 0x8E # Doom Claw
    ff5_bytes[0x112E99] = 0x9F # Missile
    ff5_bytes[0x112E9A] = 0x99 # Magic Hammer
    ff5_bytes[0x112E9B] = 0x96 # Fusion
    ff5_bytes[0x112E9C] = 0x84 # Aqua Rake
    ff5_bytes[0x112E9D] = 0x85 # L5 Doom
    ff5_bytes[0x112E9E] = 0x95 # Guard Off

    # Regole/Bal/Kelb/Surgate Dimen Magic Shop
    ff5_bytes[0x112E9F] = 0x00 # Magic Shop
    ff5_bytes[0x112EA0] = 0x94 # Black Shock
    ff5_bytes[0x112EA1] = 0x92 # Emission
    ff5_bytes[0x112EA2] = 0x9E # White Wind
    ff5_bytes[0x112EA3] = 0x9D # Blowfish
    ff5_bytes[0x112EA4] = 0x86 # L4 Quarter
    ff5_bytes[0x112EA5] = 0x8C # Time Sleep
    ff5_bytes[0x112EA6] = 0x87 # L2 Old
    ff5_bytes[0x112EA7] = 0x88 # L3 Flare

    # Surgate Weapon Shop
    ff5_bytes[0x112EA8] = 0x01 # Weapon Shop
    ff5_bytes[0x112EA9] = 0x15 # Excalibur
    ff5_bytes[0x112EAA] = 0x28 # Thor's Hammer
    ff5_bytes[0x112EAB] = 0x2F # Masamune
    ff5_bytes[0x112EAC] = 0x37 # Wizard Rod
    ff5_bytes[0x112EAD] = 0x3D # Sage's Staff
    ff5_bytes[0x112EAE] = 0x45 # Yoichi Bow
    ff5_bytes[0x112EAF] = 0x4A # Apollo's Harp
    ff5_bytes[0x112EB0] = 0x4E # Flame Whip

    # Surgate Armor Shop
    ff5_bytes[0x112EB1] = 0x04 # Accessory Shop
    ff5_bytes[0x112EB2] = 0xAF # Guard Ring
    ff5_bytes[0x112EB3] = 0xC1 # Kaiser Knuckles
    ff5_bytes[0x112EB4] = 0xB5 # Running Shoes
    ff5_bytes[0x112EB5] = 0xD0 # Red Shoes
    ff5_bytes[0x112EB6] = 0xB1 # Giant's Glove
    ff5_bytes[0x112EB7] = 0x00 # Nothing
    ff5_bytes[0x112EB8] = 0x00 # Nothing
    ff5_bytes[0x112EB9] = 0x00 # Nothing

    # Moore Weapon Shop
    ff5_bytes[0x112EBA] = 0x01 # Weapon Shop
    ff5_bytes[0x112EBB] = 0x16 # Ragnarok
    ff5_bytes[0x112EBC] = 0x6A # Giant's Axe
    ff5_bytes[0x112EBD] = 0x3E # Judgement Staff
    ff5_bytes[0x112EBE] = 0x46 # Artemis Bow
    ff5_bytes[0x112EBF] = 0x53 # Tinkerbell
    ff5_bytes[0x112EC0] = 0x1E # Double Lance
    ff5_bytes[0x112EC1] = 0x60 # Wonder Wand
    ff5_bytes[0x112EC2] = 0x4F # Dragon Whip

    # Moore Armor Shop
    ff5_bytes[0x112EC3] = 0x00 # Magic Shop
    ff5_bytes[0x112EC4] = 0x54 # Phoenix
    ff5_bytes[0x112EC5] = 0x55 # Leviathan
    ff5_bytes[0x112EC6] = 0x56 # Bahamut
    ff5_bytes[0x112EC7] = 0x00 # Nothing
    ff5_bytes[0x112EC8] = 0x00 # Nothing
    ff5_bytes[0x112EC9] = 0x00 # Nothing
    ff5_bytes[0x112ECA] = 0x00 # Nothing
    ff5_bytes[0x112ECB] = 0x00 # Nothing

    # Moore White Magic Shop
    ff5_bytes[0x112ECC] = 0x00 # Magic Shop
    ff5_bytes[0x112ECD] = 0x1E # Cure 3
    ff5_bytes[0x112ECE] = 0x1F # Wall
    ff5_bytes[0x112ECF] = 0x20 # Berserk
    ff5_bytes[0x112ED0] = 0x21 # Life 2
    ff5_bytes[0x112ED1] = 0x22 # Holy
    ff5_bytes[0x112ED2] = 0x23 # Dispel
    ff5_bytes[0x112ED3] = 0x8A # Tiny Song
    ff5_bytes[0x112ED4] = 0x91 # Aero 3

    # Moore Black Magic Shop
    ff5_bytes[0x112ED5] = 0x00 # Magic Shop
    ff5_bytes[0x112ED6] = 0x30 # Fire 3
    ff5_bytes[0x112ED7] = 0x31 # Ice 3
    ff5_bytes[0x112ED8] = 0x32 # Bolt 3
    ff5_bytes[0x112ED9] = 0x33 # Flare
    ff5_bytes[0x112EDA] = 0x34 # Doom
    ff5_bytes[0x112EDB] = 0x35 # Psych
    ff5_bytes[0x112EDC] = 0x82 # Condemn
    ff5_bytes[0x112EDD] = 0x83 # Roulette

    # Moore Dimen Magic Shop
    ff5_bytes[0x112EDE] = 0x00 # Magic Shop
    ff5_bytes[0x112EDF] = 0x42 # Demi 2
    ff5_bytes[0x112EE0] = 0x43 # Haste 2
    ff5_bytes[0x112EE1] = 0x44 # Old
    ff5_bytes[0x112EE2] = 0x45 # Meteo
    ff5_bytes[0x112EE3] = 0x46 # Quick
    ff5_bytes[0x112EE4] = 0x47 # X-Zone
    ff5_bytes[0x112EE5] = 0x9A # Mighty Guard
    ff5_bytes[0x112EE6] = 0x97 # Mind Blast

    # Trench Weapon Shop
    ff5_bytes[0x112F0B] = 0x05 # Weapon/Throwable Shop
    ff5_bytes[0x112F0C] = 0x63 # Chicken Knife
    ff5_bytes[0x112F0D] = 0x61 # Brave Blade
    ff5_bytes[0x112F0E] = 0x30 # Tempest
    ff5_bytes[0x112F0F] = 0x20 # Dragoon Lance
    ff5_bytes[0x112F10] = 0x5B # Pinwheel
    ff5_bytes[0x112F11] = 0x00 # Nothing
    ff5_bytes[0x112F12] = 0x00 # Nothing
    ff5_bytes[0x112F13] = 0x00 # Nothing

    # Trench Armor Shop
    ff5_bytes[0x112F14] = 0x00 # Magic Shop
    ff5_bytes[0x112F15] = 0x54 # Nothing
    ff5_bytes[0x112F16] = 0x55 # Nothing
    ff5_bytes[0x112F17] = 0x56 # Nothing
    ff5_bytes[0x112F18] = 0x00 # Nothing
    ff5_bytes[0x112F19] = 0x00 # Nothing
    ff5_bytes[0x112F1A] = 0x00 # Nothing
    ff5_bytes[0x112F1B] = 0x00 # Nothing
    ff5_bytes[0x112F1C] = 0x00 # Nothing

    # Mirage Village Weapon Shop (Backing up Walse Weapon Shop)
    ff5_bytes[0x112F26] = 0x01 # Weapon Shop
    ff5_bytes[0x112F27] = 0x0F # Mythril Sword
    ff5_bytes[0x112F28] = 0x19 # Mythril Spear
    ff5_bytes[0x112F29] = 0x21 # Battle Axe
    ff5_bytes[0x112F2A] = 0x32 # Fire Rod
    ff5_bytes[0x112F2B] = 0x33 # Ice Rod
    ff5_bytes[0x112F2C] = 0x34 # Thunder Rod
    ff5_bytes[0x112F2D] = 0x06 # Mage Masher
    ff5_bytes[0x112F2E] = 0x05 # Kunai

    # Mirage Village Throwable Shop (Backing up Lix Throwable Shop)
    ff5_bytes[0x112F2F] = 0x05 # Weapon/Throwable Shop
    ff5_bytes[0x112F30] = 0x5A # Shuriken
    ff5_bytes[0x112F31] = 0x6C # Thief Knife
    ff5_bytes[0x112F32] = 0x12 # Epee
    ff5_bytes[0x112F33] = 0x08 # Kodachi
    ff5_bytes[0x112F34] = 0x17 # Javelin
    ff5_bytes[0x112F35] = 0x25 # Venom Axe
    ff5_bytes[0x112F36] = 0x2C # Bizen
    ff5_bytes[0x112F37] = 0x44 # Elven Bow

    # Mirage Village Armor Shop (Backing up Walse Armor Shop)
    ff5_bytes[0x112F38] = 0x02 # Armor Shop
    ff5_bytes[0x112F39] = 0x84 # Mythril Shield
    ff5_bytes[0x112F3A] = 0x85 # Golden Shield
    ff5_bytes[0x112F3B] = 0x96 # Bandana
    ff5_bytes[0x112F3C] = 0xA2 # Training Suit
    ff5_bytes[0x112F3D] = 0x91 # Tricorn
    ff5_bytes[0x112F3E] = 0xAA # Bard's Supplice
    ff5_bytes[0x112F3F] = 0x8C # Mythril Helmet
    ff5_bytes[0x112F40] = 0x9D # Mythril Armor

    # Mirage Village Accessory Shop (Backing up Istory Accessory Shop)
    ff5_bytes[0x112F41] = 0x04 # Accessory Shop
    ff5_bytes[0x112F42] = 0xC0 # Leather Shoes
    ff5_bytes[0x112F43] = 0xB4 # Glasses
    ff5_bytes[0x112F44] = 0xB2 # Elf Cape
    ff5_bytes[0x112F45] = 0xB6 # Mythril Glove
    ff5_bytes[0x112F46] = 0xB7 # Silver Armlet
    ff5_bytes[0x112F47] = 0xBD # Flame Ring
    ff5_bytes[0x112F48] = 0xBE # Coral Ring
    ff5_bytes[0x112F49] = 0xBC # Angel Ring

    # Mirage Village Level 6 Magic Shop (Backing up Lix Magic Shop)
    ff5_bytes[0x112F4A] = 0x00 # Magic Shop
    ff5_bytes[0x112F4B] = 0x4D # Ifrit
    ff5_bytes[0x112F4C] = 0x4C # Ramuh
    ff5_bytes[0x112F4D] = 0x4E # Titan
    ff5_bytes[0x112F4E] = 0x4F # Golem
    ff5_bytes[0x112F4F] = 0x50 # Shoat
    ff5_bytes[0x112F50] = 0x51 # Carbuncle
    ff5_bytes[0x112F51] = 0x52 # Syldra
    ff5_bytes[0x112F52] = 0x53 # Odin

    # Mirage Village Missable Magic Shop (Backing up Walse Magic Shop)
    ff5_bytes[0x112F53] = 0x00 # Magic Shop
    ff5_bytes[0x112F54] = 0x36 # Drag
    ff5_bytes[0x112F55] = 0x37 # Slow
    ff5_bytes[0x112F56] = 0x38 # Regen
    ff5_bytes[0x112F57] = 0x39 # Void
    ff5_bytes[0x112F58] = 0x3A # Haste
    ff5_bytes[0x112F59] = 0x3B # Float
    ff5_bytes[0x112F5A] = 0x58 # Speed Song
    ff5_bytes[0x112F5B] = 0x59 # Vitality Song

    # Mirage Village Item Shop (Backing up Lix Cheap Item Shop)
    ff5_bytes[0x112F5C] = 0x03 # Item Shop
    ff5_bytes[0x112F5D] = 0xEF # Magic Lamp
    ff5_bytes[0x112F5E] = 0xF2 # Giant Drink
    ff5_bytes[0x112F5F] = 0xF3 # Power Drink
    ff5_bytes[0x112F60] = 0xF4 # Speed Drink
    ff5_bytes[0x112F61] = 0xF5 # Protect Drink
    ff5_bytes[0x112F62] = 0xF6 # Hero Drink
    ff5_bytes[0x112F63] = 0x00 # Nothing
    ff5_bytes[0x112F64] = 0x00 # Nothing

    # Mirage Village Elixir Shop (Backing up Lix Armor Shop)
    ff5_bytes[0x112F65] = 0x02 # Armor Shop
    ff5_bytes[0x112F66] = 0x98 # Dark Hood
    ff5_bytes[0x112F67] = 0xA6 # Dark Suit
    ff5_bytes[0x112F68] = 0xCF # Raibnbow Dress
    ff5_bytes[0x112F69] = 0x93 # Circlet
    ff5_bytes[0x112F6A] = 0xAD # White Robe
    ff5_bytes[0x112F6B] = 0xAC # Black Robe
    ff5_bytes[0x112F6C] = 0xC7 # Genji Helmet
    ff5_bytes[0x112F6D] = 0xC8 # Genji Armor

    return ff5_bytes
