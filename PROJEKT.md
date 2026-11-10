# Web Pub Podzemi – poznámky k projektu

Nový web pivnice Pub Podzemi (Údolní 222/5, Brno), náhrada za starý pubpodzemi.cz.
Běží na GitHub Pages: https://matyaskriz1.github.io/Pub-Podzemi-web/ (repozitář matyaskriz1/Pub-Podzemi-web, dříve moje-prvni-stranka)

## Soubory

| Soubor | Co v něm je |
|---|---|
| `index.html` | Hlavní stránka (úvod s fotkou, o nás, nabídka, galerie, otevírací doba, kontakt) |
| `jidelni-listek.html`, `napojovy-listek.html` | Lístky – **needitovat ručně**, generují se skriptem níže |
| `tools/generuj-listky.py` | Data lístků (názvy CZ/EN, ceny) a generátor obou stránek lístků |
| `style.css` | Veškerý vzhled |
| `main.js` | Přepínač CZ/EN, rezervační okno, okénko „právě otevřeno/zavřeno“, menu, posouvání |
| `img/` | Fotky a logo; `bar-1440.jpg`/`bar-2560.jpg` (úvod), `pivo.jpg` (výřez piva pro nápojový lístek), `burger.jpg`, `olivy.jpg`, `polevka.jpg` (z Instagramu) – vše zostřené AI Real-ESRGAN |

## Jak upravit lístky (ceny, položky)

1. Upravit seznamy `NAPOJE` / `JIDLA` v `tools/generuj-listky.py`
2. Spustit `python3 tools/generuj-listky.py`
3. Zvýšit verzi `?v=…` u `style.css` / `main.js`, pokud se měnil vzhled nebo skript (ve všech třech HTML i v generátoru)

## Angličtina

Český text je přímo v HTML, anglický v atributu `data-en="…"` (u atributů `data-en-alt`, `data-en-title` …).
Volba jazyka se pamatuje v prohlížeči.

## Vzhled (dohodnuté se zákazníkem)

- Světlý, vzdušný styl; všechny fotky obdélníkové/čtvercové (žádné oblouky).
- Barvy: omítka `#f5f4f0`, černá `#161616`, zlatá z loga `#b89f2e`, rezervační tlačítka jantarová `#c8891f` s bílým textem.
- Název „Pub Podzemi“ (úvod, logo v menu, patička) písmem **Fraunces**, jednobarevně, nikdy VELKÝMI PÍSMENY.
- Ostatní nadpisy: Big Shoulders Display; text: Instrument Sans.
- Úvod: fotka přes celou obrazovku, obsah zarovnaný na střed, velký text „Otevřeno denně od 15:00 do 01:00“.
- Aktuální stav otevřeno/zavřeno jen jako malé okénko vlevo dole (podle českého času, 15:00–01:00).
- Menu: vlevo Jídlo, Nápoje, Galerie, O nás, Kontakt; vpravo CZ | EN a Rezervace.
- Rezervace: okno s volbou Zavolat / Online rezervace (online systém zatím není – zobrazí omluvu).
- Web se po otevření vždy zobrazí od úvodu (nesjíždí dolů).
- Horní lišta (záhlaví) je větší: výška `--nav-h` 86 px na počítači, 76 px na telefonu.

## Pořadí sekcí na hlavní stránce

1. Úvod (fotka přes celou obrazovku)
2. „Žádný sklep…“ – text + fotka `interier-2.jpg`
3. „Pivní speciály i drinky“ – kompaktní blok, 3 dlaždice v barvách značek (Pilsner Urquell zelená, Radegast červená, Kosmix tmavě modrá).
   Počítač: otočí se najetím myší na text. Telefon: dlaždice vedle sebe, text se ukáže v panelu pod nimi.
4. „Co si dáte?“ – jídelní a nápojový lístek vedle sebe (i na telefonu)
5. „Tradice pokračuje“ – tmavý blok
6. Galerie – velká fotka + 4 menší, pod tím řádek se 3 fotkami jídel
7. Otevírací doba + „Dobré vědět“ (jeden seznam) + ikonky plateb na střed (hotovost, bezkontaktně, Visa, Mastercard, Maestro, Apple Pay, Google Pay)
8. Kontakt + mapa (obdélník) + dlaždice Instagram/Facebook (**skryté** – viz níže)

## Otevřené nápady

- **Instagram a Facebook:** v `index.html` u `<div class="socials" hidden>` doplnit adresy profilů místo `INSTAGRAM_URL` a `FACEBOOK_URL` a smazat `hidden`. Adresy musí dodat zákazník.
- Další fotky z Instagramu do galerie – zákazník je stáhne a pošle (Instagram nejde stahovat z prostředí).
- Vlastní fotky piv na dlaždice (fotky značek z internetu nechtěl).
- Doplnit informace o pivovaru Kosmix (text na dlaždici vychází jen z lístku).

- Online rezervační systém (zatím jen telefon).
- Logo ve vyšším rozlišení (teď jen 54 × 100 px ze starého webu).
- Nová úvodní fotka přímo z pivnice by byla ostřejší než zvětšená AI.
- Případně sjednotit ostatní nadpisy na písmo Fraunces.
- Připojit doménu pubpodzemi.cz na GitHub Pages.
