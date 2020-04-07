from bs4 import BeautifulSoup
from selenium import webdriver
import json
import requests
import csv
import pandas
from bs_table_extractor import Extractor

BASE_URL = "https://www.fortuneindia.com/fortune-500/company-list/reliance-industries?year=2019"
YEARS = [2019]
COLUMNS = ["rank", "company", "url", "year", "revenue", "net_operating_income",
           "profit", "assets", "net_worth",
           "employee_cost"]


class Company:
    def __init__(self, name, rank, url):
        self.name = name
        self.rank = rank
        self.url = url
        self.values = []

    def __repr__(self):
        return self.name + " " + self.rank

    def get_info_table(self):
        year = 2019
        self.values = [self.rank, self.name, self.url, year]
        company_url = f"{self.url}?year={year}"
        soup = BeautifulSoup(make_query(company_url), features="lxml")
        t = Extractor(soup.find("table"))
        self.values = self.values + [x[1] for x in t.parse().return_list()][
                                    1:]


def make_query(url):
    """
    Makes a get request.
    :param url: URL.
    :return: HTML
    """
    response = requests.get(url=url)
    html = None
    if response.status_code == 200:
        html = response.text
    return html


def parse_csv():
    """
    CSV file
    :return:
    """
    # with open("result.csv") as f:
    #     data = f.read()
    #     data = data.replace(", ", "|").replace(',', '')
    #     print(data)
    # with open("out.csv", 'w') as f:
    #     f.write(data)
    df = pandas.read_csv("out.csv", "|")
    print(df.to_string())
    df.to_csv("out.csv", index=False)


def parse_query(html):
    """
    Parses html from the JSON return to Company object
    :return: companies list
    """
    soup = BeautifulSoup(str(html), features="lxml")
    list_element = soup.findAll("li")
    companies = []
    if list_element:
        for company in list_element:
            if company.find("span", {"class": "sl-num"}):
                name_str = str(company.text).strip().replace('\n', '')
                rank, name = name_str.split(" ", 1)
                url = str(company.find("a")["href"]).split('?')[
                    0] if company.find("a") else None
                companies.append(Company(name=name, rank=rank, url=url))
    return companies


if __name__ == '__main__':
    parse_csv()
    # html = make_query(BASE_URL)
    # companies = parse_query(html)
    # master_data = []
    # with open("result.csv", "a", newline='') as f:
    #     for company in companies:
    #         company.get_info_table()
    #         print(company.values)
    #         master_data.append(company.values)
    # print(master_data)
    # df = pandas.DataFrame.from_records(master_data)
    # print(df.to_string())
    # df.to_csv("result.csv", index=False)
