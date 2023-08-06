import requests
from bs4 import BeautifulSoup
import random


def operator_list():
    r = requests.get("https://gamepress.gg/arknights/tools/interactive-operator-list#tags=null##cn##stats")
    soup = BeautifulSoup(r.content, 'html5lib')
    operators = soup.find_all("a", class_="operator-title-actual")
    return [operator.text for operator in operators]

database = []

def get_field(start_index, end_index, text, sp_cost_path, initial_path, duration_path, skill_description_path):
    for i in range(start_index, end_index):
        try:
            sp_cost = sp_cost_path.select_one(f'[class*="skill-upgrade-tab-{i}"]').text.strip()
            initial = initial_path.select_one(f'[class*="skill-upgrade-tab-{i}"]').text.strip()
            duration = duration_path.select_one(f'[class*="effect-description skill-upgrade-tab-{i}"]').text.strip()
            skill_description = skill_description_path.select_one(f'[class^="effect-description skill-upgrade-tab-{i}"]').text.strip()
        except:
            break
        if i > 7:
            text += f"__Level 7 M{i-7}__\n**Skill Point: {sp_cost}**" + "\u2000"*5 + f"**Initial SP: {initial}**" + "\u2000"*5 + f"**Duration: {duration}**" + "\n"
        else:
            text += f"__Level {i}__\n**Skill Point: {sp_cost}**" + "\u2000"*5 + f"**Initial SP: {initial}**" + "\u2000"*5 + f"**Duration: {duration}**" + "\n"
        text += skill_description + "\n\n"
    return text

def format_operator(name: str):
    return name.lower().strip().replace(' the', '').replace(' ', '-').replace('\'', '').replace('(', '').replace(')', '')


def skill_search(operator_name: str, skill: int):
    r = requests.get(f"https://gamepress.gg/arknights/operator/{format_operator(operator_name)}")
    soup = BeautifulSoup(r.content, 'lxml')
    skill_info = soup.find("div", id=f"skill-tab-{skill}")
    if skill_info is None:
        return "*This data is invalid at the moment*", None, None, None, None, None, None
    
    skill_name = skill_info.find("div", class_="h3-custom").text.strip()

    sp_charge_type = "SP Charge Type: " + skill_info.find("div", class_="sp-charge-type skill-effect-title").find("a").text.strip()
    skill_activation = "Skill Activation: " + skill_info.find("div", class_="skill-activation skill-effect-title").find("a").text.strip()
    text = f"__**{skill_name}**__\n" + f"*{sp_charge_type}*\n" +  f"*{skill_activation}*" + "\n\n"

    sp_cost_path = skill_info.find("div", class_="sp-cost")
    initial_path = skill_info.find("div", class_="initial-sp")
    duration_path = skill_info.find("div", class_="skill-duration skill-effect-title")
    skill_description_path = skill_info.find("div", class_="skill-description")

    text1 = ""
    text1 = get_field(1, 3, text1, sp_cost_path=sp_cost_path, initial_path=initial_path, duration_path=duration_path, skill_description_path=skill_description_path)
    text2 = ""
    text2 = get_field(3, 5, text2, sp_cost_path=sp_cost_path, initial_path=initial_path, duration_path=duration_path, skill_description_path=skill_description_path)
    text3 = ""
    text3 = get_field(5, 7, text3, sp_cost_path=sp_cost_path, initial_path=initial_path, duration_path=duration_path, skill_description_path=skill_description_path)
    text4 = ""
    text4 = get_field(7, 9, text4, sp_cost_path=sp_cost_path, initial_path=initial_path, duration_path=duration_path, skill_description_path=skill_description_path)
    text5 = ""
    text5 = get_field(9, 11, text5, sp_cost_path=sp_cost_path, initial_path=initial_path, duration_path=duration_path, skill_description_path=skill_description_path)

    # Get image
    image = random.choice(soup.select("div[id^=image-tab-]")).find("a")
    image_url = "https://gamepress.gg" + image.find("img").get("src")

    return text, text1, text2, text3, text4, text5, image_url
