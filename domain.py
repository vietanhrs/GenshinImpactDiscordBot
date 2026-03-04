from datetime import datetime
from pytz import timezone

class Domain(object):
    def __init__(self):
        # ---------------------------------------------------------------------------
        # TALENT BOOKS  (0 = Mon/Thu, 1 = Tue/Fri, 2 = Wed/Sat)
        #
        # Mondstadt  : Freedom (0) / Resistance (1) / Ballad (2)
        # Liyue      : Prosperity (0) / Diligence (1) / Gold (2)
        # Inazuma    : Transience (0) / Elegance (1) / Light (2)
        # Sumeru     : Admonition (0) / Ingenuity (1) / Praxis (2)
        # Fontaine   : Equity (0) / Justice (1) / Order (2)
        # Natlan (Blazing Ruins)    : Contention (0) / Kindling (1) / Conflict (2)
        # Natlan (Lightless Capital): Moonlight (0) / Elysium (1) / Vagrancy (2)
        # ---------------------------------------------------------------------------
        self.talent = {
            0: {
                # Mondstadt – Cecilia Garden (Mon/Thu)
                "Freedom": (
                    "Aloy", "Amber", "Barbara", "Diona", "Klee", "Sucrose",
                    "Childe",
                    "Anemo Traveler", "Geo Traveler",
                ),
                # Liyue – Taishan Mansion (Mon/Thu)
                "Prosperity": (
                    "Gaming", "Keqing", "Ningguang", "Qiqi", "Shenhe",
                    "Xiao", "Yelan",
                ),
                # Inazuma – Violet Court (Mon/Thu)
                "Transience": (
                    "Yoimiya", "Kokomi", "Thoma", "Heizou", "Kirara",
                    "Electro Traveler",
                ),
                # Sumeru – Steeple of Ignorance (Mon/Thu)
                "Admonition": (
                    "Tighnari", "Cyno", "Candace", "Faruzan",
                    "Dendro Traveler",
                ),
                # Fontaine – Pale Forgotten Glory (Mon/Thu)
                "Equity": (
                    "Lyney", "Neuvillette", "Navia", "Sigewinne",
                    "Hydro Traveler",
                ),
                # Natlan – Blazing Ruins (Mon/Thu)
                "Contention": (
                    "Skirk", "Iansan", "Mualani", "Mavuika",
                ),
                # Natlan – Lightless Capital (Mon/Thu)
                "Moonlight": (
                    "Lauma", "Columbina",
                ),
            },
            1: {
                # Mondstadt – Cecilia Garden (Tue/Fri)
                "Resistance": (
                    "Bennett", "Diluc", "Eula", "Jean", "Mona", "Noelle",
                    "Razor",
                ),
                # Liyue – Taishan Mansion (Tue/Fri)
                "Diligence": (
                    "Chongyun", "Ganyu", "Hu Tao", "Kazuha", "Xiangling",
                    "Yun Jin", "Yaoyao",
                ),
                # Inazuma – Violet Court (Tue/Fri)
                "Elegance": (
                    "Ayaka", "Kujou Sara", "Itto", "Ayato", "Kuki Shinobu",
                    "Electro Traveler",
                ),
                # Sumeru – Steeple of Ignorance (Tue/Fri)
                "Ingenuity": (
                    "Nahida", "Dori", "Layla", "Alhaitham", "Kaveh",
                    "Dendro Traveler",
                ),
                # Fontaine – Pale Forgotten Glory (Tue/Fri)
                "Justice": (
                    "Furina", "Clorinde", "Lynette", "Freminet", "Charlotte",
                ),
                # Natlan – Blazing Ruins (Tue/Fri)
                "Kindling": (
                    "Citlali", "Kinich", "Ororon", "Xilonen",
                ),
                # Natlan – Lightless Capital (Tue/Fri)
                "Elysium": (
                    "Nefer", "Aino", "Illuga",
                ),
            },
            2: {
                # Mondstadt – Cecilia Garden (Wed/Sat)
                "Ballad": (
                    "Albedo", "Fischl", "Kaeya", "Lisa", "Rosaria", "Venti",
                    "Mika", "Dahlia",
                ),
                # Liyue – Taishan Mansion (Wed/Sat)
                "Gold": (
                    "Beidou", "Xingqiu", "Zhongli", "Xinyan", "Yanfei",
                    "Baizhu", "Xianyun",
                ),
                # Inazuma – Violet Court (Wed/Sat)
                "Light": (
                    "Sayu", "Raiden Shogun", "Gorou", "Yae Miko", "Chiori",
                    "Sethos", "Emilie",
                ),
                # Sumeru – Steeple of Ignorance (Wed/Sat)
                "Praxis": (
                    "Collei", "Nilou", "Wanderer", "Dehya",
                ),
                # Fontaine – Pale Forgotten Glory (Wed/Sat)
                "Order": (
                    "Arlecchino", "Chevreuse", "Wriothesley",
                    "Hydro Traveler",
                ),
                # Natlan – Blazing Ruins (Wed/Sat)
                "Conflict": (
                    "Chasca", "Ifa", "Varesa", "Kachina",
                ),
                # Natlan – Lightless Capital (Wed/Sat)
                "Vagrancy": (
                    "Jahoda", "Flins",
                ),
            },
        }
        self.talent[3], self.talent[4], self.talent[5] = (
            self.talent[0], self.talent[1], self.talent[2]
        )

        # ---------------------------------------------------------------------------
        # WEAPON ASCENSION MATERIALS  (0 = Mon/Thu, 1 = Tue/Fri, 2 = Wed/Sat)
        #
        # Mondstadt – Cecilia Garden
        #   Decarabian (0) / Boreal Wolf (1) / Dandelion Gladiator (2)
        # Liyue – Hidden Palace of Lianshan Formula
        #   Guyun (0) / Mist Veiled Elixir (1) / Aerosiderite (2)
        # Inazuma – Court of Flowing Sand
        #   Distant Sea (0) / Narukami (1) / Mask (2)
        # Sumeru – Tower of Abject Pride
        #   Copper Talisman / Forest Dew (0) / Oasis Garden (1) / Scorching Might (2)
        # Fontaine – Echoes of the Deep Tides
        #   Ancient Chord (0) / Sacred Dewdrop (1) / Pristine Sea (2)
        # Natlan – Ancient Watchtower
        #   Blazing Sacrificial (0) / Delirious Decadence (1) / Night-Wind's Mystic (2)
        # ---------------------------------------------------------------------------
        self.weapon = {
            0: {
                # Mondstadt (Mon/Thu)
                "Decarabian": (
                    "Aquila Favonia", "Royal Longsword", "The Viridescent Hunt",
                    "Snow-Tombed Starsilver", "The Alley Flash", "Favonius Sword",
                    "The Stringless", "Favonius Codex", "Royal Grimoire", "The Bell",
                ),
                # Liyue (Mon/Thu)
                "Guyun": (
                    "Primordial Jade Winged-Spear", "Summit Shaper", "Lion's Roar",
                    "Blackcliff Longsword", "Crescent Pike", "Blackcliff Warbow",
                    "Lithic Blade", "Whiteblind", "Rust", "Blackcliff Agate",
                    "Solar Pearl",
                ),
                # Inazuma (Mon/Thu)
                "Distant Sea": (
                    "Mistsplitter Reforged", "Amenoma Kageuchi", "Hakushin Ring",
                    "Oathsworn Eye",
                ),
                # Sumeru (Mon/Thu)
                "Copper Talisman": (
                    "Key of Khaj-Nisut", "Light of Foliar Incision", "Ibis Piercer",
                    "Forest Regalia", "Dialogues of the Desert Sages",
                    "Sapwood Blade", "Xiphos' Moonlight",
                ),
                # Fontaine (Mon/Thu)
                "Ancient Chord": (
                    "The First Great Magic", "Verdict", "Absolution",
                    "Song of Stillness", "Range Gauge", "Prospector's Drill",
                    "Fleuve Cendre Ferryman", "Sword of Narzissenkreuz",
                ),
                # Natlan (Mon/Thu)
                "Blazing Sacrificial": (
                    "A Thousand Blazing Suns", "Fractured Halo", "Surf's Up",
                    "Earth Shaker", "Flute of Ezpitzal", "Sturdy Bone",
                    "Waveriding Whirl",
                ),
            },
            1: {
                # Mondstadt (Tue/Fri)
                "Boreal Wolf": (
                    "Skyward Harp", "Skyward Blade", "Skyward Pride",
                    "Skyward Atlas", "The Flute", "The Black Sword",
                    "Sacrificial Greatsword", "Sword of Descension", "Deathmatch",
                    "Wine and Song", "The Widsith", "Sacrificial Bow",
                    "Dragonspine Spear",
                ),
                # Liyue (Tue/Fri)
                "Mist Veiled Elixir": (
                    "The Unforged", "Eye of Perception", "Prototype Rancour",
                    "Prototype Crescent", "Dragon's Bane", "Blackcliff Pole",
                    "Royal Spear", "Blackcliff Slasher", "Prototype Amber",
                    "Rainslasher",
                ),
                # Inazuma (Tue/Fri)
                "Narukami": (
                    "Thundering Pulse", "Hamayumi", "Katsuragikiri Nagamasa",
                    "Kitain Cross Spear", "Akuoumaru",
                ),
                # Sumeru (Tue/Fri)
                "Oasis Garden": (
                    "A Thousand Floating Dreams", "Staff of the Scarlet Sands",
                    "Fruit of Fulfillment", "Wandering Evenstar", "Talking Stick",
                    "Moonpiercer", "Reliquary of Truth",
                ),
                # Fontaine (Tue/Fri)
                "Sacred Dewdrop": (
                    "Silvershower Heartstrings", "Tome of the Eternal Flow",
                    "Splendor of Tranquil Waters", "Flowing Purity",
                    "Finale of the Deep", "The Dockhand's Assistant",
                    "Symphonist of Scents",
                ),
                # Natlan (Tue/Fri)
                "Delirious Decadence": (
                    "Fang of the Mountain King", "Starcaller's Watch",
                    "Vivid Notions", "Calamity of Eshu", "Flame-Forged Insight",
                    "Footprint of the Rainbow", "Mountain-Bracing Bolt",
                    "Ring of Yaxche",
                ),
            },
            2: {
                # Mondstadt (Wed/Sat)
                "Dandelion Gladiator": (
                    "Wolf's Gravestone", "Lost Prayer to the Sacred Winds",
                    "Skyward Spine", "Amos' Bow", "Sacrificial Sword",
                    "Favonius Lance", "Festering Desire", "Frostbearer",
                    "Alley Hunter", "Favonius Warbow", "Royal Bow",
                    "Sacrificial Fragments", "Favonius Greatsword",
                    "Royal Greatsword",
                ),
                # Liyue (Wed/Sat)
                "Aerosiderite": (
                    "Memory of Dust", "Vortex Vanquisher", "Iron Sting",
                    "Serpent Spine", "Lithic Spear", "Prototype Starglitter",
                    "Compound Bow", "Mappa Mare", "Prototype Archaic",
                ),
                # Inazuma (Wed/Sat)
                "Mask": (
                    "Engulfing Lightning", "The Catch", "Haran Geppaku Futsu",
                    "Makoto's Dawn",
                ),
                # Sumeru (Wed/Sat)
                "Scorching Might": (
                    "Hunter's Path", "Tulaytullah's Remembrance",
                    "Beacon of the Reed Sea", "King's Squire", "End of the Line",
                    "Scion of the Blazing Sun", "Makhaira Aquamarine",
                ),
                # Fontaine (Wed/Sat)
                "Pristine Sea": (
                    "Cashflow Supervision", "Lumidouce Elegy", "Tidal Shadow",
                    "Portable Power Saw", "Ultimate Overlord's Mega Magic Sword",
                    "Rightful Reward", "Ballad of the Fjords",
                ),
                # Natlan (Wed/Sat)
                "Night-Wind's Mystic": (
                    "Astral Vulture's Crimson Plumage", "Azurelight",
                    "Crimson Moon's Semblance", "Peak Patrol Song",
                    "Ash-Graven Drinking Horn", "Chain Breaker",
                    "Flower-Wreathed Feathers", "Fruitful Hook",
                    "Rainbow Serpent's Bow",
                ),
            },
        }
        self.weapon[3], self.weapon[4], self.weapon[5] = (
            self.weapon[0], self.weapon[1], self.weapon[2]
        )

    def get_output(self, type, tz=None):
        weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day = datetime.now(timezone(tz)).weekday() if tz else datetime.now().weekday()
        if day == 6:
            return ["Traveler, it is the weekend! In Sunday you can farm anything!"]
        else:
            messages = ["Today is " + weekDays[day] + " Traveler, you can farm these resource:"]
            if type in ["talent", "book", "all"]:
                for key, value in self.talent[day].items():
                    messages.append("**" + key + "** book: " + ", ".join(value))
            if type in ["weapon", "all"]:
                for key, value in self.weapon[day].items():
                    messages.append("**" + key + "** material: " + ", ".join(value))
            return messages
