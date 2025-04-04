from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import filedialog

def run_chrome_scraper():
    """Führt den Selenium Scraper aus."""
    print("Was möchtest du suchen?")
    userSearch = input()
    googleSearch = userSearch.replace(" ", "+")

    CHROMEDRIVER_PATH = "C:\\chromedriver-win64\\chromedriver.exe"

    service = Service(CHROMEDRIVER_PATH)
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    search_url = f"https://www.google.com/search?q={googleSearch}&oq={googleSearch}"
    driver.get(search_url)

    time.sleep(2)
    page_html = driver.page_source
    soup = BeautifulSoup(page_html, 'html.parser')

    allDataContainer = soup.find("div", {"class": "dURPMd"})
    allData = allDataContainer.find_all("div", {"class": "Ww4FFb"}) if allDataContainer else []

    print(f"{len(allData)} Ergebnisse gefunden....")

    l = []
    for item in allData:
        obj = {
            "title": item.find("h3").text if item.find("h3") else None,
            "link": item.find("a")["href"] if item.find("a") else None,
            "description": item.find("div", {"class": "VwiC3b"}).text if item.find("div", {"class": "VwiC3b"}) else None,
            "search": userSearch
        }
        l.append(obj)

    driver.quit()

    root = tk.Tk()
    root.withdraw()
    root.lift()
    root.attributes('-topmost', True)

    print("Wähle einen Speicherort für die CSV-Datei")
    userPath = filedialog.askdirectory(title="Wähle einen Speicherort")

    while not userPath:
        print("Speicherort wurde nicht ausgewählt. Programm wird beendet.")
        userPath = filedialog.askdirectory(title="Wähle einen Speicherort")

    root.destroy()

    userSearch = userSearch.replace(" ", "_").replace('"', "").replace("'", "")
    fullPath = f"{userPath}/search.csv"

    df = pd.DataFrame(l)
    if not df.empty:
        df.to_csv(fullPath, index=False, encoding="utf-8-sig")
        print(f"Datei wurde erfolgreich gespeichert unter: {fullPath}")
    else:
        print("Keine Daten gefunden. Datei wurde nicht erstellt.")
