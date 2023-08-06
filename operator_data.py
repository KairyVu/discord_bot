import requests
from bs4 import BeautifulSoup
import random

# Use for update database only
def operator_list():
    r = requests.get("https://gamepress.gg/arknights/tools/interactive-operator-list#tags=null##cn##stats")
    soup = BeautifulSoup(r.content, 'lxml')
    operators = soup.find_all("a", class_="operator-title-actual")
    return [operator.text for operator in operators]

database = ['Swire the Elegant Wit', 'Eyjafjalla the Hvít Aska', 'Typhon', 'Executor the Ex Foedere', 'Muelsyse',
            "Ho'olheyak", 'Silence the Paradigmatic', 'Ines', 'Kirin X Yato', 'Qiubai', 'Chongyue', 'Lin',
            'Reed the Flame Shadow', 'Vigil', 'Penance', 'Texas the Omertosa', 'Stainless', 'Młynar', 'Pozëmka',
            'Gavial the Invincible', 'Dorothy', 'Ebenholz', 'Lumen', 'Irene', 'Specter the Unchained', 'Horn',
            'Fiammetta', 'Goldenglow', 'Lee', 'Ling', 'Gnosis', 'Flametail', 'Nearl the Radiant Knight', 'Fartooth',
            'Saileach', 'Mizuki', "Ch'en the Holungday", 'Pallas', 'Carnelian', 'Skadi the Corrupting Heart',
            "Kal'tsit", 'Gladiia', 'Passenger', 'Ash', 'Dusk', 'Saga', 'Archetto', 'Mountain', 'Mudrock', 'Rosmontis',
            'Blemishine', 'Surtr', 'Eunectes', 'Thorns', 'Suzuran', 'Rosa (Poca)', 'Weedy', 'W', 'Phantom', 'Bagpipe',
            'Ceobe', 'Nian', 'Aak', 'Blaze', 'Mostima', 'Magallan', 'Hellagur', 'Schwarz', "Ch'en", 'Skadi',
            'SilverAsh', 'Saria', 'Hoshiguma', 'Nightingale', 'Shining', 'Angelina', 'Eyjafjalla', 'Ifrit', 'Siege',
            'Exusiai', 'Bryophyta', 'Poncirus', 'Valarqvin', 'Santalla', 'Spuria', 'Insider', 'Tulip', 'Melanite',
            'Cement', 'Morgan', 'Rathalos S Noir Corne', 'Wind Chimes', 'Firewhistle', 'Jieyun', 'Harmonie', 'Puzzle',
            'Qanipalaat', 'Lunacub', 'Paprika', 'Dagda', 'Highmore', 'Proviso', 'Cantabile', 'Minimalist',
            'Greyy the Lightningbearer', 'Astgenne', 'Hibiscus the Purifier', 'Czerny', 'Erato', 'Windflit', 'Rockrock',
            'Heidi', 'Kazemaru', 'Enforcer', 'Quercus', 'Kroos the Keen Glint', 'Blacknight', 'Shalem', 'Aurora', 'Kjera',
            'Nine-Colored Deer', 'Honeyberry', 'Wild Mane', 'Corroserum', 'Ashlock', 'Mulberry', 'Tequila', 'La Pluma',
            'Kirara', 'Bena', 'Akafuyu', 'Toddifons', 'Heavyrain', 'Frost', 'Blitz', 'Tachanka', 'Mr. Nothing',
            'Lava the Purgatory', 'Tuye', 'Iris', 'Robin', 'Kafka', 'Amiya (Guard)', 'Whisperain', 'Aosta', 'Whislash',
            'April', 'Mint', 'Touch', 'Pith', 'Stormeye', 'Sharp', 'Flint', 'Tomimi', 'Andreana', 'Chiave', 'Beeswax',
            'Scene', 'Ayerscarpe', 'Folinic', 'Leonhardt', 'Absinthe', 'Tsukinogi', 'Asbestos', 'Elysium', 'Shamare',
            'Sideroca', 'Sesa', 'Bibeak', 'Leizi', 'Hung', 'Snowsant', 'GreyThroat', 'Broca', 'Reed', 'Bison', 'Waai Fu',
            'Ceylon', 'Flamebringer', 'Breeze', 'Executor', 'Astesia', 'Glaucus', 'Swire', 'Grani', 'Nightmare', 'Savage',
            'FEater', 'Manticore', 'Sora', 'Istina', 'Pramanix', 'Cliffheart', 'Firewatch', 'Provence', 'Vulcan',
            'Croissant', 'Liskarm', 'Projekt Red', 'Nearl', 'Warfarin', 'Silence', 'Mayer', 'Skyfire', 'Amiya', 'Meteorite',
            'Platinum', 'Blue Poison', 'Specter', 'Lappland', 'Indra', 'Franka', 'Texas', 'Zima', 'Ptilopsis', 'Humus',
            'Quartz', 'Totter', 'Luo Xiaohei', 'Chestnut', 'Pudding', 'Roberta', 'Indigo', 'Beanstalk', 'Pinecone',
            'Bubble', 'Arene', 'Aciddrop', 'Jaye', 'Click', 'Podenco', 'Jackie', 'Cutter', 'Conviction', 'Utage',
            'Purestream', 'Ambriel', 'May', 'Ethan', 'Dur-nar', 'Vermeil', 'Myrtle', 'Sussurro', 'Greyy', 'Beehunter',
            'Shaw', 'Earthspirit', 'Deepcolor', 'Gummy', 'Cuora', 'Matterhorn', 'Perfumer', 'Gavial', 'Myrrh', 'Rope',
            'Gravel', 'Mousse', 'Estelle', 'Frostleaf', 'Matoimaru', 'Dobermann', 'Vigna', 'Scavenger', 'Courier', 'Shirayuki',
            'Meteor', 'Jessica', 'Gitano', 'Haze', 'Reserve Operator - Caster', 'Reserve Operator - Logistics',
            'Reserve Operator - Sniper', 'Reserve Operator - Melee', 'Spot', 'Popukar', 'Midnight', 'Catapult', 'Orchid',
            'Steward', 'Ansel', 'Hibiscus', 'Lava', 'Adnachiel', 'Kroos', 'Beagle', 'Cardigan', 'Melantha', 'Plume', 'Vanilla',
            'Fang', '12F', 'Durin', 'Rangers', 'Noir Corne', 'Yato', 'Friston-3', 'U-Official', 'Terra Research Commission',
            "'Justice Knight'", 'THRM-EX', 'Castle-3', 'Lancet-2']



def format_operator(name: str):
    return name.lower().strip().replace(' the', '').replace(' ', '-').replace('\'', '').replace('(', '').replace(')', '')


def skill_search(operator_name: str, skill: int):
    r = requests.get(f"https://gamepress.gg/arknights/operator/{format_operator(operator_name)}")
    soup = BeautifulSoup(r.content, 'lxml')
    skill_info = soup.find("div", id=f"skill-tab-{skill}")
    if skill_info is None:
        return "*This data is invalid at the moment*", None
    
    skill_name = skill_info.find("div", class_="h3-custom").text.strip()

    sp_charge_type = "SP Charge Type: " + skill_info.find("div", class_="sp-charge-type skill-effect-title").find("a").text.strip()
    skill_activation = "Skill Activation: " + skill_info.find("div", class_="skill-activation skill-effect-title").find("a").text.strip()
    text = f"__**{skill_name}**__\n" + f"*{sp_charge_type}*" + "\u2000"*5 +  f"*{skill_activation}*" + "\n\n"

    sp_cost_path = skill_info.find("div", class_="sp-cost")
    intial_path = skill_info.find("div", class_="initial-sp")
    duration_path = skill_info.find("div")

    for i in range(1, 8):
        try:
            sp_cost = sp_cost_path.select_one(f'[class*="skill-upgrade-tab-{i}"]').text.strip()
            initial = intial_path.select_one(f'[class*="skill-upgrade-tab-{i}"]').text.strip()
        except:
            break
        
        text += f"Level {i}\nSkill Point: {sp_cost}" + "\u2000"*5 + f"Initial SP: {initial}" + "\n\n"
    
    text2 = ""
    for i in range(8, 11):
        try:
            sp_cost = sp_cost_path.select_one(f'[class*="skill-upgrade-tab-{i}"]').text.strip()
            initial = intial_path.select_one(f'[class*="skill-upgrade-tab-{i}"]').text.strip()
        except:
            break
        
        text2 += f"Level 7 M{i-7}\nSkill Point: {sp_cost}" + "\u2000"*5 + f"Initial SP: {initial}" + "\n\n"

    # Get image
    image = random.choice(soup.select("div[id^=image-tab-]")).find("a")
    image_url = "https://gamepress.gg" + image.find("img").get("src")

    return text, text2 ,image_url
