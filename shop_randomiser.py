#!/usr/bin/env python3


from mappings import shop_type_flag_memory_locations, shop_types, useful_shop_types, missable_shops_type_addresses, shared_shops, shop_goods_mappings
from mappings import weapon_codes, armor_codes, accessory_codes, item_codes, magic_codes, job_codes
from mappings import weapons, armors, accessories, items, spells, jobs
from fixed import fixed_mod

from typing import Dict, Tuple, List
from random import choice, shuffle, seed
from struct import pack
from argparse import ArgumentParser, Namespace
from sys import exit

import os



ff5_bytes: List[int] = []
latest_selected_shop_type: int = -1


def parse_arguments() -> Tuple[str, str]:
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument("-i", "--input_rom", type=str, metavar="input_rom", required=True)
    parser.add_argument("-o", "--output_rom", type=str, metavar="output_rom", required=True)
    parser.add_argument("--overwrite", action="store_true", required=False)
    parser.add_argument("--fixed", action="store_true", required=False)

    args: Namespace = parser.parse_args()
    input_rom: str = args.input_rom
    output_rom: str = args.output_rom
    overwrite: str = args.overwrite
    fixed: str = args.fixed

    if not os.path.isabs(input_rom):
        input_rom = os.path.join(os.getcwd(), input_rom)

    if not os.path.exists(input_rom):
        print("{} does not seem to exist. Aborting.".format(input_rom))
        exit(-1)

    if not overwrite and os.path.isfile(output_rom):
        print("{} already exist. Use --overwrite to forcefully overwrite it.".format(output_rom))
        exit(-1)

    if os.path.exists(output_rom) and not os.path.isfile(output_rom):
        print("{} already exists, and it is not a regular file. Aborting for safety.".format(output_rom))

    return input_rom, output_rom, fixed


def main():
    input_rom, output_rom, fixed = parse_arguments()

    global ff5_bytes
    ff5_bytes = load_rom_data(rom_path=input_rom)

    if fixed:
        ff5_bytes = fixed_mod(ff5_bytes=ff5_bytes)
    else:
        randomise()

    # Everything free in every weapon/armor/item shop.
    for i in range(0x112A00, 0x112CFF + 1):
        ff5_bytes[i] = 0x00

    # Everything free in every magic shop.
    for i in range(0x380000, 0x380096 + 1):
        ff5_bytes[i] = 0x00

    save_data_to_rom(ff5_edited_bytes=ff5_bytes, rom_path=output_rom)

    spoiler_log: List[str] = generate_spoiler_log()
    write_spoiler_log(spoiler_log=spoiler_log, output_file_path="{}.spoiler_log.txt".format(output_rom))


def load_rom_data(rom_path: str) -> List[int]:
    assert os.path.isfile(rom_path)

    with open(rom_path, "rb") as f:
        return [b for  b in f.read()]

def save_data_to_rom(ff5_edited_bytes: List[int], rom_path: str) -> None:
    assert not  os.path.exists(rom_path) or os.path.isfile(rom_path) # The check for --overwrite has been already performed.
    assert ff5_edited_bytes is not None

    for b in ff5_edited_bytes:
        assert b is not None and type(b) == int and b >=0x00 and b <= 0xFF

    with open(rom_path, "wb") as f:
        for b in ff5_edited_bytes:
            f.write(pack("=B", b))

        f.flush()


def generate_spoiler_log(ff5_bytes_ro: List[int]=None) -> List[str]:
    if not ff5_bytes_ro:
        global ff5_bytes
    else:
        ff5_bytes = ff5_bytes_ro

    spoiler_log: List[str] = []

    for location, shops in shop_type_flag_memory_locations.items():
        if location != "dummy":
            spoiler_log.append(location + ":")

            for shop_type_name, shop_type_address in shops.items():
                new_shop_type_name: str = next(k for k, v in shop_types.items() if v == ff5_bytes[shop_type_address])

                spoiler_log.append("    originally: {} - now: {}:".format(shop_type_name, new_shop_type_name))

                for good_code in [ff5_bytes[i] for i in range(shop_type_address + 1, shop_type_address + 9)]:
                    good_name: str = get_good_name_from_code_and_type(good_code=good_code, shop_type_address=shop_type_address)
                    spoiler_log.append("        {}".format(good_name))
            
                spoiler_log.append("    ----------")
            spoiler_log += append_shared_shops(location)

    spoiler_log += append_dummy_shops_data()

    return spoiler_log


def append_shared_shops(location: str) -> List[str]:
    to_return: list[str] = []

    if location in shared_shops.keys():
        for shop in shared_shops[location]:
            to_return.append("    {}".format(shop))
            to_return.append("    ----------")

    return to_return


def append_dummy_shops_data() -> List[str]:
    global ff5_bytes

    dummy_spoiler_log: List[str] = []
    dummy_shops: Dict[str, Dict[str, int]] = {kk: vv for k, v in shop_type_flag_memory_locations.items() if k == "dummy" for kk, vv in v.items()}

    for dummy_shop_type, shops in dummy_shops.items():
        for _, shop_type_address in shops.items():
            new_shop_type_name: str = next(k for k, v in shop_types.items() if v == ff5_bytes[shop_type_address])
            dummy_spoiler_log.append("Originally: dummy {} shop - now: {} at {}:".format(dummy_shop_type, new_shop_type_name, hex(shop_type_address)))

            for good_code in [ff5_bytes[i] for i in range(shop_type_address + 1, shop_type_address + 9)]:
                good_name: str = get_good_name_from_code_and_type(good_code=good_code, shop_type_address=shop_type_address)
                dummy_spoiler_log.append("    {}".format(good_name))

    return dummy_spoiler_log


def get_good_name_from_code_and_type(good_code: int, shop_type_address: int) -> str:
    if good_code == 0x00:
        return "-"
    elif ff5_bytes[shop_type_address] == 0x00:
        return identify_magic(good_code=good_code)
    elif ff5_bytes[shop_type_address] in (0x01, 0x03, 0x05, 0x06, 0x81, 0x83):
        return identify_mixed_weapon_item(good_code=good_code)
    elif ff5_bytes[shop_type_address] in (0x02, 0x04, 0x82):
        return identify_mixed_armor_accessory(good_code=good_code)
    elif ff5_bytes[shop_type_address] == 0x07:
        return identify_job_class(good_code=good_code)
    else:
        return "Unknown ({})".format(hex(good_code))


def identify_magic(good_code: int) -> str:
    for _, magic_list in spells.items():
        for magic_name, magic_code in magic_list.items():
            if good_code == magic_code:
                return magic_name

    return "Unknown spell/summon/msword/song ({})".format(hex(good_code))


def identify_weapon(good_code: int) -> str:
    for _, weapon_list in weapons.items():
        for weapon_name, weapon_code in weapon_list.items():
            if good_code == weapon_code:
                return weapon_name

    return "Unknown weapon ({})".format(hex(good_code))


def identify_mixed_armor_accessory(good_code: int) -> str:
    for _, armor_list in armors.items():
        for _, armor_sublist in armor_list.items():
            for armor_name, armor_code in armor_sublist.items():
                if good_code == armor_code:
                    return armor_name

    accessory: str = identify_accessory(good_code=good_code)

    if not "Unknown" in accessory:
        return accessory
    else:
        return "Unknown armor ({})".format(hex(good_code))


def identify_item(good_code: int) -> str:
    for item_name, item_code in items.items():
        if good_code == item_code:
            return item_name

    return "Unknown item ({})".format(hex(good_code))


def identify_accessory(good_code: int) -> str:
    for accessory_name, accessory_code in accessories.items():
        if good_code == accessory_code:
            return accessory_name

    return "Unknown accessory ({})".format(hex(good_code))


def identify_mixed_weapon_item(good_code: int) -> str:
    weapon: str = identify_weapon(good_code=good_code)

    if "Unknown" in weapon:
        it: str = identify_item(good_code=good_code)

        if "Unknown" in it:
            return "Unknown weapon or item: ({})".format(hex(good_code))
        else:
            return it
    else:
        return weapon


def identify_job_class(good_code: int) -> str:
    for job_name, job_code in jobs.items():
        if good_code == job_code:
            return job_name

    return "Unknown job class ({})".format(hex(good_code))


def write_spoiler_log(spoiler_log: List[str], output_file_path: str) -> None:
    with open(output_file_path, "w") as f:
        for line in spoiler_log:
            f.write(line + "\n")

        f.flush()


def randomise() -> None:
    useful_shops: Dict[str, Dict[str, int]] = {k: v for k, v in shop_type_flag_memory_locations.items() if k != "dummy"}
    dummy_shops: Dict[str, Dict[str, int]] = {kk: vv for k, v in shop_type_flag_memory_locations.items() if k == "dummy" for kk, vv in v.items()}
    mirage_shops: Dict[str, int] = shop_type_flag_memory_locations["mirage"]

    fill_dummy_shops(dummy_shops=dummy_shops)

    seed()

    shuffle(weapon_codes)
    shuffle(armor_codes)
    shuffle(accessory_codes)
    shuffle(item_codes)
    shuffle(magic_codes)
    shuffle(job_codes)

    randomise_shops(useful_shops=useful_shops)
    copy_missable_shops_to_mirage(mirage_shops=mirage_shops)


def copy_missable_shops_to_mirage(mirage_shops: Dict[str, int]) -> None:
    global ff5_bytes

    mirage_shops_type_address_list: List[int] = list(mirage_shops.values())

    shuffle(mirage_shops_type_address_list)

    assert len(missable_shops_type_addresses) <= len(mirage_shops_type_address_list)

    for missable_shop_type_address in missable_shops_type_addresses:
        replacement_shop_type_address: int = mirage_shops_type_address_list.pop()
        ff5_bytes[replacement_shop_type_address] = ff5_bytes[missable_shop_type_address]

        for i in range(1, 9):
            ff5_bytes[replacement_shop_type_address + i] = ff5_bytes[missable_shop_type_address + i]


def fill_dummy_shops(dummy_shops: Dict[str, Dict[str, int]]) -> None:
    global ff5_bytes
    
    current_item_code: int = 0xE0

    for _, shops in dummy_shops.items():
        for _, shop_type_address in shops.items():
            ff5_bytes[shop_type_address] = 0x03 # We force an item shop
            for i in range(1, 9):
                ff5_bytes[shop_type_address + i] = current_item_code
            
            current_item_code += 1

def randomise_shops(useful_shops: Dict[str, Dict[str, int]]) -> None:
    for _, shops in useful_shops.items():
        for shop_name, shop_type_address in shops.items():
            if not "arrest" in shop_name:
                randomise_shop(shop_type_address=shop_type_address)
            else:
                manage_karnak_temporary_shop(shop_type_address=shop_type_address)


def manage_karnak_temporary_shop(shop_type_address: int) -> None:
    # Make this Karnak temporary shops sell nothing (it also becomes a magic shop).
    for i in range(9):
        ff5_bytes[shop_type_address + i] = 0x00


def randomise_shop(shop_type_address: int) -> None:
    global ff5_bytes, latest_selected_shop_type

    shop_type, remaining_entries_for_type = select_shop_type()
    latest_selected_shop_type = shop_type

    assert shop_type is not None and remaining_entries_for_type >= 0

    ff5_bytes[shop_type_address] = shop_type

    if remaining_entries_for_type == 0:
        for i in range(0, 9):
            ff5_bytes[shop_type_address + i] = 0x00
    else:
        place_stuff_in_shop(shop_type=shop_type, shop_type_address=shop_type_address, remaining_entries_for_type=remaining_entries_for_type)
        fill_leftover_spots(shop_type_address=shop_type_address, remaining_entries_for_type=remaining_entries_for_type)

        remaining_entries_for_type -= min(remaining_entries_for_type, 8)


def select_shop_type() -> Tuple[int, int]:
    remaining_shop_types: List[int] = [elm for elm in useful_shop_types]

    for shop_type_name, goods_list in shop_goods_mappings.items():
        if len(goods_list) == 0:
            remaining_shop_types.remove(shop_types[shop_type_name])

    if len(remaining_shop_types) == 0:
        return 0x00, 0 # We force all the remaining shops to be magic shops (not that it matters).
    else:
        return roll_shop_type(remaining_shop_types=remaining_shop_types)


def roll_shop_type(remaining_shop_types: List[int]) -> Tuple[int, int]:
    assert len(remaining_shop_types) > 0

    global latest_selected_shop_type

    if len(remaining_shop_types) == 1:
        candidate: int = remaining_shop_types[0]
    elif not latest_selected_shop_type in remaining_shop_types:
        candidate: int = choice(remaining_shop_types)
    else:
        candidate: int = choice([elm for elm in remaining_shop_types if elm != latest_selected_shop_type])

    return candidate, len(shop_goods_mappings[next(k for k, v in shop_types.items() if v == candidate)])


def place_stuff_in_shop(shop_type: int, shop_type_address: int, remaining_entries_for_type: int) -> None:
    global ff5_bytes

    for i in range(1, min(remaining_entries_for_type + 1, 9)):
        ff5_bytes[shop_type_address + i] = shop_goods_mappings[next(k for k, v in shop_types.items() if v == shop_type)].pop()


def fill_leftover_spots(shop_type_address: int, remaining_entries_for_type: int) -> None:
    global ff5_bytes
    
    # If there are not enough goods left, we make so the leftover spots for a particular shop contain nothing.
    if remaining_entries_for_type < 8:
        for i in range(remaining_entries_for_type + 1, 9):
            ff5_bytes[shop_type_address + i] = 0x00


if __name__ == "__main__":
    main()
