import requests
import pandas as pd
from bs4 import BeautifulSoup

uri = "https://reteinformaticalavoro.it/offerte-di-lavoro?cerca=&regione=&city=&page="

r = requests.get(uri+"1")
soup = BeautifulSoup(r.content)
skill_tags = soup.find_all('label', 'label-job-skill')
skills = []

count = 0

for tag in skill_tags:
    count += 1
    for skill in tag.text.lower().split(' '):

        if(skill != ''):
            skills.append(skill.strip())

series = pd.Series(skills)
df = pd.DataFrame(series)

print(df.describe())
print(series.unique())