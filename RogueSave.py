import datetime
import shutil
import re
import os

INVENTORY_SLOTS = 45
STORAGE_SLOTS = 360
ITEMS = {
    0:"Empty",
    1:"Planet Stone",
    2:"Orichalcum",
    3:"Galacticite",
    4:"Zephyr",
    5:"Flamethyst",
    6:"Existence Gem",
    11:"Tasty Herb",
    12:"Glowshroom",
    13:"Spicy Seed",
    14:"Star Fruit",
    15:"Aether Bulb",
    16:"Chaos Leaf",
    21:"Creature Eyeball",
    22:"Monster Claw",
    23:"Chitin Fragment",
    24:"Beast Heart",
    25:"Shiny Scale",
    26:"Ectoplasm",
    31:"Flutterfly",
    32:"Dung Beetle",
    33:"Ghast Bug",
    34:"Thunderworm",
    35:"Glowfly",
    36:"Plasma Moth",
    44:"Arena Ticket",
    45:"Magicite",
    46:"Aethercrystal",
    47:"Platinum Badge",
    48:"Remembrance Ticket",
    49:"Champion Badge",
    50:"Glob of Aether",
    51:"World Fragment",
    52:"Credit",
    53:"Ashen Dust",
    54:"Mystery Gift",
    55:"Ion Ticket",
    56:"Lightsworn Crystal",
    57:"Scrap Metal",
    58:"Quest Prize",
    59:"Wealth Trophy",
    60:"Health Pack I",
    61:"Mana Pack I",
    62:"Energy Pack I",
    63:"Droid Fuel",
    64:"Anti-Poison",
    65:"Health Pack II",
    66:"Mana Pack II",
    67:"Energy Pack II",
    68:"Anti-Frost",
    69:"Anti-Heat",
    70:"Health Pack III",
    71:"Mana Pack III",
    72:"Energy Pack III",
    73:"Elixir",
    74:"Demonbrew",
    86:"Aetherlite Shard",
    87:"Darkened Shard",
    88:"Omega Shard",
    89:"Aetherlite Crystal",
    90:"Darkemed Crystal",
    91:"Omega Crystal",
    101:"Planet Emblem",
    102:"Orichalcum Emblem",
    103:"Galacticite Emblem",
    104:"Zephyr Emblem",
    105:"Flame Emblem",
    106:"Existence Emblem",
    111:"Herb Emblem",
    112:"Shroom Emblem",
    113:"Seed Emblem",
    114:"Star Emblem",
    115:"Aether Emblem",
    116:"Chaos Emblem",
    121:"Eyeball Emblem",
    122:"Claw Emblem",
    123:"Fragment Emblem",
    124:"Beast Emblem",
    125:"Shiny Emblem",
    126:"Ectoplasm Emblem",
    131:"Flutterfly Emblem",
    132:"Bettle Emblem",
    133:"Ghast Emblem",
    134:"Thunderworm Emblem",
    135:"Glowfly Emblem",
    136:"Plasma Emblem",
    201:"BonusVIT+",
    202:"BonusSTR+",
    203:"BonusDEX+",
    204:"BonusTEC+",
    205:"BonusMAG+",
    206:"BonusFTH+",
    207:"ResistHeat+",
    208:"ResistFrost+",
    209:"ResistPoison+",
    210:"ProjectileRange+",
    211:"CritRate+",
    212:"CritDmg+",
    213:"HealthRegen+",
    214:"ManaRegen+",
    215:"StaminaRegen+",
    216:"MoveSpeed+",
    217:"DashSpeed+",
    218:"JumpHeight+",
    219:"OreHarvest+",
    220:"PlantHarvest+",
    221:"MonsterDrops+",
    222:"BugHarvest+",
    223:"ExpBoost+",
    224:"CreditBoost+",
    300:"Aetherblade",
    301:"Bolt Edge",
    302:"Colossus",
    303:"Doomguard",
    304:"Gadget Saber",
    305:"Ragnarok",
    312:"Mage Masher",
    313:"Fractured Soul",
    314:"Arcwind",
    315:"Trigoddess",
    316:"Flamberge",
    317:"Key of Hearts",
    318:"Excalibur",
    319:"Zweihander",
    320:"Heaven's Cloud",
    321:"Death Exalted",
    322:"Dark Messenger",
    323:"Ruin",
    324:"Claymore",
    325:"Forgeblade",
    326:"Lost Voice",
    327:"Valflame",
    328:"Helswath",
    329:"Awakened Force",
    345:"Azazel's Blade",
    346:"Ringabolt's Axe",
    347:"Caius' Demonblade",
    348:"Glitterblade",
    349:"4th Age Sword",
    350:"Aetherlance",
    351:"Runelance",
    352:"The Highwind",
    353:"Gallatria's Spire",
    354:"Abraxas",
    355:"Cain's Lance",
    362:"Galaxy Lance",
    363:"World's End",
    364:"Emblem Fates",
    365:"Doombringer",
    366:"Darkforce",
    367:"World Reborn",
    368:"King's Lance",
    369:"Gungnir",
    370:"Spirit Lance",
    371:"Firestorm",
    372:"Heartseeker",
    373:"Longinus",
    374:"Stormbringer",
    375:"Devilsbane",
    376:"Rampart Golem",
    377:"Dragon Whisker",
    378:"Vengeful Spirit",
    379:"Dragoon Lance",
    397:"Wallace's Lance",
    398:"Urugorak's Tooth",
    399:"4th Age Lance",
    400:"Aethergun Mk.IV",
    401:"Arcfire",
    402:"Frost",
    403:"Vengeance",
    404:"Judgement",
    405:"Golden Eye",
    406:"Thrasher",
    407:"Athena XVI",
    412:"Star Destroyer",
    413:"Quicksilver",
    414:"Repeater",
    415:"Magma",
    416:"Chaingun",
    417:"Oblivion",
    418:"Avalanche",
    419:"Atma Weapon",
    420:"Coldsnap",
    421:"Sirius",
    422:"Sonicsteel",
    423:"Death Penalty",
    424:"Fomalhaut",
    425:"Cataclysm",
    426:"Betrayer",
    427:"Golden Suns",
    428:"Cerberus",
    429:"Poopmaker",
    448:"Plaguesteel",
    449:"4th Age Gun",
    450:"Aethercannon",
    451:"Typhoon IX",
    452:"Auto Rifle",
    453:"Viking XXVII",
    454:"Bazooka",
    455:"The Wyvern",
    456:"Aqualung",
    457:"Heatcannon",
    462:"Commando",
    463:"Hypercannon",
    464:"Missile RPG",
    465:"Vorpal RPG",
    466:"The Dominator",
    467:"The Zapper",
    468:"Stormcannon",
    469:"The Machine",
    470:"Volt Sniper",
    471:"War-Forged Gun",
    472:"Carbine",
    473:"Gadget RPG",
    474:"Tropic Thunder",
    475:"Hand Cannon",
    476:"Flak Cannon",
    477:"Dragon Cannon",
    478:"Flame Swathe",
    479:"Wyvern Bone",
    496:"MEGA WEAPON",
    497:"GALACTIC FLAMEBLASTER",
    498:"Pirate Musket",
    499:"4th Age Cannon",
    500:"Mage Gauntlet",
    501:"Soul Reaver",
    502:"Flame Lash",
    503:"Wolt's Thunder",
    504:"Gaia's Gale",
    505:"Decimator",
    506:"Dargon Idol",
    507:"Red Lightning",
    512:"Mystic Arrow",
    513:"Elementalizer",
    514:"Flareblade",
    515:"Ice Wall",
    516:"Wrath Aura",
    517:"Nether Torrent",
    518:"Bolganone",
    519:"Caius' Pyre",
    520:"Elfire",
    521:"Gafgard's Maelstrom",
    522:"Maalurk Totem",
    523:"Monk Gauntlet",
    524:"Tornado",
    525:"Airsplitter",
    526:"Gruu's Talisman",
    527:"Destruction Wave",
    528:"Annihilation",
    529:"Banana",
    546:"Baalfog's Avalanche",
    547:"Moloch's Wrath",
    548:"Shroomhazzard",
    549:"4th Age Gauntlet",
    550:"Aetherstaff",
    551:"Pyroclasm",
    552:"Astra",
    553:"Thornwall",
    554:"Seraphim",
    555:"Nirvana",
    562:"Twilight Staff",
    563:"Enigma",
    564:"Summoner's Staff",
    565:"Armageddon",
    566:"Doomsayer",
    567:"Merciless Gladiator",
    568:"Bubblegum Staff",
    569:"Cherry Blossom",
    570:"The Whitemage",
    571:"Vinewhip",
    572:"Jungle King",
    573:"Sage's Staff",
    574:"Lightning Rod",
    575:"Caster Sword",
    576:"Seeker of Stars",
    577:"Maelstrom",
    578:"Darkness",
    579:"The Blackmage",
    597:"Perceval's Wand",
    598:"Hivemind Rod",
    599:"4th Age Staff",
    600:"Aethershield",
    601:"Cadet Buckler",
    602:"Aegis",
    603:"Bolt Shield",
    604:"Gallatria Sigil",
    605:"Force Guard",
    612:"Eagle Shield",
    613:"Leader's Crest",
    614:"Twilight Shield",
    615:"Arc's Buckler",
    616:"Soul Infusion",
    617:"Supernova",
    618:"Purifier",
    619:"Oathkeeper",
    620:"Tower Aegis",
    621:"King's Crest",
    622:"Champion Shield",
    623:"Spiked Lightning",
    624:"Blood Shield",
    625:"Heater Shield",
    626:"Fungi Shield",
    627:"Sunlight",
    628:"Blood Shield",
    629:"Peacekeeper",
    648:"Scarab Shell",
    700:"Recruit Helm",
    701:"Runerider Helm",
    702:"Nautilus Helm",
    703:"Vorpal Helm",
    704:"Titan Helm",
    705:"Isaac Helm",
    706:"Ultrom Helm",
    707:"Brute Helm",
    708:"Yoshimitsu Helm",
    709:"Ghost Helm",
    710:"Vigilante Helm",
    711:"Wraith Helm",
    712:"4th Age Helm [STR]",
    713:"4th Age Helm [DEX]",
    714:"4th Age Helm [MAG]",
    725:"Captain's Hat",
    726:"Urugorak's Hat",
    730:"Bolgon's Helm",
    731:"Broccoli Helm",
    732:"Dredger Helm",
    733:"Overworld Helm",
    734:"Scourge Helm",
    735:"Wallace's Helm",
    736:"Gromwell'S Helm",
    737:"Ringabolt's Helm",
    738:"Perceval's Helm",
    739:"Baalfog's Eye",
    740:"Azazel's Helm",
    750:"Elite Helm",
    751:"Voyager Helm",
    752:"Siege Helm",
    753:"Krabshell Helm",
    754:"Dunecloth",
    755:"Drifter Helm",
    756:"Leviathan Helm",
    757:"Kraken Helm",
    758:"Chaos Helm",
    759:"Ultima Helm",
    760:"Destruction Helm",
    761:"Ithaca's Helm",
    762:"Champion Helm",
    763:"Heroic Helm",
    764:"Deathgod Helm",
    765:"Shatterspell Helm",
    766:"Towermage Helm",
    767:"Deus Helm",
    768:"Plasma Helm",
    769:"Rapture Helm",
    770:"Firegod Helm",
    771:"Bruiser Helm",
    772:"Inferno Helm",
    773:"Ironforge Helm",
    774:"Yojimbo Helm",
    775:"Oni Helm",
    776:"Aku Helm",
    777:"Recon Helm",
    778:"Force Helm",
    779:"Helloworld Helm",
    780:"Darkknight Helm",
    781:"Onslaught Helm",
    782:"Whitewhorl Helm",
    783:"Maelstrom Helm",
    784:"Ruin Helm",
    785:"Pyroclasm Helm",
    800:"Recruit Armor",
    801:"Runerider Armor",
    802:"Nautilus Armor",
    803:"Vorpal Armor",
    804:"Titan Armor",
    805:"Isaac Armor",
    806:"Ultrom Armor",
    807:"Brute Armor",
    808:"Yoshimitsu Armor",
    809:"Ghost Armor",
    810:"Vigilante Armor",
    811:"Wraith Armor",
    812:"4th Age Armor",
    830:"Bolgon's Armor",
    831:"Broccoli Armor",
    832:"Dredger Armor",
    839:"Baalfog's Suit",
    840:"Azazel's Armor",
    850:"Elite Armor",
    851:"Voyager Armor",
    852:"Siege Armor",
    853:"Krabshell Armor",
    854:"Dunecloth",
    855:"Drifter Armor",
    856:"Leviathan Armor",
    857:"Kraken Armor",
    858:"Chaos Armor",
    859:"Ultima Armor",
    860:"Destruction Armor",
    861:"Ithaca's Armor",
    862:"Champion Armor",
    863:"Heroic Armor",
    864:"Deathgod Armor",
    865:"Shatterspell Armor",
    866:"Towermage Armor",
    867:"Deus Armor",
    868:"Plasma Armor",
    869:"Rapture Armor",
    870:"Firegod Armor",
    871:"Bruiser Armor",
    872:"Inferno Armor",
    873:"Ironforge Armor",
    874:"Yojimbo Armor",
    875:"Oni Armor",
    876:"Aku Armor",
    877:"Recon Armor",
    878:"Force Armor",
    879:"Helloworld Armor",
    880:"Darkknight Armor",
    881:"Onslaught Armor",
    882:"Whitewhorl Armor",
    883:"Maelstrom Armor",
    884:"Ruin Armor",
    885:"Pyroclasm Armor",
    900:"Gallahad Ring",
    901:"Ezerius Ring",
    902:"Anelice Ring",
    903:"Gromwell Ring",
    904:"Brym Ring",
    905:"Falstadt Ring",
    906:"Roehn Ring",
    907:"Perceval Ring",
    908:"Owain Ring",
    909:"Tydus Ring",
    910:"Vaati Ring",
    1000:"RCK 22",
    1001:"FLWR 08",
    1002:"BAT 17",
    1003:"OBSIDIAN 64",
    1004:"HELPR 55",
    1005:"GUARDIAN 07",
    1012:"SOLAR 05",
    1013:"PRISM 88",
    1014:"MONOLTH 25",
    1015:"FARMHAND 78",
    1016:"BULB 88",
    1017:"BTTRFLY 8",
    1018:"DRAGON 67",
    1019:"WYVRN 77",
    1020:"MEGAZORD 36",
    1021:"STEEL 65",
    1022:"DIAMND 66",
    1023:"BOGBOT 67",
    1024:"AIDBOT 56",
    1025:"HELLBOT 57",
    1026:"iBOT 58",
    1027:"WHITEMAG 09",
    1028:"OVERSEER 06",
    1029:"MRGRGRR 05",
    1030:"GOLD 15",
    2000:"Scrap Metal Block",
    2001:"Glass Block",
    2002:"Firesteel Block",
    2100:"Storage Block",
    2101:"Forge Block",
    2102:"Emblem Block",
    2103:"Combat Block",
    2104:"Alchemy Block",
    2105:"Computer Block",
    2106:"Portal Block",
    2107:"Ship Droid Block",
    2108:"Door Block",
    2200:"Scrap Metal Wall",
    2300:"Scrap Metal Platform",
    2400:"Engine Block",
    2401:"Blue Light",
    2402:"Red Light",
    2403:"Spawn Location",
    2501:"Shmoo Card",
    2502:"Eyepod Card",
    2503:"Dunebug Card",
    2504:"Worm Card",
    2505:"Wasp Card",
    2506:"Urugorak Card",
    2507:"Sluglord Card",
    2508:"Slugmother Card",
    2509:"Chamcham Card",
    2510:"Rhinobug Card",
    2511:"Hivemind Card",
    2512:"Glibglob Card",
    2513:"Slime Card",
    2514:"Rock Spider Card",
    2515:"Sploopy Card",
    2516:"Rock Scarab Card",
    2517:"Shroom Card",
    2518:"Blue Shroom Card",
    2519:"Shroom Bully Card",
    2520:"Relicfish Card",
    2521:"Ancient Guard Card",
    2522:"Ancient Beast Card",
    2523:"Roach Card",
    2524:"Card",
    2525:"Squirm Card",
    2526:"Plague Caster Card",
    2527:"Glitterbug Card",
    2528:"Plaguebeast Card",
    2529:"Space Pirate Card",
    2530:"Wicked Card",
    2531:"Wisp Card",
    2532:"Yeti Card",
    2533:"Mammoth Card",
    2534:"Wyvern Card",
    2535:"Lava Blob Card",
    2536:"Fire Slime Card",
    2537:"Lava Dragon Card",
    2538:"Tyrannog Card",
    2539:"Beelzeblob Card",
    2540:"Gruu Card",
    2541:"Treant Card",
    2542:"Willowwart Card",
    2543:"Caius Card",
    2544:"Moloch Card",
    2600:"Brave Badge",
    2601:"Magicite Badge",
    2602:"Destroyer Badge",
    2603:"Pious Badge",
    2604:"Creator Badge",
    2605:"Science Badge",
    2606:"Rebellion Badge",
    2607:"Starlight Badge",
    2608:"Justice Badge",
    2609:"Enigma Badge",
    2610:"Darkweapon Badge",
    2611:"Zeig Badge"
}
RACES = [
    "Wanderer",
    "Royalite",
    "Centurion",
    "Illuminate",
    "Shlaami",
    "Fishfolk",
    "Gekko",
    "Nomad",
    "Deathrazor",
    "Hiveling",
    "Ancient",
    "Lightsworn",
    "Drifter",
    "Goblin",
    "Swampfolk",
    "Tiki",
    "Titan",
    "Trogon",
    "Scaled",
    "Florbgon",
    "Oompa",
    "Wizened",
    "Necro",
    "Golem",
    "Avalancher",
    "Boogoo",
    "Afflicted",
    "Runefolk",
    "Overseer",
    "Bunyip"
]
UNIFORMS = [
    "Fleet Cadet",
    "Hero",
    "Scholar",
    "Explorer",
    "Pyromancer",
    "Fairy",
    "Seer",
    "Soldier",
    "Blacksmith",
    "President",
    "Gadget Worker",
    "Minister",
    "Antihero",
    "Dirtmage",
    "Beehive",
    "Monster Trainer",
    "Scientist",
    "Crusader",
    "Echo",
    "Metalgear",
    "Pheonix",
    "Cobalt Mage",
    "Peasant",
    "Overworld"
]
TRAITS = [
    "Vitality",
    "Strength",
    "Dexterity",
    "Tech",
    "Magic",
    "Faith"
]
CLASSES = [
    "Enforcer",
    "Gunner",
    "Machinist",
    "Darkmage",
    "Aethermage",
    "Blademaster",
    "Dragoon",
    "Spellblade",
    "Aetherknight",
    "Bounty Hunter",
    "Gunmage",
    "Commander",
    "Datamancer",
    "Alchemist",
    "Arcanist"
]
AUGMENTS = [
    "None",
    "Crusader Hat",
    "Rogue Bandana",
    "Berserker Scarf",
    "Mage Hat",
    "Crown",
    "Shmoo Hat",
    "Glibglob Hat",
    "Beats by Boizu",
    "Eyepod Hat",
    "Slime Hat",
    "Mech City Beanie",
    "Lucky Pumpkin",
    "Eye Gadget",
    "Baby Silver",
    "Oculus Goggles",
    "Chamcham Hat",
    "Demon Horns",
    "Forsaker Mask",
    "Shroom Hat",
    "Halo",
    "Creator Mask",
    "Rebellion Headpiece",
    "Gas Mask"
]
ALLEGIANCES = [
    "Galatic Fleet",
    "Starlight Rebellion",
    "Church of Faust",
    "Gray Enigma",
    "Junkbelt Mercenaries",
    "Droidtech Enterprise"
]

class Save:
    """
    Save data for one PlayerPrefs file.
    saveFilePath: the absolute path to the save file
    """

    def __init__(self, saveFilePath):
        #shutil.copy(saveFilePath, saveFilePath + " %s.bak" % datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S"))
        with open(saveFilePath) as saveFile:
            saveFileContents = saveFile.read()
            saveFileContents = re.sub(r"\s", "", saveFileContents)
            self.saveContents = dict(item.split(":", 1) for item in saveFileContents.split(";"))
            for key in list(self.saveContents.keys()):
                self.saveContents[key] = self.saveContents[key].split(":")[0]

        self.characters = list()
        for key in list(self.saveContents.keys()):
            if "name" in key:
                i = int(key[0])
                self.characters.append(Character(self, i))

        self.storageLevel = int(self.saveContents["storageLevel"])
        self.storage = list()
        for i in range(STORAGE_SLOTS):
            itemId = int(self.saveContents["storage%iid" % i])
            tier = int(self.saveContents["storage%itier" % i])
            quantity = int(self.saveContents["storage%iq" % i])
            exp = int(self.saveContents["storage%iexp" % i])
            self.storage.append(Item(itemId, tier, quantity, exp))


class Character:
    """
    A character and its inventory.
    save: save instance containing this character
    id: the character's id
    """

    def __init__(self, save, id):
        self.id = id
        self.name = save.saveContents["%iname" % id]
        self.level = int(save.saveContents["%ilevel" % id])
        self.hp = int(save.saveContents["%ihp" % id])
        self.mana = int(save.saveContents["%imana" % id])
        self.race = int(save.saveContents["%irace" % id])
        self.variant = int(save.saveContents["%ivariant" % id])
        self.uniform = int(save.saveContents["%iuniform" % id])
        self.trait0 = int(save.saveContents["%itrait0" % id])
        self.trait1 = int(save.saveContents["%itrait1" % id])
        self.lifetime = int(save.saveContents["%ilifetime" % id])
        self.exp = int(save.saveContents["%iexp" % id])
        self.augment = int(save.saveContents["%iaugment" % id])
        self.traitClass = int(save.saveContents["%iclass" % id])
        self.allegience = int(save.saveContents["%iallegiance" % id])
        self.vitality = int(save.saveContents["%ipStat0" % id])
        self.strength = int(save.saveContents["%ipStat1" % id])
        self.dexterity = int(save.saveContents["%ipStat2" % id])
        self.tech = int(save.saveContents["%ipStat3" % id])
        self.magic = int(save.saveContents["%ipStat4" % id])
        self.faith = int(save.saveContents["%ipStat5" % id])

        self.inventory = list()
        for i in range(INVENTORY_SLOTS):
            itemId = int(save.saveContents["%i%iid" % (id, i)])
            tier = int(save.saveContents["%i%itier" % (id, i)])
            quantity = int(save.saveContents["%i%iq" % (id, i)])
            exp = int(save.saveContents["%i%iexp" % (id, i)])
            self.inventory.append(Item(itemId, tier, quantity, exp))

class Item:
    """
    An item and its stats.
    id: the item's id
    tier: the items's tier
    quanitity: the item's quanitity
    exp: the item's experience
    """

    def __init__(self, id, tier, quantity, exp):
        self.id = id
        self.tier = tier
        self.quantity = quantity
        self.exp = exp

def characterSelect(save):
    """
    Display the save's characters and storage and allow the user to choose
    one to interact with.
    save: the save instance to use
    """

    for i in range(len(save.characters)):
        print("%i: %s" % (i, save.characters[i].name))
    print("%i: Storage" % len(save.characters))
    print("--")

    try:
        choice = int(input("Choice: "))
        if choice < 0 or choice > len(save.characters):
            raise ValueError
    except ValueError:
        print("Please select one of the options listed.")
        characterSelect(save)
        return

    if choice == len(save.characters):
        showStorage(save)
    else:
        showCharacter(save, choice)

def showStorage(save):
    """
    Display the items in and properties of a save's storage and allow the user
    to choose one to interact with.
    save: the save instance to use
    """

    print("storage")
    print("--")

def showCharacter(save, id):
    """
    Display the properties of a character in a save and allow the user to choose
    one to interact with.
    save: the save instance to use
    id: the character's id
    """

    print("character %i" % id)
    print("--")

def showInventory(save, id):
    """
    Display the items in a character's inventory and allow the user to choose
    one to interact with.
    save: the save instance to use
    id: the character's id
    """

    print("character %i's inventory" % id)
    print("--")

def showItem(save, loc, slot):
    """
    Display the properties of an item in an inventory and allow the user to
    choose one to interact with.
    save: the save instance to use
    loc: the id of the character containing the inventory, or -1 for storage
    slot: the slot the item is in
    """

    print("item in slot %i in loc %i" % (slot, loc))
    print("--")

def main():
    saveDirectory = os.getenv("APPDATA") + "/../LocalLow/DefaultCompany/Roguelands"
    save = Save(saveDirectory + "/PlayerPrefs.txt")

    characterSelect(save)

if __name__ == "__main__":
    main()
