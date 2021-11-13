#!/usr/bin/env python3
import re
import requests
from bs4 import BeautifulSoup

regex_PDF = re.compile(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*).pdf")

def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")

def fcfm_PDF():
    soup = get_soup(f"http://www.fcfm.uanl.mx/")
    resultado = open(f"pdfs_FCFM.txt", "w", encoding="UTF-8")

    archivos = soup.find_all('a')
    target = [archivo.get("href") for archivo in archivos]
    target_clean = []

    for valor in target:
            if valor != None:
                    target_clean.append(valor)
    filtrado_PDF = list(filter(regex_PDF.match, target_clean))
    
    for i in filtrado_PDF:
        resultado.write(f"{i}\n")

    print(f"{filtrado_PDF}\n")


if __name__ == "__main__":
    fcfm_PDF()
