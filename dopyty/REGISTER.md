# Register dopytov siete Forge

**Owner:** WS-011 (dokumenty a registre siete) · **Verzia:** 1.0 · **Status:** Aktívny · **Dátum:** 2026-09-10
**Audience:** public-ready — verejný register; obsah je L1/L2 podľa D-2026-5, kontrola L3 vykonaná.
**Pravidlo, ktoré tento register vykonáva:** `dopyt-v-sieti.md` §3 (čo register eviduje, ako dopyt vzniká,
kto mení stav) a §4 (životný cyklus a expirácia).
**Rozhodnutia:** **D-2026-21** (register dopytov je nosná vec), **D-2026-22** (dopyty žijú ako issues
vo `forge-platform`, register v tom istom repozitári), **D-2026-20** (jeden slovník druhov pre ponuku
aj dopyt), **D-2026-19** (ochrana údajov zastúpeného), **D-2026-6** / **D-2026-14** (Forge nesprostredkúva
a neručí) — `registry/decisions.md`.
**Licencia:** text pravidiel v tomto súbore je pod **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)** —
© 2026 Amunet s.r.o.; **názov „Forge", sieť uzlov, register uzlov a register dopytov nie sú predmetom
licencie** (D-2026-14, bod 2).

> **Kanonický zdroj tohto súboru je `project-forge` → `20-ecosystem/network/register-dopytov.md`.**
> Verejnú adresu mu dáva **nasadená kópia** `forge-platform/dopyty/REGISTER.md` (sync O-30a, princíp
> **D-2026-15**). Kópia je **bitovo zhodná** s kanonickým súborom. **Vo `forge-platform` sa register
> needituje** — zmena vykonaná tam sa pri najbližšom behu syncu stratí. Návrh na opravu záznamu podaj
> ako komentár v issue dopytu alebo ako issue v repozitári platformy.

---

## 1. Čo tento register je

Register dopytov je **verejný zoznam toho, čo uzly siete potrebujú** — jeden riadok na dopyt. Je to
**nosná vec** celého mechanizmu dopytu (**D-2026-21**): nosič, ktorým dopyt do registra príde, je
vymeniteľný, register je to, čo tu bude o tri roky.

**Register je zámerne krátky.** Plné znenie dopytu (pole „čo presne") žije na **adrese záznamu**, nie tu —
presne ako pri uzloch, kde register drží len adresu profilu. Register nesmie byť druhou kópiou obsahu,
ktorá sa rozíde s originálom.

**Register nie je ponuka, súťaž ani objednávka.** Zápis dopytu nikoho k ničomu nezaväzuje a prevzatie
dopytu nie je objednávka (`dopyt-v-sieti.md` §4.4 a §7).

## 2. Register

*(Stav k 2026-09-10: v sieti zatiaľ **nie je zapísaný žiadny dopyt**. Prvý dopyt dostane ID `DOP-001`.)*

| ID | Uzol | Druh | Adresa záznamu | Stav | Kto ho vzal | Zápis | Posledná zmena | Expirácia |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — |

**Význam stĺpcov** (`dopyt-v-sieti.md` §3.1):

- **ID** — `DOP-XXX`, prideľuje sieť pri zápise; pri obnovení dopytu sa **nemení**.
- **Uzol** — `NODE-XXX` toho, kto dopyt podal. **Kontakt sa tu neopakuje** — je v profile uzla.
- **Druh** — jedna hodnota zo slovníka `druhy-kapacit.md` (`stroj`, `materiál`, `podklad`, `priestor`,
  `doprava`, `ruky`, `znalosť`, `spôsobilosť`, `financovanie`, `dosah`, alebo `iné` s podtypom).
- **Adresa záznamu** — verejná adresa, na ktorej dopyt v plnom znení žije (dnes odkaz na issue).
- **Stav** — `otvorený` · `vzatý` · `splnený` · `zrušený` · `expirovaný`.
- **Kto ho vzal** — `NODE-XXX`; vypĺňa sa až v stave `vzatý`.
- **Dátumy** — zápis · posledná zmena stavu · **expirácia** podľa `dopyt-v-sieti.md` §4.2.

## 3. Kde dopyty žijú a kto register vedie

**Dopyty žijú ako issues v repozitári `forge-platform`** (**D-2026-22**, rozhodnutie riaditeľa k O-39):
uzol podá dopyt cez šablónu **`.github/ISSUE_TEMPLATE/dopyt.yml`**, issue nesie štítok **`dopyt`** a stavový
štítok **`dopyt:<stav>`**. Adresa issue je adresou záznamu.

| Čo | Kto to robí |
|---|---|
| podá dopyt | **uzol** — cez šablónu issue (prvá vstupná cesta); neskôr aj cez formulár platformy (druhá cesta, O-37) |
| pridelí ID a zapíše riadok | **prevádzkovateľ siete** — nový riadok so stavom `otvorený` a dátumom expirácie |
| mení **obsah** dopytu | **výhradne uzol, ktorý ho podal** (v issue) |
| mení **stav** v registri a na štítku | **prevádzkovateľ siete** — podľa toho, čo sa stalo na adrese záznamu |
| vyhodnocuje expiráciu | **pravidelná kontrola platformy**; expirácia je **údržba, nie nález** |

**Prakticky (do zavedenia formulára a strojovej kontroly):** riadok registra zapisuje **chat cez GitHub
konektor** do kanonického súboru v `project-forge` a nasadí ho sync — rovnakým postupom ako každú inú zmenu
dokumentu siete. Zápis dopytu je tým **oneskorený o merge a o beh syncu**; issue je verejne viditeľné hneď,
register o niekoľko minút neskôr. **Je to vedomá cena**, nie nedopatrenie — a je predmetom otvorenej
otázky **O-40** (či sa na register dopytov rozšíri výnimka P-011, teda zápis priamo do `main` bez PR).

## 4. Ako sa pozná nesúlad medzi registrom a issue

Register a issue nesú tú istú informáciu na dvoch miestach, takže sa **môžu rozísť**. Pravidlo:

1. **Rozhoduje register.** Je to nosná vec (**D-2026-21**); stavový štítok na issue je pohodlný pohľad,
   nie zdroj pravdy. Pri rozpore sa opravuje **štítok**, nie register.
2. **Nesúlad je nález, nie chyba uzla.** Kontrolovateľné strojovo sú tri veci:
   - riadok registra, ktorého **adresa záznamu neexistuje** alebo vedie na zavreté issue bez stavu;
   - issue so štítkom `dopyt`, ktoré **nemá riadok v registri** (dopyt prišiel a nikto ho nezapísal);
   - **stavový štítok ≠ stav v riadku** registra.
3. **Uzatvorenie issue nie je stav.** Stav je v registri a v štítku — inak by sa dopyt po zavretí issue
   nedal prečítať strojovo.

*Strojová kontrola týchto troch vecí zatiaľ **nebeží** — je to zadanie pre platformu (obdoba dennej
kontroly registra uzlov). Do jej nasadenia ich kontroluje prevádzkovateľ pri každej zmene stavu.*

## 5. Ako sa register drží krátky

Register má **jeden riadok na dopyt** a plné znenie nechá na adrese záznamu — už tým rastie pomaly.
Napriek tomu platí to isté pravidlo ako pre ostatné registre (`CLAUDE.md`, „Registre a limit zápisu"):

- **Nič sa nemaže.** Expirovaný ani zrušený dopyt sa z histórie neodstraňuje — verejná a trvalá história
  dopytov je to jediné, čo v sieti bez hodnotenia a reputácie nesie informáciu o spoľahlivosti.
- **Keď súbor presiahne ~35 kB, uzavreté dopyty sa presunú do archívu podľa období** —
  `register-dopytov/ARCHIV-<obdobie>.md`, doslovná kópia riadkov, rad ID sa nemení. Do archívu idú len
  dopyty v stave `splnený`, `zrušený` alebo `expirovaný`; **otvorené a vzaté ostávajú tu vždy**.
- **Založenie archívu znamená aj nový cieľ v mapovaní syncu** (a teda dva behy) — patrí do tej istej
  zmeny ako presun riadkov.

*Orientačne: pri ~120 znakoch na riadok je prah 35 kB niekde okolo **250 dopytov**. Rozdelenie preto nie je
téma pre najbližšie mesiace — pravidlo je tu preto, aby sa naň nezabudlo, keď bude.*

## 6. Číselný rad

**Ďalšie voľné ID dopytu: `DOP-001`.**

## Change Log

| Dátum | Zmena |
|---|---|
| 2026-09-10 | **v1.0 — register založený (D-2026-22).** Prázdny, s hlavičkou a pravidlami; žiadny vymyslený dopyt. Kanonický zdroj v `project-forge`, verejná kópia `forge-platform/dopyty/REGISTER.md` cez sync. Zapísané: kto register vedie a kto čo mení (§3), pravidlo nesúladu medzi registrom a issue (§4, návrh relácie), pravidlo držania krátkosti a archívu podľa období (§5, návrh relácie), číselný rad. Otvorená otázka **O-40** — režim zápisu do registra (výnimka z P-011). Rozhodnutie riaditeľa 2026-09-08 (inbox podľa P-009, zadanie SESSION-0061) — WS-011, SESSION-0061 |
