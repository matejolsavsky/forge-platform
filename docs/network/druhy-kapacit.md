# Slovník druhov kapacít siete Forge

**Owner:** WS-011 (dokumenty siete) · **Verzia:** 0.1 · **Status:** Draft · **Dátum:** 2026-09-07
**Audience:** public-ready — navrhnuté ako **verejný slovník** (obsah je L1/L2 podľa D-2026-5, kontrola L3 vykonaná).
*Zverejnený nasadenou kópiou vo `forge-platform/docs/network/` podľa **D-2026-15** — mapovanie syncu doplnené
2026-09-08 (SESSION-0060).*
**Rozhodnutia:** **D-2026-20** (kapacita má druh; ten istý slovník pre ponuku aj dopyt), **D-2026-16** (uzol nie
je ponuka), **D-2026-17** (sieť eviduje aj dopyt), **D-2026-18** (vstup do siete; zásada „staviame pre 100 uzlov
zajtra") — `registry/decisions.md`.
**Licencia:** text je pod **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)** — © 2026 Amunet s.r.o.;
**názov „Forge", sieť uzlov a register uzlov nie sú predmetom licencie** (D-2026-14, bod 2).
Terminológia: RFC-000 (Machine, Capability, Digital Asset).

---

## 1. Načo je tento slovník

**Uzol neprispieva do siete len strojom.** Stroj je jeden druh kapacity, ktorým sieť začína — nie jediný, ktorý
existuje. Uzol, ktorý ponúka dopravu, priestor, ruky, znalosť, podklad alebo dosah, má vyplniť profil úplne
a pravdivo bez toho, aby čokoľvek predstieral.

Druhý dôvod je pre sieť dôležitejší: **ponuka aj dopyt musia používať ten istý slovník.** Ak sa kapacita popíše
jedným slovníkom a dopyt druhým, sieť ich nikdy nespáruje — a párovanie dopytu na kapacitu je celý zmysel siete
(**D-2026-17**). Preto je tento slovník jeden pre obe strany a mení sa pre obe naraz.

**Čo je kapacita:** to, čo uzol vie dať sieti k dispozícii. Kapacita **nie je ponuka** — uzol môže mať kapacitu
a nič neponúkať (**D-2026-16**); či a kedy ju použije, hovorí stav dostupnosti v jeho profile.

## 2. Ako je slovník postavený

- **Druh je riadený slovník** — desať hodnôt v §3 plus technická hodnota `iné` (§6). Druh je to, na čom sa
  ponuka a dopyt strojovo stretnú.
- **Podtyp je voľný text** — vlastnými slovami uzla („dielňa", „SLA tlačiareň", „účtovníctvo"). Podtyp sa
  nekontroluje a nezoznamuje; je pre človeka, ktorý číta výsledok po tom, čo stroj zúžil výber podľa druhu.
- **Slovník je plochý.** Dvojúrovňový slovník (uzavretý zoznam podtypov ku každému druhu) sme zvážili
  a zamietli: pri sto uzloch by každý nový nástroj znamenal rozhodnutie („je rezačka podtyp, alebo nový druh?"),
  zoznam by zastarával rýchlejšie, než by sa stíhal verzovať, a párovanie by sa tým nezlepšilo — dopyt aj tak
  hľadá najprv druh. Riadime teda desať hodnôt, nie stovky.
- **Zoznam nie je uzavretý** — pravidlo rozšírenia je v §6.

## 3. Druhy kapacít

Každý druh má: názov · strojový kľúč · definíciu jednou vetou · príklady · polia špecifické pre druh ·
poznámku, ako sa druh správa na strane dopytu.

### 3.1 stroj

| | |
|---|---|
| **Kľúč** | `stroj` |
| **Definícia** | Zariadenie, ktoré na požiadanie vyrobí, opracuje alebo zmeria vec. |
| **Príklady** | 3D tlačiareň, fréza, laser, šijací stroj, pec, brúska, dron, merací prístroj, drvič na recykláciu |
| **Polia druhu** | typ alebo technológia · počet · **materiály** (napr. PLA, PETG, živica, drevo) · **pracovný objem** (max. rozmery v mm, obmedzenia geometrie) · orientačná dostupná kapacita (hod./týždeň alebo ks/týždeň) |
| **Na strane dopytu** | Najčastejší dopyt siete: „potrebujem vyrobiť / opracovať X." Páruje sa spravidla spolu s `materiál`. Dopyt na stroj vidí **každý uzol so strojom bez ohľadu na stav dostupnosti** — práve to mu dáva možnosť voľby stať sa výrobným uzlom (D-2026-17). |

*Polia „materiály" a „pracovný objem" boli do v0.2 samostatnými sekciami profilu 3.3 a 3.4. Od štandardu v0.3 sú
poľami tejto položky — patria stroju, nie profilu. Uzol s tlačiarňou a šijacím strojom ich inak nevie popísať.*

### 3.2 materiál

| | |
|---|---|
| **Kľúč** | `materiál` |
| **Definícia** | Hmota, ktorá sa pri práci spotrebuje. |
| **Príklady** | zásoba filamentu, živica, drevo, odrezky kovu, textília, farby, spojovací materiál |
| **Polia druhu** | čo · koľko (orientačne) · stav (nový / zvyšky) · či je viazaný na miesto (treba si poň prísť) |
| **Na strane dopytu** | „Potrebujem 2 kg PLA." Sprevádza dopyt na `stroj`, ale existuje aj sám — a keďže materiál sa spotrebuje, dopyt naň je jednorazový, nie opakovaný. |

### 3.3 podklad (digitálny podklad — model a dokumentácia)

| | |
|---|---|
| **Kľúč** | `podklad` |
| **Definícia** | Hotový digitálny súbor alebo dokumentácia, ktorú vie použiť niekto iný bez toho, aby ju znovu vytvoril. |
| **Príklady** | knižnica modelov na tlač, výkres, návod, šablóna, kalibračný profil, metodika hodiny |
| **Polia druhu** | čo · licencia alebo podmienky použitia · kde je dostupný (adresa) |
| **Na strane dopytu** | „Potrebujem model / návod na X." Jediný druh, ktorý sa dá uspokojiť **kópiou** — nikomu neubudne čas ani hmota, takže jeden podklad uspokojí ľubovoľný počet dopytov. Preto sa nesleduje rozsah, ale licencia. |

*Prečo samostatný druh a nie „znalosť": znalosť je schopnosť človeka, ktorú treba zakaždým znovu použiť; podklad
je vec, ktorá už existuje. Rozdiel je presne ten, ktorý RFC-000 drží medzi **Digital Asset** a prácou — a je aj
ekonomický: znalosť sa míňa časom, podklad nie.*

### 3.4 priestor

| | |
|---|---|
| **Kľúč** | `priestor` |
| **Definícia** | Miesto, ktoré uzol poskytne na prácu, stretnutie alebo uloženie. |
| **Príklady** | dielňa, učebňa, sklad, miestnosť na stretnutie, kút s pracovným stolom |
| **Polia druhu** | typ (dielňa / učebňa / sklad / iné) · veľkosť alebo kapacita (osoby, m², palety) · vybavenie · kedy je dostupný · poloha (obec alebo kraj) |
| **Na strane dopytu** | „Potrebujem miesto na …" — na prácu, na stretnutie alebo na uloženie. **Skladovanie je podtyp priestoru**, nie samostatný druh (§5). |

### 3.5 doprava

| | |
|---|---|
| **Kľúč** | `doprava` |
| **Definícia** | Presun vecí alebo ľudí z jedného miesta na druhé. |
| **Príklady** | auto, dodávka, odberné miesto, pravidelný rozvoz, cesta, ktorú uzol aj tak robí |
| **Polia druhu** | čo prevezie (objem, hmotnosť) · dosah (kraj alebo trasa) · pravidelnosť (jednorazovo / pravidelne, kedy) |
| **Na strane dopytu** | „Potrebujem dostať X z A do B do …" Dopyt na dopravu takmer vždy visí na inom dopyte — bez nej sa vzdialené uzly nespoja. |

### 3.6 ruky a čas

| | |
|---|---|
| **Kľúč** | `ruky` |
| **Definícia** | Pracovný čas, ktorý po krátkom zaučení zvládne ktokoľvek. |
| **Príklady** | montáž, brúsenie, maľovanie, balenie, trieda, ktorá zvládne dávku |
| **Polia druhu** | koľko ľudí · koľko hodín týždenne · kde (u seba / na mieste dopytu) |
| **Na strane dopytu** | „Potrebujem 200 kusov zbrúsiť do piatku." Dopyt na ruky je jediný, kde je **jedno, kto ho vezme** — preto sa dá deliť medzi viac uzlov. |

### 3.7 znalosť

| | |
|---|---|
| **Kľúč** | `znalosť` |
| **Definícia** | Schopnosť, ktorú nemožno nahradiť zaučením — patrí konkrétnemu človeku alebo tímu. |
| **Príklady** | návrh a CAD, právo, účtovníctvo, granty, bezpečnosť, preklad a lokalizácia, školenie a mentoring |
| **Polia druhu** | oblasť · forma (poradenstvo / vypracovanie / školenie) · orientačný rozsah (hod./mesiac) |
| **Na strane dopytu** | „Potrebujem navrhnúť …", „potrebujem niekoho, kto to naučí …" Dopyt na znalosť smeruje na **konkrétny uzol**, nie na ktorýkoľvek — preto sa nedelí a nedá sa nahradiť dvomi inými. |

*Hranica voči „ruky a čas": ak sa práca dá po desiatich minútach vysvetľovania odovzdať komukoľvek inému, je to
`ruky`; ak nie, je to `znalosť`. **Mentoring a školenie sú forma znalosti, nie samostatný druh** (§5).*

### 3.8 právna spôsobilosť

| | |
|---|---|
| **Kľúč** | `spôsobilosť` |
| **Definícia** | Subjekt, ktorý smie a vie konať navonok — podpísať, fakturovať, prijať grant alebo vydať potvrdenie. |
| **Príklady** | s.r.o., živnosť, občianske združenie, škola, obec, akreditovaný subjekt |
| **Polia druhu** | čo vie (podpis zmluvy · faktúra · prijatie grantu · vydanie potvrdenia) · pôsobnosť (SK / CZ / EÚ) |
| **Na strane dopytu** | „Potrebujem subjekt, ktorý prijme grant / vystaví faktúru / potvrdí …" Nemá rozsah v hodinách ani kusoch — buď subjekt danú vec smie, alebo nesmie. |

### 3.9 financovanie

| | |
|---|---|
| **Kľúč** | `financovanie` |
| **Definícia** | Prostriedky, ktoré uzol vie dať alebo dopredu vyložiť. |
| **Príklady** | sponzor, darca, predfinancovanie grantovej platby, spolufinancovanie nákupu materiálu |
| **Polia druhu** | forma (dar · predfinancovanie · spolufinancovanie) · na čo je viazané · obdobie |
| **Na strane dopytu** | „Potrebujem preplatiť materiál", „potrebujem prekryť tri mesiace do vyplatenia grantu." |

> **Hranica (D-2026-6, D-2026-14, podmienky účasti §7):** sieť eviduje **len to, že kapacita existuje** —
> nikdy sumy, podmienky ani prevody, a nesprostredkúva platby. Je to to isté pravidlo ako pri cenníku
> v profile: **štruktúra, nie hodnoty.** Peniaze medzi uzlami sú vecou dvoch uzlov, nie siete.

### 3.10 dosah

| | |
|---|---|
| **Kľúč** | `dosah` |
| **Definícia** | Prístup k ľuďom — k tým, čo dopyt prinesú, alebo k tým, čo výsledok prevezmú. |
| **Príklady** | sieť škôl, komunita, obecný spravodaj, klub, predajňa alebo e-shop, ktorý vec ponúkne ďalej |
| **Polia druhu** | koho zasahuje · orientačná veľkosť · forma (osobne / newsletter / predajné miesto) |
| **Na strane dopytu** | „Potrebujem to niekomu ponúknuť / niekde predať / osloviť školy v kraji." **Odbyt a predaj sú forma dosahu**, nie samostatný druh (§5) — obe znamenajú prístup k druhej strane. |

## 4. Overenie na reálnych prípadoch

Otázka pri každom prípade: **padne beze zvyšku do niektorého druhu?**

| Prípad | Druhy kapacít | Zvyšok |
|---|---|---|
| **NODE-001 (Jawra)** — 3D tlač, vlastná entita riaditeľa, stav `neprijíma` | `stroj` (tlačiarne, materiály, pracovný objem) · `materiál` (filament) · `spôsobilosť` (entita vie fakturovať) | žiadny |
| **NODE-002** — domáci uzol vedený zákonným zástupcom, nič neponúka | **žiadna** → pevná hodnota `bez kapacity` | žiadny — a práve tento prípad ukazuje, že zoznam musí pripúšťať **nulu kapacít** |
| **Škola bez tlačiarne** | `priestor` (učebňa, dielňa) · `ruky` (trieda) · `spôsobilosť` (podpíše, prijme grant) · `dosah` (rodičia, sieť škôl) · niekedy `znalosť` (učiteľ) | žiadny; elektrina a prevádzka sú náklad priestoru, nie samostatná kapacita |
| **Človek, ktorý vie len navrhovať** | `znalosť` — a nič iné | žiadny |
| **Obec s dielňou** | `priestor` · `spôsobilosť` · `dosah` | žiadny |
| **Niekto, kto má len dodávku** | `doprava` — a nič iné | žiadny |
| **Darca materiálu** | `materiál` — a nič iné | žiadny |
| **Občianske združenie, ktoré vie prijať grant** | `spôsobilosť`; ak aj vykladá peniaze dopredu, aj `financovanie` | žiadny |
| *(doplnené reláciou)* **Autor knižnice modelov** — zverejňuje hotové modely a návody, nič iné | `podklad` — a nič iné | žiadny |
| *(doplnené reláciou)* **Sponzor, ktorý preplatí materiál** — dá peniaze, nič iné | `financovanie` — a nič iné | žiadny; nie je to `materiál` (peniaze nie sú hmota) ani `spôsobilosť` (nič nepodpisuje) |

**Test odlíšenia** (existuje aspoň jeden reálny uzol, ktorý má tento druh a **žiadny iný**?) prešli všetky
druhy: `stroj` (človek s tlačiarňou) · `materiál` (darca) · `podklad` (autor knižnice) · `priestor` (majiteľ
prázdnej dielne) · `doprava` (majiteľ dodávky) · `ruky` (dobrovoľníci, ktorí prídu na miesto) ·
`znalosť` (návrhár) · `spôsobilosť` (združenie, ktoré len prijme grant) · `financovanie` (sponzor) ·
`dosah` (človek so sieťou škôl a ničím iným).

## 5. Čo sme zvážili a nezaradili

Kandidáti zo zadania a výsledok testu odlíšenia. **Nezaradený neznamená nezachytený** — každý má miesto,
kde v slovníku žije.

| Kandidát | Rozhodnutie | Prečo |
|---|---|---|
| energia a prevádzkové náklady | **nie** — atribút | Neexistuje uzol, ktorý ponúka energiu a nič iné. Elektrina je náklad stroja alebo priestoru; keď je to príspevok v peniazoch, je to `financovanie`. |
| dáta a modely (knižnica modelov, dokumentácia) | **áno — nový druh `podklad`** | Test odlíšenia prešiel (autor knižnice) a je to jediná kapacita, ktorá sa uspokojí kópiou. RFC-000 drží Digital Asset oddelene — slovník to má držať tiež. |
| softvér a výpočet | **nie** — podtyp | Uzol, ktorý ponúka výpočet a nič iné, je v tejto sieti hypotetický. Keď stroj počíta (render, simulácia), je to `stroj` s digitálnym výstupom; keď počíta človek, je to `znalosť`. |
| certifikácia, meranie a kontrola kvality | **nie** — rozpadá sa na dva existujúce druhy | *Meranie* je `stroj` (merací prístroj) plus `znalosť` (kto výsledok prečíta). *Potvrdenie, ktoré niekto uzná*, je `spôsobilosť` — je to tá istá inštitucionálna schopnosť ako podpis zmluvy alebo prijatie grantu. |
| skladovanie a logistika oproti doprave | **nie** — podtyp | Sklad je `priestor` (miesto sa obsadí a vráti), presun je `doprava`, koordinácia je `znalosť`. Rieši to zároveň otázku „materiál vs. skladovanie": materiál je hmota (spotrebuje sa), sklad je miesto. |
| financovanie a predfinancovanie | **áno — nový druh `financovanie`** | Test odlíšenia prešiel (sponzor). Nie je to `spôsobilosť` — subjekt smie prijať grant aj bez peňazí, a človek s peniazmi nemusí nič podpisovať. Bez tohto druhu by peniaze prenikali do `materiál` a `spôsobilosť` a slovník by prestal byť pravdivý. |
| odbyt a predaj | **nie** — forma dosahu | Predajňa, ktorá vec ponúkne ďalej, dáva prístup k druhej strane rovnako ako komunita, ktorá prinesie dopyt. Zaradením sa spresnila definícia `dosah`. |
| recyklácia a odpad | **nie** — rozpadá sa | Drvič a extrudér sú `stroj`; výsledná drť je `materiál`. Samotný „odpad" bez stroja aj bez použiteľnosti nie je kapacita. |
| mentoring a školenie oproti znalosti | **nie** — forma znalosti | Uzol, ktorý mentoruje a pritom nemá znalosť, neexistuje. Mentoring je použitie znalosti, nie samostatná kapacita. |
| jazyk a lokalizácia | **nie** — oblasť znalosti | Preklad je schopnosť konkrétneho človeka; patrí do poľa „oblasť" druhu `znalosť`. |

**Zlúčenia, ktoré sme naopak nespravili:** `ruky` a `znalosť` ostávajú oddelené (rozhoduje nahraditeľnosť —
§3.7), `materiál` a `priestor` ostávajú oddelené (hmota vs. miesto), `spôsobilosť` a `financovanie` ostávajú
oddelené (postavenie vs. peniaze).

**Výsledok: desať druhov.** Osem zo zadania obstálo v teste odlíšenia nezmenených; pribudli dva (`podklad`,
`financovanie`); desať kandidátov sa zaradilo ako podtyp, pole alebo forma existujúceho druhu. Osem nebolo
hotové číslo a desať ním tiež nie je — pravidlo rozšírenia je v §6.

## 6. Rozšíriteľnosť a neznámy druh

**Hodnota `iné`.** Ak kapacita nepadne do žiadneho druhu, uzol uvedie druh `iné` a **povinne podtyp vlastnými
slovami**. `iné` nie je druh — je to poistka, aby uzol nikdy nemusel klamať ani mlčať o tom, čo má.

**Ako pribudne nový druh:**

1. **Navrhne ho ktokoľvek** — uzol, prevádzkovateľ siete alebo relácia — rovnakou cestou ako žiadosť o zápis
   (issue v repozitári platformy alebo e-mail; podmienky účasti §5). Návrh uvedie **aspoň jeden reálny uzol,
   ktorý daný druh má a žiadny iný** (test odlíšenia z §4) a ako sa druh správa na strane dopytu.
2. **Rozhoduje riaditeľ**, tak ako o každom pravidle siete. Rozhodnutie sa zapíše (FDS-005) a slovník dostane
   novú verziu; štandard profilu a dokument dopytu sa na slovník odvolávajú, takže sa menia **naraz s ním**.
3. **Nazbierané hodnoty `iné`** sú vstupom tohto konania — sú to skutočné kapacity, ktoré slovník ešte nemá.
   Prevádzkovateľ ich prezerá pri pravidelnej kontrole registra.
4. **Do rozhodnutia** uzol používa `iné` a jeho profil je v súlade so štandardom.

**Čo robí validátor s neznámym druhom: informatívny nález, nikdy pád.**

| | |
|---|---|
| Známy druh | bez nálezu |
| `iné` bez podtypu | nález ako pri inej chýbajúcej povinnej hodnote |
| **Neznámy druh** (hodnota mimo slovníka) | **informatívny nález** — vypíše sa, ale **profil ostáva v súlade** a návratový kód sa nemení |

**Prečo nesmie padnúť:**

- **Profil je dokument uzla na adrese, ktorú sieť neriadi.** Ak by neznámy druh znamenal nesúlad, uzol
  validovaný zelene by v deň, keď sa slovník posunie, zčervenal za niečo, čo sám nespravil.
- **Denná kontrola registra by sa stala nečitateľnou.** Pri sto uzloch stačí jedna nová hodnota u desiatich
  z nich, aby sa červené hlásenie prestalo čítať — a vtedy prestane fungovať aj na skutočné chyby.
- **Slovník bude vždy zaostávať za skutočnosťou.** Pri sto uzloch to platí dvojnásobne. Štandard, ktorý trestá
  skutočnosť, ľudia obídu — napíšu `stroj` tam, kde stroj nie je, a sieť si tým pokazí presne to, kvôli čomu
  slovník vznikol.
- **Neznámy druh je vstup, nie chyba.** Je to najlacnejší zdroj informácie o tom, čo do slovníka chýba
  (bod 3 vyššie).

Nesúlad so štandardom je **nález, nie sankcia** (podmienky účasti §3) — pri neznámom druhu to platí dvojnásobne.

## 7. Vzťah k ostatným dokumentom siete

- **Štandard profilu uzla** (`standard-profil-uzla.md`, v0.3): sekcia 3.2 profilu je zoznam kapacít; každá
  položka má druh z tohto slovníka. Kľúče druhov sú kvôli samostatnosti štandardu zopakované aj v ňom;
  definície, príklady a polia sú len tu.
- **Dopyt** (`dopyt-v-sieti.md`, v1.0): dopyt uvádza **druh z tohto slovníka**, rozsah, termín a miesto.
  Toto je to miesto, kde sa jeden slovník pre obe strany vypláca — párovanie je porovnanie druhu.
  *(Dokument dopytu zatiaľ nie je v tomto priečinku — verejnú adresu dostane spolu s rozhodnutím o tom,
  kde žije register dopytov.)*
- **Podmienky účasti uzla** (v0.3): za pravdivosť údajov o kapacitách ručí uzol; sieť ich neoveruje.

## 8. Hranica zverejnenia

Slovník je verejný dokument siete — **neobsahuje nič z L3 obsahu Forge** (D-2026-5): žiadne odkazy na formálne
jadro, víziu, etapy vývoja ani interné dokumenty. Odkaz na `registry/decisions.md` je L2, rovnako ako
v ostatných dokumentoch siete.

## Change Log

| Dátum | Zmena |
|---|---|
| 2026-09-07 | Prvá verzia (v0.1) — desať druhov kapacít (`stroj`, `materiál`, `podklad`, `priestor`, `doprava`, `ruky`, `znalosť`, `spôsobilosť`, `financovanie`, `dosah`) plus hodnota `iné`; plochý slovník s voľným podtypom; overenie na desiatich reálnych prípadoch a test odlíšenia; desať zvážených a nezaradených kandidátov s odôvodnením; pravidlo rozšírenia a správanie validátora pri neznámom druhu (informatívny nález, nikdy pád). Rozhodnutie riaditeľa 2026-09-07 (inbox podľa P-009, zadanie SESSION-0058) → **D-2026-20** — WS-011, SESSION-0058 |
| 2026-09-08 | **Slovník dostal verejnú adresu** — doplnený do mapovania syncu, nasadzuje sa do `forge-platform/docs/network/` ako ostatné dokumenty siete (**D-2026-15**); poznámka „zatiaľ bez verejnej adresy" v hlavičke tým odpadla. §7 — odkaz na dokument dopytu zosúladený s jeho platnou podobou (`navrh-dopyt-v-sieti.md` → **`dopyt-v-sieti.md` v1.0**, D-2026-21). **Obsah slovníka, druhy ani pravidlá sa nemenia — verzia ostáva v0.1.** Zadanie riaditeľa 2026-09-08 (inbox podľa P-009, zadanie SESSION-0060, body 2 a 4) — WS-011, SESSION-0060 |
