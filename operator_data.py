import requests
from bs4 import BeautifulSoup
import random


def operator_list():
    r = requests.get("https://gamepress.gg/arknights/tools/interactive-operator-list#tags=null##cn##stats")
    soup = BeautifulSoup(r.content, 'lxml')
    operators = soup.find_all("a", class_="operator-title-actual")
    return [operator.text for operator in operators]

database = []

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
