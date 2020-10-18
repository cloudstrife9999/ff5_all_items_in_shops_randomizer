#!/usr/bin/env python3


from argparse import ArgumentParser, Namespace
from typing import List

from shop_randomiser import generate_spoiler_log, load_rom_data, write_spoiler_log


import  os



ff5_bytes: List[int] = []


def parse_arguments() -> str:
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument("-i", "--input_rom", type=str, metavar="input_rom", required=True)

    args: Namespace = parser.parse_args()
    input_rom: str = args.input_rom

    if not os.path.isabs(input_rom):
        input_rom = os.path.join(os.getcwd(), input_rom)

    if not os.path.exists(input_rom):
        print("{} does not  see to exist. Aborting.".format(input_rom))
        exit(-1)

    return input_rom


def main():
    input_rom: str = parse_arguments()

    global ff5_bytes
    ff5_bytes = load_rom_data(rom_path=input_rom)

    spoiler_log: List[str] = generate_spoiler_log(ff5_bytes_ro=ff5_bytes)
    write_spoiler_log(spoiler_log=spoiler_log, output_file_path="{}.spoiler_log.txt".format(input_rom))


def load_rom_data(rom_path: str) -> List[int]:
    assert os.path.isfile(rom_path)

    with open(rom_path, "rb") as f:
        return [b for  b in f.read()]


if __name__ == "__main__":
    main()
