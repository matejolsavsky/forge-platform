# Štandard profilu uzla siete Forge

**Owner:** WS-010 · **Verzia:** 0.1 · **Status:** Draft · **Dátum:** 2026-08-31
**Audience:** public-ready — navrhnuté ako **verejný štandard** (zverejní sa spolu s prvým uzlom);
obsah je L1/L2 podľa D-2026-5, kontrola L3 vykonaná.
**Rozhodnutia:** **D-2026-6** (Forge = bezplatná platforma; uzly podnikajú komerčne ako samostatné
entity), **D-2026-7** (architektúra „kontrakt cez špecifikáciu"; NODE-001 prvý uzol) — `registry/decisions.md`.
**Licencia:** text tohto štandardu je pod **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)** —
© 2026 Amunet s.r.o. Smie sa kopírovať, šíriť a upravovať aj komerčne pri uvedení zdroja; **názov „Forge",
sieť uzlov a register uzlov nie sú predmetom licencie** (D-2026-14, bod 2). Kód platformy je samostatne pod
Apache-2.0 (repozitár `forge-platform`).
Terminológia: RFC-000 (uzol ≈ Machine + Capability prevádzkované entitou).

---

## 1. Účel a princíp

Uzol siete Forge je **samostatná podnikateľská entita**, ktorá na platforme Forge ponúka výrobnú
kapacitu (napíklad 3D tlač) a **podniká komerčne vo vlastnom mene a na vlastnú zodpovednosť**.
Forge je bezplatná platforma — nemá podiel na tržbách uzla a jeho komerčnú činnosť neprevádzkuje.

Vzťah Forge ↔ uzol je **kontrakt cez špecifikáciu**:

1. Forge definuje a verzuje tento štandard profilu uzla.
2. Uzol žije vo **vlastnom samostatnom repozitári**, kde vedie svoj profil podľa tohto štandardu
   a všetky svoje komerčné detaily (cenníkové hodnoty, katalóg, prevádzkové postupy).
3. Forge na repozitár uzla **iba linkuje** (záznam `60-partners/NODE-XXX-*`). Žiadne prelínanie obsahu
   — komerčné údaje uzla sa do repozitára Forge nezapisujú a obsah Forge sa nekopíruje do repa uzla.

**Profil uzla je jediné rozhranie** medzi uzlom a sieťou: čo nie je v profile, sieť o uzle nevie.

## 2. Ako uzol publikuje profil

- Profil je súbor **`PROFILE.md`** v koreni repozitára uzla (jazyk podľa pôsobnosti uzla — SK/CZ/EN).
- Profil má vlastnú verziu a change log (menený len prevádzkovateľom uzla).
- Voliteľne môže uzol pridať strojovo čitateľnú podobu **`profile.yaml`** s rovnakými poľami;
  pri rozpore platí `PROFILE.md`.
- Hlavička profilu uvádza verziu tohto štandardu, podľa ktorej je napísaný (napr. `standard: v0.1`).

## 3. Povinné sekcie profilu

| # | Sekcia | Obsah |
|---|---|---|
| 3.1 | **Identifikácia uzla** | ID uzla pridelené Forge (`NODE-XXX`), názov uzla, prevádzkovateľ (názov entity, IČO, sídlo/pôsobnosť), dátum založenia uzla |
| 3.2 | **Kapacita** | stroje (počet, typ / technológia — napr. FDM, SLA), orientačná dostupná kapacita (hod./týždeň alebo ks/týždeň) |
| 3.3 | **Materiály** | zoznam materiálov (napr. PLA, PETG, ABS, resin), poznámka k farbám a materiálom na vyžiadanie |
| 3.4 | **Pracovný objem** | maximálne rozmery tlače/výroby na stroj (mm), prípadné obmedzenia geometrie |
| 3.5 | **Ponuka** | čo uzol robí (tlač na zákazku, vlastný katalóg, modelovanie, postprocessing…) + odkaz na katalóg v repe uzla |
| 3.6 | **Cenník — štruktúra** | štandard predpisuje **len štruktúru, nie hodnoty**: položka · jednotka (ks / hod. / g / model) · spôsob určenia ceny (pevná / vzorec / na vyžiadanie) · poznámka. Konkrétne hodnoty žijú výhradne v repe uzla |
| 3.7 | **Lehoty** | typická lehota dodania, možnosť expresu, ako sa lehota potvrdzuje |
| 3.8 | **Kontakt** | zodpovedná osoba, e-mail / telefón / formulár, preferovaný kanál |
| 3.9 | **Stav dostupnosti** | jedna z hodnôt: `prijíma zákazky` · `obmedzene` · `neprijíma` + **dátum poslednej aktualizácie profilu** |

> **Overenie profilu (od 2026-09-04):** či je profil v súlade s touto verziou štandardu — hlavička
> `standard:`, prítomnosť a názvy povinných sekcií 3.1–3.9 a hodnoty v sekcii 3.9 — vie overiť **validátor
> platformy Forge**: `python -m forge_platform.profil <cesta k PROFILE.md>` (kód 0 = v súlade, 1 = nálezy).
> Validátor kontroluje len tvar profilu, nie obsah sekcií, a neznáme sekcie podľa §4 ignoruje. Profil
> NODE-001 ním prešiel bez nálezu.

## 4. Voliteľné sekcie a rozšírenia

Štandard je navrhnutý **rozšíriteľne** — uzol smie pridať vlastné sekcie a prevádzkové koncepty
(napr. vernostné podmienky, školy a vzdelávanie, servis, požičiavanie strojov):

- vlastné sekcie sa označia ako rozšírenie uzla (v `profile.yaml` prefix `x-`),
- čitateľ/nástroj Forge neznáme sekcie **ignoruje** (neznamenajú nekompatibilitu),
- rozšírenia, ktoré sa v praxi osvedčia, môžu byť prevzaté do ďalšej verzie štandardu
  (návrh podaj prevádzkovateľ uzla — vo Forge sa rozhodne štandardným postupom).

## 5. Záznam uzla vo Forge

Forge vedie o uzle **len minimálny záznam** (`60-partners/NODE-XXX-*.md`): ID, typ uzla,
prevádzkovateľ (až po jeho výslovnom potvrdení — záznam môže byť verejne prístupný),
link na repozitár uzla, stav. Nič viac — kanonický zdroj všetkého ostatného je profil v repe uzla.

> **Podmienky účasti (od 2026-09-04):** čo znamená byť v registri siete — kto profil vlastní, čo s ním
> platforma smie robiť, ako sa uzol zapisuje a ako odchádza — je popísané v samostatnom dokumente
> **`podmienky-ucasti-uzla.md`** (v0.1, CC BY 4.0). Je to **pravidlo siete, nie zmluva** (D-2026-14, bod 5).

## 6. Zmeny štandardu

- Štandard verzuje Forge (tento súbor, FDS-006); zmeny significanté pre uzly sa oznamujú v change logu.
- V rámci jednej major verzie sú zmeny spätne kompatibilné (povinné sekcie sa nemenia ani neodúberajú).
- Uzol nie je povinný prejsť na novú verziu okamžite; profil uvádza verziu, podľa ktorej je napísaný.

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
