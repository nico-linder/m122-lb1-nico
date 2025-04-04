import requests
import psycopg2
import json

api_key = None

def get_api_key():
    global api_key
    if api_key is None:
        api_key = input("Gib deinen Scrapingdog API-Key ein: ").strip()
        if not api_key:
            print("API-Key darf nicht leer sein.")
            exit(1)
    return api_key

def save_to_db(search, title, link, description):
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        insert_query = """
            INSERT INTO search_results (search, title, link, description)
            VALUES (%s, %s, %s, %s);
        """
        cursor.execute(insert_query, (search, title, link, description))
        conn.commit()
        print(f"Gespeichert: {title}")
    except Exception as db_error:
        print("Fehler beim Zugriff auf die Datenbank:", db_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

def run_api_scraper():
    user_search = input("Was möchtest du suchen?: ").strip()
    key = get_api_key()

    url = "https://api.scrapingdog.com/google/"
    params = {
        "api_key": key,
        "query": user_search,
        "gl": "ch",
        "hl": "de"
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            try:
                data = response.json()
                print("API Antwort (JSON):", json.dumps(data, indent=2))

                # Ergebnisse aus "menu_items" speichern
                menu_items = data.get("menu_items", [])
                for item in menu_items:
                    title = item.get("title", "Kein Titel")
                    link = item.get("link", "Kein Link")
                    # Für menu_items gibt es meist keine Beschreibung – wir speichern hier einen leeren String
                    description = ""
                    save_to_db(user_search, title, link, description)

                # Ergebnisse aus "peopleAlsoAskedFor" speichern
                paa_items = data.get("peopleAlsoAskedFor", [])
                for item in paa_items:
                    # Hier verwenden wir "title" als Titel, "link" falls vorhanden, ansonsten den "question"
                    title = item.get("title", "Kein Titel")
                    link = item.get("link", "Kein Link")
                    # Als Beschreibung speichern wir den Antworttext oder "answers"
                    description = item.get("answers", "")
                    if not description:
                        description = item.get("question", "")
                    save_to_db(user_search, title, link, description)

            except json.JSONDecodeError:
                print("Fehler: Antwort konnte nicht als JSON decodiert werden.")
        else:
            print(f"Request fehlgeschlagen. Status Code: {response.status_code}")
    except requests.RequestException as e:
        print("Fehler bei der HTTP-Anfrage:", e)

if __name__ == "__main__":
    run_api_scraper()
