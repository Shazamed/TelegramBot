import bs4
import requests
import re


def daily_infections():
    moh_URL = "https://www.moh.gov.sg/covid-19"
    textList = []
    res = requests.get(moh_URL)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.content, 'html.parser')
    daily_URL = soup.find_all('a', href=re.compile(r'https://www.moh.gov.sg/news-highlights/details/\d?\d-new-cases-of-locally-transmitted-covid-19-infection'))
    daily_URL = daily_URL[4]['href']
    res = requests.get(daily_URL)
    res.raise_for_status()
    regex = r'\d?\d New Cases? of Locally Transmitted COVID-19 Infection'
    headline = re.search(regex, res.text, re.IGNORECASE)
    headline = headline.group()

    textList.append(f'<b>{headline}\n</b>')
    textList.append(f"<a>{daily_URL}</a>")
    dailyFinal = ''.join(textList)
    return dailyFinal


def vaccinations_update():
    mohVaccinationURL = 'https://www.moh.gov.sg/covid-19/vaccination'
    vaccinationUpdateList = []
    res = requests.get(mohVaccinationURL)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.content, 'html.parser')
    elemsVacTable = soup.find_all('table')
    firstDose = elemsVacTable[0].text.strip().replace('Dose', 'Dose: ')
    fullDose = elemsVacTable[1].text.strip().replace('Regimen', 'Regimen: ')
    totalDose = elemsVacTable[2].text.strip().replace('Administered', 'Administered: ')
    vaccinationUpdateList.append(firstDose)
    vaccinationUpdateList.append(fullDose)
    vaccinationUpdateList.append(totalDose)
    vaccinationUpdateList.append(mohVaccinationURL)
    vacFinal = '\n'.join(vaccinationUpdateList)
    return vacFinal

def cluster_update():
    clusterURL = 'https://www.moh.gov.sg/covid-19/rsc'
    clusterStrList = []
    res = requests.get(clusterURL)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.content, 'html.parser')
    elems = soup.select('#ContentPlaceHolder_contentPlaceholder_TB03B381D008_Col00 > div:nth-child(9) > h3 > strong')
    latestCluster = elems[0].text.strip()
    clusterStrList.append(f'<b>{latestCluster}\n</b>')
    clusterStrList.append(f'<a>{clusterURL}</a>')
    clusterFinal = ''.join(clusterStrList)
    return clusterFinal
