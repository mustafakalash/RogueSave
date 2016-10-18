import datetime
import shutil
import os

"""The amount of slots inventory slot a character has, including equipment."""
INVENTORY_SLOTS = 45
"""The amount of storage slots a save has."""
STORAGE_SLOTS = 360
"""The amount of combat chip slots a character has, including the hot bar."""
COMBAT_CHIP_SLOTS = 38
"""The amount of quests a save can have."""
QUEST_SLOTS = 3
"""The maximum number of ship droids."""
SHIP_DROID_SLOTS = 6
"""The amount of storage slots for ship droids."""
SHIP_DROID_STORAGE_SLOTS = 9
"""The length of one dimension of the ship's square area."""
SHIP_SIZE = 64
"""The items and their IDs."""
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
    2524:"Ancient Golem Card",
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
"""The available races, sorted by ID."""
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
"""The available uniforms, sorted by ID."""
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
"""The available traits, sorted by ID."""
TRAITS = [
    "Vitality",
    "Strength",
    "Dexterity",
    "Tech",
    "Magic",
    "Faith"
]
"""The available classes, sorted by ID."""
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
"""The available augments, sorted by ID."""
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
"""The available allegiences, sorted by ID."""
ALLEGIANCES = [
    "Galatic Fleet",
    "Starlight Rebellion",
    "Church of Faust",
    "Gray Enigma",
    "Junkbelt Mercenaries",
    "Droidtech Enterprise"
]
"""The available mods, sorted by ID."""
MODS = [
    "Empty",
    "BonusVIT+",
    "BonusSTR+",
    "BonusDEX+",
    "BonusTEC+",
    "BonusMAG+",
    "BonusFTH+",
    "ProjectileRange+",
    "CritRate+",
    "CritDmg+",
    "HealthRegen+",
    "ManaRegen+",
    "StaminaRegen+",
    "MoveSpeed+",
    "DashSpeed+",
    "JumpHeight+",
    "OreHarvest+",
    "PlantHarvest+",
    "BugHarvest+",
    "MonsterDrops+",
    "ExpBoost+",
    "CreditBoost+",
    "ResistHeat+",
    "ResistFrost+",
    "ResistPoision+"
]
"""The available combat chips and their IDs."""
COMBAT_CHIPS = {
    0:"Empty",
    1:"Swiftness",
    2:"Vitality I",
    52:"Vitality II",
    102:"Vitality X",
    3:"Strength I",
    53:"Stength II",
    103:"Strength X",
    4:"Dexterity I",
    54:"Dexterity II",
    104:"Dexterity X",
    5:"Tech I",
    55:"Tech II",
    105:"Tech X",
    6:"Intelligence I",
    56:"Intelligence II",
    106:"Intelligence X",
    7:"Faith I",
    57:"Faith II",
    107:"Faith X",
    8:"Photon Blade",
    9:"Dancing Slash",
    10:"Triple Shot",
    11:"Atalanta's Eye",
    12:"Plasma Grenade",
    13:"Gadget Turret",
    14:"Blaze",
    15:"Shock",
    16:"Healing Ward",
    17:"Bubble",
    18:"Berserk",
    19:"Megaslash",
    20:"Hyperbeam",
    21:"Trickster",
    22:"Quadracopter",
    23:"Cluster Bomber",
    24:"Inferno",
    25:"Enhanced Mind",
    26:"Angelic Augur",
    27:"Prism",
    38:"Darkfire"
}
"""The monsters."""
MONSTERS = [
    "Error",
    "Shmoo",
    "Eyepod",
    "Dunebug",
    "Worm",
    "Wasp",
    "Urugorak",
    "Sluglord",
    "Slugmother",
    "Chamcham",
    "Rhinobug",
    "Hivemind",
    "Glibglob",
    "Slime",
    "Rock Spider",
    "Sploopy",
    "Rock Scarab",
    "Shroom",
    "Blue Shroom",
    "Shroom Bully",
    "Relicfish",
    "Ancient Guard",
    "Ancient Beast",
    "Roach",
    "Ancient Golem",
    "Squirm",
    "Plague Caster",
    "Glitterbug",
    "Plaguebeast",
    "Space Pirate",
    "Wicked",
    "Wisp",
    "Yeti",
    "Mammoth",
    "Wyvern",
    "Lava Blob",
    "Fire Slime",
    "Lava Dragon",
    "Tyrannog",
    "Beelzeblob",
    "Gruu",
    "Treant",
    "Willowwart",
    "Caius",
    "Moloch"
]

class Save:
    """
    Save data for one PlayerPrefs file.

    saveFilePath: the absolute path to the save file
    """

    def __init__(self, saveFilePath):
        #shutil.copy(saveFilePath, %s + " %s.bak"
        #   % (saveFilePath,
        #   datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")))
        with open(saveFilePath) as saveFile:
            saveFileContents = saveFile.read()
            saveFileContents = saveFileContents.replace(" ", "")
            self.saveContents = dict(item.split(":", 1)
                for item in saveFileContents.split(";"))
            for key in list(self.saveContents.keys()):
                self.saveContents[key] = self.saveContents[key].split(":")[0]

        self.characters = list()
        for key in list(self.saveContents.keys()):
            if "name" in key:
                charId = int(key[0])
                name = self.saveContents["%iname" % charId]
                level = int(self.saveContents["%ilevel" % charId])
                hp = int(self.saveContents["%ihp" % charId])
                mana = int(self.saveContents["%imana" % charId])
                race = int(self.saveContents["%irace" % charId])
                variant = int(self.saveContents["%ivariant" % charId])
                uniform = int(self.saveContents["%iuniform" % charId])
                trait0 = int(self.saveContents["%itrait0" % charId])
                trait1 = int(self.saveContents["%itrait1" % charId])
                lifetime = int(self.saveContents["%ilifetime" % charId])
                exp = int(self.saveContents["%iexp" % charId])
                augment = int(self.saveContents["%iaugment" % charId])
                traitClass = int(self.saveContents["%iclass" % charId])
                allegience = int(self.saveContents["%iallegiance" % charId])
                vitality = int(self.saveContents["%ipStat0" % charId])
                strength = int(self.saveContents["%ipStat1" % charId])
                dexterity = int(self.saveContents["%ipStat2" % charId])
                tech = int(self.saveContents["%ipStat3" % charId])
                magic = int(self.saveContents["%ipStat4" % charId])
                faith = int(self.saveContents["%ipStat5" % charId])

                inventory = list()
                for i in range(INVENTORY_SLOTS):
                    itemId = int(self.saveContents["%i%iid" % (charId, i)])
                    tier = int(self.saveContents["%i%itier" % (charId, i)])
                    quantity = int(self.saveContents["%i%iq" % (charId, i)])
                    exp = int(self.saveContents["%i%iexp" % (charId, i)])
                    mod0 = int(self.saveContents["%i%ia0" % (charId, i)])
                    mod1 = int(self.saveContents["%i%ia1" % (charId, i)])
                    mod2 = int(self.saveContents["%i%ia2" % (charId, i)])
                    modL0 = int(self.saveContents["%i%iaL0" % (charId, i)])
                    modL1 = int(self.saveContents["%i%iaL1" % (charId, i)])
                    modL2 = int(self.saveContents["%i%iaL2" % (charId, i)])
                    inventory.append(Item(itemId, tier, quantity, exp, mod0,
                        mod1, mod2, modL0, modL1, modL2))

                combatChips = list()
                for i in range(COMBAT_CHIP_SLOTS):
                    combatChips.append(int(self.saveContents["%icc%i" % (charId, i)]))

                self.characters.append(Character(charId, name, level, hp, mana,
                    race, variant, uniform, trait0, trait1, lifetime, exp,
                    augment, traitClass, allegience, vitality, strength,
                    dexterity, tech, magic, faith, inventory))

        self.storageLevel = int(self.saveContents["storageLevel"])
        self.storage = list()
        for i in range(STORAGE_SLOTS):
            itemId = int(self.saveContents["storage%iid" % i])
            tier = int(self.saveContents["storage%itier" % i])
            quantity = int(self.saveContents["storage%iq" % i])
            exp = int(self.saveContents["storage%iexp" % i])
            mod0 = int(self.saveContents["storage%ia0" % i])
            mod1 = int(self.saveContents["storage%ia1" % i])
            mod2 = int(self.saveContents["storage%ia2" % i])
            modL0 = int(self.saveContents["storage%iaL0" % i])
            modL1 = int(self.saveContents["storage%iaL1" % i])
            modL2 = int(self.saveContents["storage%iaL2" % i])
            self.storage.append(Item(itemId, tier, quantity, exp, mod0, mod1,
                mod2, modL0, modL1, modL2))

        self.shipDroids = list()
        for i in range(SHIP_DROID_SLOTS):
            self.shipDroids.append(int(self.saveContents["sd%i" % i]))
        self.shipDroidStorage = list()
        for i in range(SHIP_DROID_STORAGE_SLOTS):
            itemId = int(self.saveContents["gather%iid" % i])
            tier = int(self.saveContents["gather%itier" % i])
            quantity = int(self.saveContents["gather%iq" % i])
            exp = int(self.saveContents["gather%iexp" % i])
            mod0 = int(self.saveContents["gather%ia0" % i])
            mod1 = int(self.saveContents["gather%ia1" % i])
            mod2 = int(self.saveContents["gather%ia2" % i])
            modL0 = int(self.saveContents["gather%iaL0" % i])
            modL1 = int(self.saveContents["gather%iaL1" % i])
            modL2 = int(self.saveContents["gather%iaL2" % i])
            self.shipDroidStorage.append(Item(itemId, tier, quantity, exp, mod0,
            mod1, mod2, modL0, modL1, modL2))

        self.questsCompleted = self.saveContents["qCompleted"]
        self.quests = list()
        for i in range(QUEST_SLOTS):
            qType = int(self.saveContents["%iqType" % i])
            tier = int(self.saveContents["%iqTier" % i])
            level = int(self.saveContents["%iqChallenge" % i])
            thingId = int(self.saveContents["%iqThingID" % i])
            thingQ = int(self.saveContents["%iqNumberOf" % i])
            progress = int(self.saveContents["%iqNumberOf2" % i])
            rewardId = int(self.saveContents["%iqRewardID" % i])
            rewardQ = int(self.saveContents["%iqRewardQ" % i])
            self.quests.append(Quest(i, qType, tier, level, thingId, thingQ,
                progress, rewardId, rewardQ))

        self.shipWalls = list()
        self.shipBlocks = list()
        self.shipItems = list()
        for x in range(SHIP_SIZE):
            for y in range(SHIP_SIZE):
                self.shipWalls.append(
                    ShipPart(int(self.saveContents["wallx%iy%i" % (x, y)]), x, y))
                self.shipBlocks.append(
                    ShipPart(int(self.saveContents["gridx%iy%i" % (x, y)]), x, y))
                self.shipItems.append(
                    ShipPart(int(self.saveContents["gridSx%iy%i" % (x, y)]), x, y))

class Character:
    """
    A character and its inventory.

    id: the character's id
    name: the character's name
    level: the character's level
    hp: the character's hp
    mana: the character's mana
    race: the character's race
    variant: the character's race variant
    uniform: the character's uniform
    trait0: the character's first main stat
    trait1: the character's second main stat
    lifetime: the amount of time the character has been played
    exp: the exp the character has
    augment: the character's augment
    traitClass: the character's class, based on its traits
    allegience: the character's faction allegience
    vitality: the character's vitality stat
    strength: the character's strength stat
    dexterity: the character's dexterity stat
    tech: the charactter's tech stat
    magic: the character's magic stat
    faith: the character's faith stat
    inventory: a list containing the character's Items
    combatChips: a list containing the character's combat chips
    """

    def __init__(self, id, name, level, hp, mana, race, variant, uniform,
        trait0, trait1, lifetime, exp, augment, traitClass, allegience,
        vitality, strength, dexterity, tech, magic, faith, inventory):
        self.id = id
        self.name = name
        self.level = level
        self.hp = hp
        self.mana = mana
        self.race = race
        self.variant = variant
        self.uniform = uniform
        self.trait0 = trait0
        self.trait1 = trait1
        self.lifetime = lifetime
        self.exp = exp
        self.augment = augment
        self.traitClass = traitClass
        self.allegience = allegience
        self.vitality = vitality
        self.strength = strength
        self.dexterity = dexterity
        self.tech = tech
        self.magic = magic
        self.faith = faith
        self.inventory = inventory

class Item:
    """
    An item and its stats.

    id: the item's id
    tier: the items's tier
    quanitity: the item's quanitity
    exp: the item's experience
    mod0, mod1, mod2: the mods installed in the item
    modL0, modL1, modL2: the levels of the mods installed in the item
    """

    def __init__(self, id, tier, quantity, exp, mod0, mod1, mod2, modL0, modL1,
        modL2):
        self.id = id
        self.tier = tier
        self.quantity = quantity
        self.exp = exp
        self.mod0 = mod0
        self.mod1 = mod1
        self.mod2 = mod2
        self.modL0 = modL0
        self.modL1 = modL1
        self.modL2 = modL2

class Quest:
    """
    A quest and its information.

    id: the quest's id
    type: the quest's type
    tier: the quest's tier
    level: the quest's challenge level
    thingId: the id of the item or mob needed to complete the quest
    thingQ: the amount of items or kills needed to complete the quest
    progress: the amount of items or kills already completed
    rewardId: the id of the item given for completing the quest
    rewardQ: the amount of the item given for completing the quest
    """

    def __init__(self, id, type, tier, level, thingId, thingQ, progress,
    rewardId, rewardQ):
        self.id = id
        self.type = type
        self.tier = tier
        self.level = level
        self.thingId = thingId
        self.thingQ = thingQ
        self.progress = progress
        self.rewardId = rewardId
        self.rewardQ = rewardQ

class ShipPart:
    """
    An item, block, or background wall placed in the ship.

    id: the id of the part
    x: the x coordinate of the part
    y: the y coordinate of the part
    """

    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

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
