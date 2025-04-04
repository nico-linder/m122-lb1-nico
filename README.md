
# Scraper-Projekt

Dieses Repository enthält zwei verschiedene Scraper, die Google-Suchergebnisse extrahieren und speichern.

## 1. **Selenium-basierter Scraper (Chrome Scraper)**

Dieser Scraper nutzt **Selenium** und **BeautifulSoup**, um Google-Suchergebnisse zu extrahieren und die Daten in einer CSV-Datei zu speichern.

### Funktionsweise:
- Der Benutzer gibt einen Suchbegriff ein.
- Der Scraper öffnet Google, führt die Suche aus und extrahiert Titel, Links und Beschreibungen der Ergebnisse.
- Die Ergebnisse werden in einer CSV-Datei gespeichert, die der Benutzer in einem Ordner seiner Wahl ablegen kann.

### Abhängigkeiten:
- `selenium`
- `beautifulsoup4`
- `pandas`
- `tkinter` (für den Dialog zum Dateispeichern)

## 2. **API-basierter Scraper (Scrapingdog API)**

Dieser Scraper verwendet die **Scrapingdog API**, um Google-Suchergebnisse zu extrahieren und die Daten in eine PostgreSQL-Datenbank zu speichern.

### Funktionsweise:
- Der Benutzer gibt einen Suchbegriff und seinen Scrapingdog API-Schlüssel ein.
- Der Scraper ruft die API auf und extrahiert Titel, Links und Beschreibungen der Ergebnisse.
- Die Ergebnisse werden in einer PostgreSQL-Datenbank gespeichert.

### Abhängigkeiten:
- `requests`
- `psycopg2`

### Datenbank:
- PostgreSQL-Datenbank mit einer Tabelle `search_results` (Spalten: `search`, `title`, `link`, `description`)

## Nutzung:

1. **Selenium-basierter Scraper**:
   - Stelle sicher, dass **ChromeDriver** und die notwendigen Python-Bibliotheken installiert sind.
   - Starte den Scraper und gib den gewünschten Suchbegriff ein.
   - Wähle einen Speicherort für die CSV-Datei.

2. **API-basierter Scraper**:
   - Installiere die erforderlichen Abhängigkeiten.
   - Gib deinen **Scrapingdog API-Schlüssel** ein.
   - Der Scraper speichert die Ergebnisse in der PostgreSQL-Datenbank.

