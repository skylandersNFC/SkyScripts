# SkyScripts

> [!TIP]
> To run any of the scripts, place them inside your main Skylanders dump directory and simply double-click.
> 
> Ensure you have Python installed beforehand.


## SkyUID_Duplicate_Checker.py

> [!NOTE]
> 
> It will scan all dumps in the main directory, including those in subfolders, and generate a list of dumps with duplicate UIDs.


### Example:

```
Scanning directory and subdirectories from: D:\Skylanders Ultimate NFC Pack\Dumps

Duplicate 4-byte HEX sequences found:

HEX: FC E4 24 29 - Found in files:
  4. Trap Team\9) Traps\1) Crystal Traps\Dark\Dark Spider (Shadow Spider).dump
  4. Trap Team\9) Traps\3) Trappable Villains\Dark\Tae Kwon Crow.dump
HEX: B6 0F DD 9D - Found in files:
  4. Trap Team\9) Traps\1) Crystal Traps\Dark\Dark Sword (Dark Dagger).dump
  4. Trap Team\9) Traps\3) Trappable Villains\Dark\Eye Scream.dump
  4. Trap Team\9) Traps\3) Trappable Villains\Dark\Fisticuffs.dump
  4. Trap Team\9) Traps\3) Trappable Villains\Dark\Nightshade (Doom Raider).dump
HEX: 90 E4 FA 2C - Found in files:
  4. Trap Team\9) Traps\1) Crystal Traps\Earth\Earth Handstand (Rubble Trouble).dump
  4. Trap Team\9) Traps\3) Trappable Villains\Earth\Tussle Sprout.dump
HEX: 6D 6B 35 4B - Found in files:
  4. Trap Team\9) Traps\1) Crystal Traps\Earth\Earth Hourglass (Dust of Time).dump
  4. Trap Team\9) Traps\3) Trappable Villains\Earth\Chomp Chest.dump
HEX: DF 25 B6 4A - Found in files:
  4. Trap Team\9) Traps\1) Crystal Traps\Fire\Fire Scepter (Fire Flower).dump
  4. Trap Team\9) Traps\3) Trappable Villains\Fire\Chef Pepper Jack (Doom Raider).dump
  4. Trap Team\9) Traps\3) Trappable Villains\Fire\Smoke Scream.dump
...
```

## SkyUID_Finder.py

> [!NOTE]
> 
> Enter a UID that you suspect belongs to a Skylander dump file, and the script will identify the corresponding Skylander if it matches.
> 
> For example, the UID `90377C9F` corresponds to the Bash dump file.

### Example:

```
Scanning directory and subdirectories from:

D:\Skylanders Ultimate NFC Pack\Dumps

Enter a 4-byte UID (or type 'exit' to quit): 90377C9F

The UID 90377C9F was found in the following file(s):
  1. Spyro's Adventure\1) Figures\Bash.dump
```

## Fix_Sector_0_Trailer_Access_Conditions.py

> [!NOTE]
> 
> Changes Sector 0 Trailer Access Conditions to 0xFF, 0x07, 0x80 for all dumps.

## Skylanders_CharID_and_VarID_Reader.py

> [!NOTE]
> 
> Reads Skylanders CharacterID and VariantID.

## Check_Sector_0_Trailer_Empty_Keys.py

> [!NOTE]
> 
> Checks if existing dumps have empty 0x00 keys on Sector 0 Trailer.

## Bulk Skylanders Reset

We have two variants of the scripts :

- Bulk_Skylanders_Reset.py
- Bulk_Skylanders_Imaginators_Reset.py

----------------------------------------

- Bulk_Skylanders_Reset.py is for Skylander dumps from SSA to SSC. It will reset all Skylanders to LVL 1.

----------------------------------------

- Bulk_Skylanders_Imaginators_Reset.py is the new script to be used for Bulk Imaginators dumps reset to LVL 1.
Have almost the same functionality and the script above, but the wiping requirements are different for Imaginators. Read bellow.

----------------------------------------
How does it works?
----------------------------------------

Just put several Skylanders .dump files in the same directory where you've placed the "Bulk_Skylanders_Reset.py" script (or whatever variant of the script you have).

You can also place folders and subfolders with dumps, those will be also processed and overwritten.
Then open "cmd" in that same directory and type:

python Bulk_Skylanders_Reset.py

* Or whatever script variant you have, like "python Bulk_Skylanders_Imaginators_Reset.py" or another one. You can also double-click on the .py file if you have the file extension associated with Python.

----------------------------------------
What does it do?
----------------------------------------

Bulk_Skylanders_Reset.py

It preserves data on:

`Sector 0`

`All Sector Trailers`

And wipes everything else.

----------------------------------------

Bulk_Skylanders_Imaginators_Reset.py and Bulk_Skylanders_Imaginators_Reset_Alt_Version.py

It preserves data on:

`Sector 0 (as the previous non-imaginators dumps)`

`All Sector Trailers (as the previous non-imaginators dumps)`

`Sector 1, Block 0 (Imaginators Signature Data)`

`Sector 8, Block 2 (Imaginators Signature Data)`

`Sector 15, Block 2 (Imaginators Signature Data)`

And wipes everything else.

----------------------------------------
Some HxD visualizations
----------------------------------------
![00. Skylanders Hex Explained](https://raw.githubusercontent.com/skylandersNFC/SkyScripts/main/img/Skylanders_Hex_Explained.png)

![01. Skylanders Resetting SSA - SSC](https://raw.githubusercontent.com/skylandersNFC/SkyScripts/main/img/Skylanders_Resetting_SSA_SSC.png)

![02. Skylanders Resetting Imaginators](https://raw.githubusercontent.com/skylandersNFC/SkyScripts/main/img/Skylanders_Resetting_Imaginators.png)