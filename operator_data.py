import requests
from bs4 import BeautifulSoup

def skill_search(operator_name: str, skill: int):
    r = requests.get(f"https://gamepress.gg/arknights/operator/{operator_name.lower()}")
    soup = BeautifulSoup(r.content, 'lxml')
    skill_info = soup.find("div", id=f"skill-tab-{skill}")
    if skill_info is None:
        return "This data is invalid at the moment"
    skill_name = skill_info.find("div", class_="h3-custom").text.strip()
    skill_point = skill_info.find("div", class_="sp-cell")
    text = f"__**{skill_name}**__\n"
    for i in range(1, 11):
        sp_cost = skill_point.find("div", class_="sp-cost").select_one(f'[class*="skill-upgrade-tab-{i}"]').text.strip()
        initial = skill_point.find("div", class_="initial-sp").select_one(f'[class*="skill-upgrade-tab-{i}"]').text.strip()
        text += f"Skill Point: {sp_cost}\u2000\u2000\u2000\u2000\u2000Initial SP: {initial}\n"
    return text
    
