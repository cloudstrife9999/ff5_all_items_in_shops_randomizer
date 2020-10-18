# Final Fantasy V ALL-ITEMS-IN-SHOPS-FOR-FREE Randomizer

## The idea

The general idea of this randomizer is to be able to get unlimited amounts of every item (and one copy of every magic/job) in Final Fantasy V for free:

* Every `object` (`item/weapon/armor/accessory`) that usually appears in the `Item` menu is guaranteed to appear for free in exactly one shop (except for the missable shops which are backed-up in Mirage Village - see below).

* Two dummied-out weapons (`Sabre` and `Mythril Staff`) are also included. The Sabre is still not equippable by any job class, at the moment.

* Every `black magic`, `white magic`, `dimen/time magic`, `summon`, `blue magic`, and `song` is also guaranteed to be purchasable.

* Every `job class` is also guaranteed to be purchasable.

* Each original shop does not sell anymore its original goods, in order to  make room for the randomized goods.

* Every missable shop (those at `Walse`, `Istory`, and `Lix`) is backed-up in `Mirage Village`. There are 8 unique shops in total in those 3 locations, and exactly 8 shops in Mirage Village. How convenient!

* Every good is classified in one of 6 classes: `weapon`, `armor`, `item`, `accessory`, `magic`, `job`. Armor includes head and body pieces of equipment. Magic includes white, black, dimen/time, and blue spells, as well as summons and songs. `Magic swords` are not included (running out of available shops). However, getting a black/white magic will automatically get you the corresponding magic sword as well, if it exists.

* Every shop can only sell goods belonging to exactly 1 of the above categories (e.g., weapon shops only sell weapons). Each shop type is randomized as well, as may or may not match the original.

* `Karnak's pre-arrest` weapon and armor shops do not sell anything. Just quit the shop to trigger the arrest sequence.

## Compatibility

This randomiser is compatible with the following versions of Final Fantasy V:

* The `RPGe modded ROM` of Final Fantasy V for SNES.

* Any [Project Demi](https://www.bigbridge.studio/projectdemi/) modded ROM of Final Fantasy V for SNES, provided it was created from an RPGe modded ROM.

This randomiser is not compatible with any of the following versions of Final Fantasy V:

* The GBA, iOS, Android, and PC versions, regardless of region and language.

* The original Japanese version for SNES.

The compatibility with any other version (e.g., a [Career Day](https://www.bigbridge.studio/careerday/) modded ROM) is to be determined.

## HOWTO

Run the following command, and follow the resulting instructions

```console
python3 shop_randomiser.py
```
