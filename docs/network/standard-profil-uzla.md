# Štandard profilu uzla siete Forge

**Owner:** WS-010 (od 2026-09-04 dokumenty siete udržiava WS-011) · **Verzia:** 0.3 · **Status:** Draft · **Dátum:** 2026-09-07
**Audience:** public-ready — navrhnuté ako **verejný štandard** (zverejnený nasadenou kópiou vo `forge-platform/docs/network/`);
obsah je L1/L2 podľa D-2026-5, kontrola L3 vykonaná.
**Rozhodnutia:** **D-2026-6** (Forge = bezplatná platforma; uzly, ktoré prijímajú zákazky, podnikajú komerčne ako samostatné
entity), **D-2026-7** (architektúra „kontrakt cez špecifikáciu"; NODE-001 prvý uzol), **D-2026-16** (uzol nie je ponuka —
povinnosti podľa stavu), **D-2026-18** (vstup do siete: uzol profil hostí sám alebo ho v jeho mene hostí platforma),
**D-2026-19** (uzol vedený zákonným zástupcom), **D-2026-20** (kapacita má druh; ten istý slovník pre ponuku aj dopyt) —
`registry/decisions.md`.
**Licencia:** text tohto štandardu je pod **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)** —
© 2026 Amunet s.r.o. Smie sa kopírovať, šíriť a upravovať aj komerčne pri uvedení zdroja; **názov „Forge",
sieť uzlov a register uzlov nie sú predmetom licencie** (D-2026-14, bod 2). Kód platformy je samostatne pod
Apache-2.0 (repozitár `forge-platform`).
Terminológia: RFC-000 (uzol ≈ Machine + Capability prevádzkované entitou; od v0.2 aj uzol bez stroja a bez ponuky,
od v0.3 aj uzol s kapacitou iného druhu než stroj).

---

## 1. Účel a princíp

Uzol siete Forge je **osoba alebo entita, ktorá je súčasťou siete**: má verejný profil podľa tohto štandardu
a je zapísaná v registri siete. **Uzol nie je ponuka.** Uzol nemusí nič ponúkať ani nič chcieť — aj obyčajný
človek s tlačiarňou (alebo bez nej), ktorý sa pridal, je uzol. Či a kedy sa stane **výrobným uzlom**, je jeho
voľba a vyjadruje ju stav dostupnosti (§3.9). Uzol, ktorý zákazky prijíma, **podniká komerčne vo vlastnom mene
a na vlastnú zodpovednosť**. Forge je bezplatná platforma — nemá podiel na tržbách uzla a jeho činnosť neprevádzkuje.

**Uzol neprispieva do siete len strojom.** To, čo uzol vie dať sieti k dispozícii, je **kapacita**, a každá
kapacita má **druh** (**D-2026-20**). Stroj je jeden druh kapacity, ktorým sieť začína — nie jediný, ktorý
existuje: doprava, priestor, ruky a čas, znalosť, materiál, digitálny podklad, právna spôsobilosť, financovanie
a dosah sú kapacity rovnako. Uzol, ktorý ponúka niektorú z nich, vyplní profil úplne a pravdivo bez toho, aby
čokoľvek predstieral. Zoznam druhov a ich definície sú v samostatnom dokumente siete
**`druhy-kapacit.md`** (slovník druhov kapacít).

Sieť okrem profilov (čo uzol má a vie) eviduje aj **dopyt** (čo uzol potrebuje): dopyt uvidí uzol, ktorý má
kapacitu daného druhu, a sám sa rozhodne, či ho vezme — tým sa stáva výrobným uzlom. **Dopyt používa ten istý
slovník druhov ako profil** — ak by ponuka a dopyt hovorili každý svojím slovníkom, sieť by ich nikdy nespárovala.
Tvar dopytu upraví samostatný dokument siete.

Vzťah Forge ↔ uzol je **kontrakt cez špecifikáciu**:

1. Forge definuje a verzuje tento štandard profilu uzla a slovník druhov kapacít.
2. Uzol vedie svoj profil na **verejnej adrese, ktorú si zvolí** (vlastný repozitár, web, statická stránka,
   úložisko) — **alebo ho v jeho mene hostí platforma** (§2). V oboch prípadoch **obsah profilu určuje uzol
   a ručí zaň**; komerčné detaily (cenníkové hodnoty, katalóg, prevádzkové postupy) ostávajú u uzla.
3. Forge vedie o uzle len **minimálny záznam** (§5) a na profil odkazuje. Komerčné údaje uzla sa do
   repozitára Forge nezapisujú a obsah Forge sa nekopíruje k uzlu.

**Profil uzla je jediné rozhranie** medzi uzlom a sieťou: čo nie je v profile, sieť o uzle nevie.

## 2. Ako uzol publikuje profil

- Profil je súbor **`PROFILE.md`** (jazyk podľa pôsobnosti uzla — SK/CZ/EN).
- Profil má **dve rovnocenné cesty na verejnú adresu**; register siete eviduje **len adresu profilu**,
  takže mu je jedno, ktorou cestou vznikol:
  - **Vlastné hostovanie:** uzol profil zverejní sám **kdekoľvek na verejnej adrese**, ktorú vie sieť
    prečítať (repozitár, web, statická stránka, úložisko). Sieť nepredpisuje žiadnu technológiu —
    repozitár ani účet u konkrétneho poskytovateľa **nie sú podmienkou**.
  - **Hostovanie platformou:** uzol dodá údaje (žiadosť alebo formulár platformy), platforma z nich vytvorí
    profil podľa tohto štandardu a **zverejní ho na svojej adrese v mene uzla**. Platforma profil **mení len
    na pokyn uzla** a na jeho žiadosť ho odstráni. *Kým platforma túto cestu neponúka automaticky, vykonáva
    ju prevádzkovateľ siete ručne na žiadosť uzla.*
- Profil má vlastnú verziu a change log (menený len uzlom, resp. na jeho pokyn).
- Hlavička profilu uvádza verziu tohto štandardu, podľa ktorej je napísaný (napr. `standard: v0.3`).
- Voliteľne môže uzol pridať strojovo čitateľnú podobu **`profile.yaml`** s rovnakými poľami;
  pri rozpore platí `PROFILE.md`.

### 2.1 Uzol vedený zákonným zástupcom

Uzol môže viesť **zákonný zástupca** (napríklad za maloletého). Vtedy platí:

- profil ani záznam v registri **neuvádzajú osobné údaje zastúpeného** — žiadne priezvisko, dátum narodenia,
  adresu ani mesto, školu, fotografiu, ani vlastný kontakt zastúpeného;
- uzol nesie **krstné meno alebo prezývku**; **kontaktom aj zodpovednou osobou je zástupca**;
- profil uvádza, že ho **spravuje zákonný zástupca**.

Profil aj register sú **verejné a trvalé** (história sa nemaže), preto sa pravidlo dodržiava od prvého
zverejnenia, nie dodatočne. To isté pravidlo je v podmienkach účasti uzla (§2).

## 3. Sekcie profilu a ich povinnosť

Od v0.2 sú **povinnosti odstupňované podľa stavu dostupnosti** (§3.9) a podľa toho, aké kapacity uzol má (§3.2).
Sekcie, ktoré v danom stave nie sú povinné, uzol **nemusí uvádzať vôbec** — profil bez nich je úplný
(nie „prázdna sekcia", ale sekcia, ktorá nemusí existovať). Ak ich uvedie, platí pre ne tento štandard.

| # | Sekcia | Povinná | Obsah |
|---|---|---|---|
| 3.1 | **Identifikácia uzla** | **vždy** | ID uzla pridelené Forge (`NODE-XXX`), názov uzla, prevádzkovateľ — entita alebo osoba (názov / krstné meno alebo prezývka; **IČO a sídlo len ak uzol podniká**, inak pôsobnosť — kraj/krajina), dátum založenia uzla; pri uzle vedenom zákonným zástupcom veta podľa §2.1 |
| 3.2 | **Kapacita** | **vždy** | **zoznam kapacít**; každá položka má **druh** zo slovníka (§3.2.1), voliteľný **podtyp** vlastnými slovami, **rozsah** (koľko, ako často alebo koľko je k dispozícii) a **polia svojho druhu** (§3.2.2). Uzol **bez akejkoľvek kapacity** uvedie pevnú hodnotu **`bez kapacity`** — aj to je údaj, ktorý sieť potrebuje |
| 3.3 | **Materiály** | **historická sekcia** (v0.1/v0.2) | Od v0.3 je to **pole položky druhu `stroj`** (§3.2.2). Profil podľa v0.1/v0.2 ju uvádza ako samostatnú sekciu a **je v súlade** (§6) |
| 3.4 | **Pracovný objem** | **historická sekcia** (v0.1/v0.2) | To isté — od v0.3 pole položky druhu `stroj` (§3.2.2) |
| 3.5 | **Ponuka** | v stave `prijíma zákazky` / `obmedzene` | čo uzol robí (tlač na zákazku, vlastný katalóg, modelovanie, postprocessing, doprava, prenájom priestoru…) + odkaz na katalóg uzla |
| 3.6 | **Cenník — štruktúra** | v stave `prijíma zákazky` / `obmedzene` | štandard predpisuje **len štruktúru, nie hodnoty**: položka · jednotka (ks / hod. / g / model) · spôsob určenia ceny (pevná / vzorec / na vyžiadanie) · poznámka. Konkrétne hodnoty žijú výhradne u uzla |
| 3.7 | **Lehoty** | v stave `prijíma zákazky` / `obmedzene` | typická lehota dodania, možnosť expresu, ako sa lehota potvrdzuje |
| 3.8 | **Kontakt** | **vždy** | zodpovedná osoba (pri zástupcovi: zástupca), e-mail / telefón / formulár, preferovaný kanál |
| 3.9 | **Stav dostupnosti** | **vždy** | jedna z hodnôt: `prijíma zákazky` · `obmedzene` · `neprijíma` + **dátum poslednej aktualizácie profilu** |
| 3.10 | **Záujem** | voliteľná (každý stav) | čo si uzol vyrába pre seba, čo ho zaujíma, čo by chcel skúsiť — **signál pre sieť bez záväzku**; nie je to ponuka ani dopyt |

### 3.2.1 Druhy kapacít (kľúče)

Kanonický zdroj definícií, príkladov a polí je **`druhy-kapacit.md`**. Kvôli samostatnosti tohto štandardu sú
kľúče zopakované aj tu:

| Kľúč | Druh | Jednou vetou |
|---|---|---|
| `stroj` | stroj | zariadenie, ktoré na požiadanie vyrobí, opracuje alebo zmeria vec |
| `materiál` | materiál | hmota, ktorá sa pri práci spotrebuje |
| `podklad` | digitálny podklad | hotový model alebo dokumentácia použiteľná bez toho, aby ju niekto znovu vytvoril |
| `priestor` | priestor | miesto na prácu, stretnutie alebo uloženie |
| `doprava` | doprava | presun vecí alebo ľudí |
| `ruky` | ruky a čas | pracovný čas, ktorý po krátkom zaučení zvládne ktokoľvek |
| `znalosť` | znalosť | schopnosť, ktorú nemožno nahradiť zaučením |
| `spôsobilosť` | právna spôsobilosť | subjekt, ktorý smie a vie konať navonok (podpis, faktúra, grant, potvrdenie) |
| `financovanie` | financovanie | prostriedky, ktoré uzol vie dať alebo dopredu vyložiť |
| `dosah` | dosah | prístup k ľuďom — k dopytu alebo k odbytu |
| `iné` | *(nie je druh)* | kapacita mimo slovníka; **podtyp je povinný** — je to vstup pre rozšírenie slovníka |

**Zoznam nie je uzavretý.** Ako pribudne nový druh a čo robí kontrola s neznámym druhom, hovorí
`druhy-kapacit.md` §6; podstatné je, že **neznámy druh nerobí profil nesúladným**.

### 3.2.2 Polia položky podľa druhu

Každá položka kapacity nesie polia svojho druhu (úplný zoznam v `druhy-kapacit.md` §3). Pre sieť sú záväzné
tieto dve, lebo bez nich sa dopyt na výrobu nedá posúdiť:

- položka druhu **`stroj`** uvádza **materiály** a **pracovný objem** (max. rozmery, obmedzenia geometrie);
- ostatné druhy uvádzajú polia svojho druhu podľa slovníka.

**Prečo sú tieto dve polia vnútri položky a nie sekciou profilu:** sú to vlastnosti **konkrétneho stroja**, nie
profilu. Uzol s tlačiarňou a šijacím strojom nevie do jednej sekcie napísať „PLA, PETG" aj „bavlna, plátno" tak,
aby bolo jasné, čo patrí čomu — a pri sto uzloch to prestane byť čitateľné úplne. Profil s jediným strojom je
tým nezmenene krátky: dva riadky vnútri jednej položky namiesto dvoch nadpisov.

**Prečo je 3.2 nezávislá od stavu:** je to údaj o tom, **čo uzol má**, nie o tom, čo ponúka. Sieť má vedieť,
že uzol má tlačiareň, dodávku alebo dielňu, aj keď zákazky neprijíma — práve to z neho robí uzol, ktorý môže
niekedy dopyt vziať.

**Prečo sú 3.5–3.7 viazané na stav:** ponuka, cenník a lehoty sú vyhlásením „beriem zákazky". Uzol v stave
`neprijíma` také vyhlásenie nerobí a nemôže mať cenník na niečo, čo neponúka.

> **Overenie profilu:** či je profil v súlade s týmto štandardom — hlavička `standard:`, prítomnosť a názvy
> sekcií povinných v danom stave, hodnoty v sekciách 3.2 a 3.9 — vie overiť **validátor platformy Forge**:
> `python -m forge_platform.profil <cesta k PROFILE.md>` (kód 0 = v súlade, 1 = nálezy; `--json` pre strojový
> výstup, kódy nálezov v `docs/KODY-NALEZOV.md` platformy). Validátor kontroluje len tvar profilu, nie obsah
> sekcií, a neznáme sekcie podľa §4 ignoruje. Kontroluje **podľa aktuálnej verzie štandardu**; hlavička
> `standard:` musí uvádzať verziu, ktorú platforma pozná (`v0.1`, `v0.2` alebo `v0.3`).
> *Prechodný stav (2026-09-07): kontrola podľa stavu ani podľa druhov kapacít sa do validátora ešte
> nenasadzuje; do nasadenia validátor vyžaduje sekcie 3.1–3.9 a hlavičku `v0.1` — profil napísaný podľa v0.2
> alebo v0.3 sa preto do registra zapíše až po nasadení. Text zadania pre platformu vznikne až nad týmto
> štandardom v0.3 (rozhodnutie riaditeľa 2026-09-07).*

## 4. Voliteľné sekcie a rozšírenia

Štandard je navrhnutý **rozšíriteľne** — uzol smie pridať vlastné sekcie a prevádzkové koncepty
(napr. vernostné podmienky, školy a vzdelávanie, servis, požičiavanie strojov):

- **3.10 Záujem** je voliteľná sekcia **štandardu** (má pevné číslo a názov; validátor ju pozná a jej
  neprítomnosť nie je nález),
- vlastné sekcie sa označia ako rozšírenie uzla (v `profile.yaml` prefix `x-`),
- čitateľ/nástroj Forge neznáme sekcie **ignoruje** (neznamenajú nekompatibilitu),
- rozšírenia, ktoré sa v praxi osvedčia, môžu byť prevzaté do ďalšej verzie štandardu
  (návrh podá uzol — vo Forge sa rozhodne štandardným postupom).

**Rozšírenie slovníka druhov** má vlastné pravidlo (`druhy-kapacit.md` §6) — nerieši sa cez `x-` sekcie, lebo
druh je hodnota, na ktorej sa páruje ponuka a dopyt, nie sekcia navyše.

## 5. Záznam uzla vo Forge

Forge vedie o uzle **len minimálny záznam** (`60-partners/NODE-XXX-*.md` a riadok v registri platformy):
ID, typ uzla, prevádzkovateľ (až po jeho výslovnom potvrdení — záznam môže byť verejne prístupný; pri uzle
vedenom zákonným zástupcom len „vedie zákonný zástupca"), **adresa profilu** (vlastná alebo adresa platformy),
stav. Nič viac — kanonický zdroj všetkého ostatného je profil uzla.

> **Podmienky účasti (od 2026-09-04):** čo znamená byť v registri siete — kto profil vlastní, čo s ním
> platforma smie robiť, ako sa uzol zapisuje a ako odchádza — je popísané v samostatnom dokumente
> **`podmienky-ucasti-uzla.md`** (v0.3, CC BY 4.0). Je to **pravidlo siete, nie zmluva** (D-2026-14, bod 5).

## 6. Zmeny štandardu

- Štandard verzuje Forge (tento súbor, FDS-006); zmeny významné pre uzly sa oznamujú v change logu.
- V rámci jednej major verzie sú zmeny **spätne kompatibilné: profil platný podľa staršej verzie je platný aj
  podľa novšej** — povinné sekcie sa neodoberajú a nové povinnosti sa bez zmeny major verzie nepridávajú;
  povinnosť sa smie len **uvoľniť alebo podmieniť** (ako vo v0.2) a smú pribudnúť voliteľné sekcie.
- Uzol nie je povinný prejsť na novú verziu okamžite; profil uvádza verziu, podľa ktorej je napísaný.
  Validátor platformy kontroluje podľa aktuálnej verzie a prijíma všetky verzie, ktoré pozná.

### 6.1 Pravidlo čítania sekcie 3.2 podľa verzie profilu (v0.3)

v0.3 mení **tvar zápisu** sekcie 3.2 (položka s druhom namiesto zoznamu strojov). Aby ostala v platnosti veta
„profil platný podľa staršej verzie je platný aj podľa novšej", platí toto pravidlo čítania:

- V profile s hlavičkou **`v0.1` alebo `v0.2`** sa **každá položka v 3.2 číta ako kapacita druhu `stroj`**
  a pevná hodnota **`bez strojov`** ako „žiadna kapacita druhu `stroj`". Sekcie 3.3 a 3.4 sa čítajú ako
  materiály a pracovný objem tejto kapacity. **Takýto profil je podľa v0.3 v súlade a nič v ňom netreba meniť.**
- V profile s hlavičkou **`v0.3`** má **každá položka uvedený druh**; uzol bez akejkoľvek kapacity uvedie
  `bez kapacity`. Hodnota `bez strojov` v ňom ostáva prípustná a znamená to isté ako predtým.

**Toto je čisté uvoľnenie:** žiadny existujúci profil sa nestáva nesúladným, žiadna povinná sekcia sa
neodoberá a povinnosť uviesť druh vzniká len v tvare, ktorý si uzol zvolí dobrovoľne prechodom na v0.3.
Oproti v0.2 je tu jeden rozdiel, ktorý treba pomenovať: **validátor už nevystačí s jediným pravidlom pre
všetky verzie** — potrebuje k nemu toto pravidlo čítania podľa hlavičky. Je to zmena v kóde platformy, nie
v tom, čo sieť od uzlov žiada.

## 7. Hranica zverejnenia

Profil uzla je verejný dokument uzla — **neobsahuje nič z L3 obsahu Forge** (D-2026-5): žiadne odkazy
na formálne jadro, víziu, etapy vývoja ani interné dokumenty Forge. Uzol o vnútorných vrstvách Forge
nič nepublikuje; Forge sa v profile spomína len ako platforma/sieť (L1/L2).

## Change Log

| Dátum | Zmena |
|---|---|
| 2026-08-31 | Prvá verzia (v0.1) — podľa D-2026-6 a D-2026-7 (inbox 2026-08-31, §4) — WS-010, SESSION-0029 |
| 2026-09-01 | **Prvý uzol publikoval profil podľa v0.1** — NODE-001 „Jawra", `github.com/matejolsavsky/jawra-profile` (PROFILE.md v0.1, hlavička `standard: v0.1`, sekcie 3.1–3.9 kompletné); verzia štandardu sa nemení — WS-010, SESSION-0030 |
| 2026-09-04 | **Doplnená poznámka o validátore** (§3): súlad profilu so štandardom v0.1 vie overiť CLI `python -m forge_platform.profil`; profil NODE-001 ním prešiel bez nálezu. Text štandardu ani povinné sekcie sa nemenia, **verzia ostáva v0.1** — D-2026-13 (R5, zadanie riaditeľa), WS-011, SESSION-0047 |
| 2026-09-04 | **Doplnená licenčná hlavička CC BY 4.0** (© 2026 Amunet s.r.o.) podľa **D-2026-14** bod 2 — text štandardu je voľne šíriteľný pri uvedení zdroja; názov „Forge", sieť a register uzlov nie sú predmetom licencie. Obsah štandardu, povinné sekcie ani verzia sa nemenia — **v0.1** — WS-011, SESSION-0052 |
| 2026-09-04 | **Doplnený odkaz na podmienky účasti uzla** (§5) — nový dokument `podmienky-ucasti-uzla.md` v0.1 (krok (iv) **D-2026-14**). Text štandardu, povinné sekcie ani verzia sa nemenia — **v0.1** — WS-011, SESSION-0053 |
| 2026-09-07 | **v0.2 — uzol nie je ponuka (D-2026-16):** §1 uzol = osoba alebo entita v sieti, ponuka je voľba vyjadrená stavom; sieť eviduje aj dopyt. **§3 povinnosti podľa stavu a vybavenia:** vždy 3.1, 3.2, 3.8, 3.9; 3.3–3.4 len ak 3.2 uvádza stroj (inak pevná hodnota `bez strojov`); 3.5–3.7 len v stave `prijíma zákazky` / `obmedzene` — v stave `neprijíma` nemusia existovať; **nová voliteľná sekcia 3.10 Záujem**. **§2 dve cesty na verejnú adresu — vlastné hostovanie alebo hostovanie platformou v mene uzla (D-2026-18)**; repozitár nie je podmienkou. **Nová §2.1 uzol vedený zákonným zástupcom (D-2026-19)** — bez osobných údajov zastúpeného, kontaktom je zástupca. §5 záznam eviduje adresu profilu. §6 pravidlo kompatibility spresnené (povinnosť sa smie len uvoľniť). **Hlavička nových profilov `standard: v0.2`; validátor prijíma `v0.1` aj `v0.2` a kontroluje jedným pravidlom (v0.2 je čisté uvoľnenie)** — rozhodnutie relácie v rámci zadania; kontrola podľa stavu = zadanie pre Programátora (prechodný stav v §3). Profil NODE-001 ostáva platný bez zmeny. Rozhodnutia riaditeľa 2026-09-05 a 2026-09-07 (inbox podľa P-009, zadania (26) a (27)) — WS-011, SESSION-0057 |
| 2026-09-07 | **v0.3 — kapacita má druh (D-2026-20):** **§3.2 už nie je zoznam strojov, ale zoznam kapacít** — každá položka má druh zo slovníka `druhy-kapacit.md` (nový dokument siete, v0.1: `stroj`, `materiál`, `podklad`, `priestor`, `doprava`, `ruky`, `znalosť`, `spôsobilosť`, `financovanie`, `dosah` + hodnota `iné`), voliteľný podtyp, rozsah a polia svojho druhu (nové §3.2.1 a §3.2.2). Pevná hodnota `bez strojov` z v0.2 sa dopĺňa hodnotou **`bez kapacity`** pre uzol bez akejkoľvek kapacity; obe ostávajú platné. **Materiály a pracovný objem sú od v0.3 poľami položky druhu `stroj`**, nie sekciami profilu — sekcie 3.3 a 3.4 ostávajú platné ako historické (odporúčanie relácie, dôsledky v §3.2.2). §1 doplnený o vetu „uzol neprispieva do siete len strojom" a o pravidlo, že **dopyt používa ten istý slovník** (D-2026-17). §4 doplnená o vetu, že slovník sa nerozširuje cez `x-` sekcie. **Nová §6.1 — pravidlo čítania 3.2 podľa verzie profilu:** položka v profile v0.1/v0.2 sa číta ako kapacita druhu `stroj`, takže **žiadny existujúci profil sa nestáva nesúladným**; v0.3 je preto čisté uvoľnenie, len s dôsledkom, že validátor potrebuje okrem jedného pravidla aj toto pravidlo čítania. **Ruší sa podmienka „ak 3.2 uvádza stroj" z D-2026-16** — nahrádza ju podmienka podľa druhu; D-2026-16 inak platí. **3.5–3.7 ostávajú viazané na stav — D-2026-16 sa v tomto nemení.** Profil NODE-001 (v0.1) ostáva platný bez zmeny. Rozhodnutie riaditeľa 2026-09-07 (inbox podľa P-009, zadanie SESSION-0058) — WS-011, SESSION-0058 |
