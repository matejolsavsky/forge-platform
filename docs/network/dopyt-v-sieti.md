# Dopyt v sieti Forge

**Owner:** WS-011 (dokumenty siete) · **Verzia:** 1.1 · **Status:** Draft · **Dátum:** 2026-09-10
**Audience:** public-ready — pravidlo siete určené na zverejnenie spolu so štandardom profilu uzla
a slovníkom druhov kapacít; obsah je L1/L2 podľa D-2026-5, kontrola L3 vykonaná.
**Rozhodnutia:** **D-2026-21** (register dopytov je nosná vec; issue = prvá vstupná cesta, formulár = druhá;
vlastný dokument uzla sa nezavádza), **D-2026-22** (dopyty žijú ako issues vo `forge-platform`, register
v tom istom repozitári), **D-2026-17** (sieť eviduje aj dopyt), **D-2026-20** (kapacita má druh;
ten istý slovník pre ponuku aj dopyt), **D-2026-18** (dve rovnocenné cesty na verejnú adresu),
**D-2026-16** (uzol nie je ponuka), **D-2026-19** (uzol vedený zákonným zástupcom),
**D-2026-6** / **D-2026-14** (Forge nesprostredkúva a neručí) — `registry/decisions.md`.
**Licencia:** text je pod **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)** — © 2026 Amunet s.r.o.;
**názov „Forge", sieť uzlov, register uzlov a register dopytov nie sú predmetom licencie** (D-2026-14, bod 2).
Kód platformy je samostatne pod Apache-2.0 (repozitár `forge-platform`).
**Povaha dokumentu:** **pravidlo siete, nie zmluva.** Nezakladá záväzky ani nároky; popisuje, ako sieť eviduje
dopyt. Súvisiace dokumenty: `standard-profil-uzla.md` (čo uzol má), `druhy-kapacit.md` (akého druhu môže byť
kapacita a dopyt), `register-dopytov.md` (samotný register a pravidlá jeho vedenia),
`podmienky-ucasti-uzla.md` (čo znamená byť v registri siete).

---

## 1. Načo je dopyt

Sieť s jedným uzlom nemá čo demonštrovať — prínos nevzniká v uzle, ale **medzi uzlami**. Preto sieť okrem
toho, čo uzly majú (profil), eviduje aj to, **čo uzly potrebujú** (dopyt).

Cyklus, ktorý má byť vidieť bez vysvetľovania (**D-2026-17**):

> **dopyt → voľba → producent**

Uzol zapíše dopyt. Uzol, ktorý má kapacitu potrebného druhu, dopyt uvidí a **sám sa rozhodne**, či ho vezme —
a tým sa z uzla, ktorý „len je v sieti", stáva výrobný uzol. Forge nikoho nepriraďuje a nikoho neoslovuje;
**koordinuje, neriadi** — dáva rozhodnutiu podklad, samo nerozhoduje.

**Nosnou vecou je register dopytov** (**D-2026-21**) — miesto, kde sieť vedie, čo sa žiada, **v tom istom
slovníku druhov, v akom vedie kapacity** (D-2026-20). Register je to, čo tu bude o tri roky; **nosič, ktorým
dopyt do registra príde, je vymeniteľný** (§5).

## 2. Tvar dopytu

Dopyt je **záznam jednej potreby**. Má presne toto a nič viac:

| Pole | Povinné | Obsah |
|---|---|---|
| **ID dopytu** | áno | `DOP-XXX` — prideľuje sieť pri zápise do registra |
| **Kto ho podáva** | áno | ID uzla (`NODE-XXX`), ktorý dopyt zapísal. **Kontakt je v profile uzla a tu sa neopakuje** — dopyt je verejný a trvalý, kontakt má jedno miesto |
| **Druh kapacity** | áno | jedna hodnota zo slovníka `druhy-kapacit.md` (`stroj`, `materiál`, `podklad`, `priestor`, `doprava`, `ruky`, `znalosť`, `spôsobilosť`, `financovanie`, `dosah`, alebo `iné` s povinným podtypom) |
| **Čo presne** | áno | vlastnými slovami; pri druhu `stroj` aj materiál a rozmery, ak na nich záleží; voliteľne odkaz na `podklad` (model, výkres) |
| **Rozsah** | áno | koľko — kusov, hodín, kilogramov, ľudí, m². Ak sa rozsah nedá vyčísliť (typicky pri druhu `spôsobilosť`), uvedie sa `neurčuje sa` |
| **Termín** | áno | dátum, dokedy to má byť, alebo **`bez termínu`** |
| **Miesto** | áno | kraj alebo obec, alebo **`na diaľku`**, ak na mieste nezáleží |
| **Stav** | áno | `otvorený` · `vzatý` · `splnený` · `zrušený` · `expirovaný` (§4) |
| **Dátumy** | áno | dátum zápisu · dátum poslednej zmeny stavu · **dátum expirácie** (§4.2) |

**Ako sa ozve ten, kto dopyt vezme.** Uzol, ktorý dopyt berie, spraví dve veci, a to v tomto poradí:

1. **Vyhlási to pri dopyte** — verejne, na mieste, kde dopyt žije („beriem to", ID svojho uzla, dátum).
   Vlastník záznamu podľa toho prepne stav na **`vzatý`** a zapíše **ID preberajúceho uzla a dátum**.
2. **Ozve sa zapisovateľovi priamo** — kontaktom uvedeným v **profile zapisujúceho uzla**. Všetko ostatné
   (čo presne, za koľko, kedy, ako sa to odovzdá) **si dohodnú dva uzly medzi sebou mimo siete**.

Sieť do tejto dohody nevstupuje a nič z nej neeviduje. Verejné vyhlásenie „beriem to" má jediný účel: aby
ostatní vedeli, že sa tomu už niekto venuje, a nerobili tú istú robotu dvakrát.

**Čo v dopyte nikdy nie je:** cena a rozpočet · platobné a dodacie podmienky · zmluvné znenie · osobné údaje
(kontakt je v profile uzla; pri uzle vedenom zákonným zástupcom platí **D-2026-19** v plnom rozsahu) ·
hodnotenie iných uzlov.

Dopyt sa **číta človekom aj strojom** rovnako ako profil a **kontroluje sa tým istým mechanizmom** — tvar,
povinné polia, prípustné hodnoty stavu a druhu. **Neznámy druh nie je chyba** (`druhy-kapacit.md` §6):
vypíše sa, dopyt ostáva platný.

## 3. Register dopytov

**Register dopytov je nosná vec celého mechanizmu** (**D-2026-21**). Je to verejný zoznam — jeden riadok
na dopyt — a vedie ho prevádzkovateľ siete rovnako ako register uzlov.

**Kde register je:** `forge-platform/dopyty/REGISTER.md` (**D-2026-22**). Kanonický zdroj tohto súboru je
`register-dopytov.md` v repozitári `project-forge`; verejnú adresu mu dáva nasadená kópia (rovnaký princíp
ako pri dokumentoch siete — **D-2026-15**). Pravidlá vedenia registra — kto čo mení, ako sa pozná nesúlad
medzi registrom a issue a ako sa register drží krátky — sú v ňom samotnom.

### 3.1 Čo register eviduje

| Stĺpec | Obsah |
|---|---|
| ID dopytu | `DOP-XXX` |
| Uzol | `NODE-XXX` zapisovateľa |
| Druh | jedna hodnota zo slovníka |
| Adresa záznamu | verejná adresa, na ktorej dopyt v plnom znení žije |
| Stav | `otvorený` · `vzatý` · `splnený` · `zrušený` · `expirovaný` |
| Kto ho vzal | `NODE-XXX` — vypĺňa sa až v stave `vzatý` |
| Dátumy | zápis · posledná zmena · expirácia |

**Register je zámerne krátky.** Plné znenie dopytu (pole „čo presne") žije na adrese záznamu, nie v registri —
presne ako pri uzloch, kde register drží len adresu profilu. Dôvod je ten istý: **register má ostať čitateľný
aj pri stovkách záznamov** a nesmie sa stať druhou kópiou obsahu, ktorá sa rozíde s originálom.

### 3.2 Ako dopyt vzniká

1. Uzol podá dopyt jednou zo **vstupných ciest** (§5).
2. Prevádzkovateľ siete mu pridelí **ID** a zapíše riadok do registra so stavom `otvorený` a s dátumom expirácie
   podľa §4.2.
3. Od tej chvíle je dopyt viditeľný pre celú sieť.

**Zápis dopytu je bezplatný** a nezakladá žiadny poplatok — rovnako ako zápis uzla (podmienky účasti §5).
**Dopyt smie podať len uzol zapísaný v registri siete**; je to jediná podmienka a plynie z toho, že dopyt sa
na niekoho odkazuje — bez profilu by nebolo kam poslať kontakt a za pravdivosť by nemal kto ručiť.

### 3.3 Kto stav mení

**Vlastník záznamu** je ten, kto vlastní adresu, na ktorej dopyt žije — uzol, alebo platforma, ak dopyt vedie
v jeho mene (rovnaké dve cesty ako pri profile, **D-2026-18**). Stav v registri mení **prevádzkovateľ siete**
podľa toho, čo sa stalo na adrese záznamu; obsah dopytu mení **výhradne uzol, ktorý ho podal**.

## 4. Životný cyklus

### 4.1 Stavy

| Stav | Znamená | Kedy nastane |
|---|---|---|
| `otvorený` | dopyt platí a nikto ho nevzal | pri zápise; a vždy, keď sa dopyt vráti späť do hry |
| `vzatý` | uzol X verejne vyhlásil, že ho berie (zapíše sa **ID uzla a dátum**) | po vyhlásení podľa §2 |
| `splnený` | potreba je vybavená | oznámi **uzol, ktorý dopyt podal** |
| `zrušený` | dopyt sa ruší bez vybavenia — potreba pominula alebo sa vyriešila inak | oznámi uzol, ktorý dopyt podal |
| `expirovaný` | uplynula lehota a nikto ho nevybavil | automaticky podľa §4.2 |

**Dopyt je krátkodobý.** Profil uzla žije roky, dopyt žije týždne — a to je dôvod, prečo dopyt nie je sekciou
profilu ani samostatným dokumentom uzla (**D-2026-21**). Krátky život má dôsledok, ktorý treba brať vážne:
**register, ktorý sa nečistí, prestane byť pravdivý** — a neaktuálny dopyt je horší než žiadny, lebo uzol,
ktorý sa naň ozve, narazí na potrebu, ktorá už neexistuje.

### 4.2 Expirácia

| Prípad | Lehota |
|---|---|
| dopyt **s termínom** | expiruje **14 dní po termíne**, ak dovtedy nie je `splnený` ani `zrušený` |
| dopyt **bez termínu** | expiruje **60 dní** od zápisu alebo od poslednej zmeny stavu |
| dopyt v stave **`vzatý`** | expirácia sa **prepočíta na 60 dní od prevzatia** — dohoda dvoch uzlov trvá, kým trvá |

- **Expirovaný dopyt sa nemaže.** Ostáva v registri aj na svojej adrese; história dopytov je verejná a trvalá.
- **Uzol môže dopyt kedykoľvek obnoviť** — zmenou termínu sa dopyt vráti do stavu `otvorený` a lehota beží
  odznova. Obnovenie nie je nový dopyt, ID sa nemení.
- Expiráciu vyhodnocuje **pravidelná kontrola platformy** rovnako ako kontrolu registra uzlov; expirácia je
  **údržba, nie nález** — nikto nič neporušil.

### 4.3 Keď z prevzatia nič nebude

Dopyt sa vráti do stavu **`otvorený`** s dátumovanou poznámkou a s novou lehotou. Nič viac sa nedeje.

**Sieť nikoho nehodnotí a nesankcionuje** — nevedie hviezdičky, reputáciu ani čiernu listinu. Je to vedomá
voľba a má cenu: pri sto uzloch bude prevzatý a nedokončený dopyt bežná vec. Vystačíme si s tým, že **história
dopytov je verejná a trvalá** — kto neplní, je to na jeho zázname vidieť bez toho, aby to sieť čokoľvek
„známkovala". Hodnotenie je samostatný a ťažký mechanizmus s vlastnými rizikami; nezačíname s ním.

### 4.4 Čo sa nezapisuje nikdy

**Cena, dodanie, faktúra, záruka a prípadná zmluva sú vecou dvoch uzlov.** Forge nie je stranou, nič
nesprostredkúva a za nič neručí (podmienky účasti §4 a §7, **D-2026-6**, **D-2026-14**). Prevzatie dopytu
v sieti **nie je objednávka ani záväzok**.

## 5. Dve vstupné cesty

Dopyt sa podáva **rovnako ako profil** (**D-2026-18**): má dve rovnocenné cesty na verejnú adresu a **register
eviduje len adresu záznamu** — je mu jedno, ktorou cestou dopyt vznikol.

| Cesta | Ako to vyzerá | Stav |
|---|---|---|
| **1 — issue** | uzol vyplní **štruktúrované issue** vo verejnom repozitári siete `forge-platform` (šablóna „Dopyt v sieti Forge"); issue nesie štítok `dopyt` a stav nesie štítok `dopyt:<stav>` | **funguje ako prvá vstupná cesta** |
| **2 — formulár** | uzol vyplní **formulár platformy**; platforma z neho vytvorí a vedie záznam v mene uzla | **zatiaľ nie je k dispozícii** — pribudne s variantom A vstupu do siete (rozhodnutie o architektúre je otvorené) |

**Prvá cesta nie je dočasná barlička.** Ostáva v platnosti aj potom, čo pribudne druhá — kto vie a chce podať
dopyt cez issue, bude ho podávať cez issue aj o tri roky. **Dočasné je len to, že prvá cesta je zatiaľ jediná**,
a tým je bariérou pre toho, kto nemá účet u poskytovateľa repozitára; túto bariéru odstraňuje až druhá cesta.

**Uzatvorenie issue nie je stav.** Stav dopytu je v registri a v štítku — inak by sa dopyt po zavretí issue
nedal prečítať strojovo.

*Vlastný dokument dopytu u uzla (obdoba `PROFILE.md`) sa **nezavádza**: dokument u uzla sedí na veci, ktorá
žije roky, a dopyt žije týždne (**D-2026-21**).*

> **Uzavreté (2026-09-08, D-2026-22):** verejným miestom prvej vstupnej cesty je repozitár **`forge-platform`** —
> šablóna issue, štítky aj register dopytov sú v ňom. Riaditeľ rozhodol **s vedomím ceny**, že fronta zadaní
> Programátora a dopyty uzlov budú v jednom zozname issues; pri väčšom počte dopytov je **samostatný verejný
> repozitár siete pravdepodobný budúci krok** — presun je vtedy **prepis registra, nie migrácia údajov**, lebo
> register je krátky zoznam odkazov. Tento dokument je od miesta nezávislý: menila by sa adresa, nie pravidlo.

## 6. Párovanie

Párovanie je **porovnanie druhu** — presne kvôli tomu má ponuka aj dopyt jeden slovník (**D-2026-20**).

Uzol je **kandidát** na dopyt, ak:

1. má v profile kapacitu **toho istého druhu**, a
2. miesto sedí — kraj sa prekrýva, alebo dopyt hovorí `na diaľku`, a
3. dopyt je v stave `otvorený`.

Tri poznámky, na ktorých záleží viac než na samotnom pravidle:

- **Stav dostupnosti uzla kandidatúru neobmedzuje.** Dopyt vidí aj uzol v stave `neprijíma` — inak by cyklus
  „dopyt → voľba → producent" nemal ako začať. Práve uzol, ktorý dnes nič neponúka, je ten, ktorému má dopyt
  dať dôvod začať.
- **Sieť nikoho nevyberá.** Zoznam kandidátov je informácia, nie priradenie. **Kto dopyt vezme, rozhoduje
  sám**; kto dopyt zapísal, si vyberá, s kým sa dohodne.
- **Jeden dopyt = jeden druh.** Ak potreba vyžaduje viac druhov (výroba + doprava), zapíšu sa **viac dopytov** —
  každý s jedným druhom — a v poli „čo presne" sa odkážu na seba. Zložený dopyt by sa nedal spárovať ani
  prevziať po častiach.

## 7. Čo dopyt nie je

- **Nie je objednávka.** Zápis dopytu nikoho k ničomu nezaväzuje, ani zapisovateľa.
- **Nie je verejná súťaž.** Sieť neporovnáva ponuky a neurčuje víťaza.
- **Nie je inzerát na predaj.** Uzol, ktorý chce niečo ponúknuť, na to má profil (sekcie 3.5–3.7);
  uzol, ktorý si len niečo praje bez konkrétnej potreby, na to má sekciu 3.10 Záujem.

## 8. Ochrana údajov

Dopyt je **verejný a trvalý** rovnako ako profil. Preto:

- dopyt **neobsahuje osobné údaje** — ani zapisovateľa, ani tretích osôb; kontaktom je kontakt z profilu uzla;
- pri uzle vedenom zákonným zástupcom platí **D-2026-19** v plnom rozsahu (žiadne osobné údaje zastúpeného,
  kontaktom je zástupca);
- „čo presne" sa píše vecne — nie ako príbeh, v ktorom sa dá niekoho identifikovať.

## 9. Hranica zverejnenia

Tento dokument je verejné pravidlo siete — **neobsahuje nič z L3 obsahu Forge** (D-2026-5): žiadne odkazy
na formálne jadro, víziu, etapy vývoja ani interné dokumenty. Odkaz na `registry/decisions.md` je L2, rovnako
ako v ostatných dokumentoch siete.

## Change Log

| Dátum | Zmena |
|---|---|
| 2026-09-07 | Prvá verzia textu ako **návrh** (`navrh-dopyt-v-sieti.md` v0.1, Status: Draft — návrh, nie platný dokument siete): obsah záznamu dopytu, párovanie podľa druhu, životný cyklus a prevzatie, ochrana údajov, tri varianty nosiča ako podklad pre rozhodnutie **O-35**. Zadanie riaditeľa 2026-09-07 (inbox podľa P-009) — WS-011, SESSION-0058 |
| 2026-09-08 | **v1.0 — platný dokument siete (D-2026-21, O-35 uzavretá).** Riaditeľ rozhodol inak, než boli postavené varianty: **nosnou vecou je register dopytov**, nosič je vymeniteľný. Súbor premenovaný `navrh-dopyt-v-sieti.md` → **`dopyt-v-sieti.md`**, hlavička „NÁVRH" odstránená. Nové **§3 Register dopytov** (čo eviduje, ako dopyt vzniká, kto mení stav). **Stavy zosúladené s rozhodnutím riaditeľa:** `otvorený` · **`vzatý`** · **`splnený`** · `zrušený` · **`expirovaný`** (predtým `prevzatý`/`uzavretý`). Nová **§4.2 expirácia** — dopyt je krátkodobý: 14 dní po termíne, 60 dní bez termínu, prepočet pri prevzatí; expirovaný dopyt sa nemaže a dá sa obnoviť (pravidlo navrhla relácia). **§5 dve vstupné cesty** — issue je **prvá vstupná cesta, nie dočasná barlička**, formulár je druhá a zatiaľ nie je k dispozícii; **vlastný dokument uzla sa nezavádza**. **§2 doplnené o „ako sa ozve ten, kto dopyt vezme"** (verejné vyhlásenie + priamy kontakt z profilu). **§6 párovanie bez hodnotenia a reputácie** — návrh relácie riaditeľ prijal. Doplnená licencia CC BY 4.0, povaha „pravidlo siete, nie zmluva" a §9 hranica zverejnenia. **Kde issue fyzicky žije, dokument nerieši — otvorená otázka O-39.** Rozhodnutie riaditeľa 2026-09-08 (inbox podľa P-009, zadanie SESSION-0060) — WS-011, SESSION-0060 |
| 2026-09-10 | **v1.1 — O-39 uzavretá (D-2026-22): dopyty žijú vo `forge-platform`.** Doplnené konkrétne miesto tam, kde dokument dovtedy hovoril všeobecne: **§3 adresa registra** (`forge-platform/dopyty/REGISTER.md`, kanonický zdroj `register-dopytov.md` v `project-forge`) s odkazom na pravidlá jeho vedenia; **§5 prvá vstupná cesta** menuje repozitár, šablónu a štítky `dopyt` / `dopyt:<stav>`, pribudla veta **„uzatvorenie issue nie je stav"**; poznámka o otvorenej O-39 nahradená **uzavretým rozhodnutím** vrátane vedomej dočasnosti (samostatný verejný repozitár siete ako pravdepodobný budúci krok — presun je prepis registra, nie migrácia údajov). Do hlavičky doplnené **D-2026-22** a súvisiaci dokument `register-dopytov.md`. **Pravidlá dopytu sa nemenili** — tvar, stavy, expirácia, párovanie ani ochrana údajov nie sú dotknuté; zmena je adresa, nie pravidlo. Dokument je od tejto verzie **v mapovaní syncu** a má verejnú adresu (D-2026-15). Rozhodnutie riaditeľa 2026-09-08 (inbox podľa P-009, zadanie SESSION-0061) — WS-011, SESSION-0061 |
