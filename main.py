from scrapers.api_scraper import run_api_scraper
from scrapers.chrome_scraper import run_chrome_scraper

def again():
    while True:
        user_input = input("Möchtest du eine weitere Suche durchführen? (ja/nein): ").strip().lower()
        if user_input == "ja":
            return True
        elif user_input == "nein":
            return False
        else:
            print("Ungültige Eingabe. Bitte 'ja' oder 'nein' eingeben.")

def main():
    isRunning = True
    while isRunning:
        print("\nWähle eine Scraping-Methode:")
        print("1 - Scrapingdog API (schnell & ohne Browser)")
        print("2 - Selenium Web Scraping (langsam, aber ohne API)")
        print("3 - Beenden")

        choice = input("Deine Wahl: ").strip()
        if choice == "1":
            while True:
                run_api_scraper()
                if not again():
                 break
        elif choice == "2":
            while True:
                run_chrome_scraper()
                if not again():
                    break
        elif choice == "3":
            print("Programm wird beendet.")
            isRunning = False
        else:
            print("Ungültige Eingabe. Bitte eine gültige Option wählen.")

if __name__ == "__main__":
    main()
