from bs4 import BeautifulSoup
from selenium import webdriver
import json
import requests

BASE_URL = "https://www.fortuneindia.com/fortune-500/company-list/reliance-industries?year=2019"


class Company:
    def __init__(self, name, rank, url):
        self.name = name
        self.rank = rank
        self.url = url

    def __repr__(self):
        return self.name + " " + self.rank

    def get_info_table(self):



def parse_query(url):
    """
    Makes the get request and parses the JSON return
    :return: HTML
    """
    response = requests.get(url=url)
    html = None
    if response.status_code == 200:
        html = response.text

    soup = BeautifulSoup(html, features="lxml")
    list_element = soup.findAll("li")
    companies = []
    if list_element:
        for company in list_element:
            if company.find("span", {"class": "sl-num"}):
                name_str = str(company.text).strip().replace('\n', '')
                rank, name = name_str.split(" ", 1)
                url = str(company.find("a")["href"]).split('?')[0] if company.find("a") else None
                companies.append(Company(name=name, rank=rank, url=url))








if __name__ == '__main__':
    parse_query(BASE_URL)
