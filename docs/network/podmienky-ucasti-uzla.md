# Podmienky účasti uzla v sieti Forge

**Owner:** WS-011 · **Verzia:** 0.1 · **Status:** Draft · **Dátum:** 2026-09-04
**Audience:** public-ready — určené na zverejnenie spolu so štandardom profilu uzla;
obsah je L1/L2 podľa D-2026-5, kontrola L3 vykonaná.
**Jazykové znenie:** **Záväzné je slovenské znenie; anglická verzia je preklad.**
Anglické znenie je `node-participation-terms.md` (v0.1); obe verzie nesú tú istú verziu a menia sa spolu.
**Rozhodnutia:** **D-2026-14** bod 5 (podmienky účasti ako pravidlo siete), **D-2026-6** (Forge = bezplatná
platforma; uzly podnikajú komerčne ako samostatné entity), **D-2026-7** („kontrakt cez špecifikáciu") —
`registry/decisions.md`.
**Licencia:** text je pod **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)** — © 2026 Amunet s.r.o.;
**názov „Forge", sieť uzlov a register uzlov nie sú predmetom licencie**. Kód platformy je samostatne pod
Apache-2.0 (repozitár `forge-platform`).
**Povaha dokumentu:** **pravidlo siete, nie zmluva.** Nezakladá záväzky ani nároky; popisuje, ako sieť funguje
a čo znamená byť v jej registri. Súvisiace dokumenty: `standard-profil-uzla.md` (čo má profil obsahovať),
`forge-platform` (kód, ktorý profily číta a kontroluje).

---

## 1. Načo je tento dokument

Sieť Forge vedie **verejný register uzlov**. Uzol je samostatná podnikateľská entita, ktorá ponúka výrobnú
kapacitu (napríklad 3D tlač) a **podniká vo vlastnom mene a na vlastnú zodpovednosť**. Forge je bezplatná
platforma — nemá podiel na tržbách uzla a jeho činnosť neprevádzkuje.

Tento dokument hovorí, **čo znamená byť v registri**: čo od uzla sieť čaká, čo s jeho údajmi robí a ako sa
zo siete odchádza. Je určený každému, kto zvažuje zápis svojho uzla.

## 2. Profil uzla je verejný a patrí uzlu

- Uzol vedie svoj profil (`PROFILE.md`) podľa **verejného štandardu profilu uzla** vo **vlastnom verejnom
  repozitári** alebo na inom verejnom mieste, ktoré vie sieť prečítať.
- **Obsah profilu určuje uzol.** Profil je jeho dokument — Forge ho nepíše, needituje a nepripomienkuje.
- Profil je **jediné rozhranie** medzi uzlom a sieťou: čo v ňom nie je, o tom sieť nevie.

## 3. Čo s profilom robí platforma

Platforma Forge smie profil **zobrazovať, sťahovať a automaticky kontrolovať** proti štandardu (súlad tvaru:
hlavička verzie, prítomnosť povinných sekcií, prípustné hodnoty stavu). Kontrola beží pravidelne a jej
výsledok je verejný — rovnako ako profil.

Platforma profil **nemení a neukladá**: v repozitári platformy ostáva len odkaz a záznam v registri, nie kópia
obsahu. Nesúlad so štandardom je **nález, nie sankcia** — ide o informáciu pre uzol, že jeho profil sa
odchýlil od tvaru, ktorý sieť očakáva.

## 4. Za pravdivosť ručí uzol

Údaje v profile — kapacita, materiály, lehoty, ceny, kontakty — sú **vyhlásením uzla**. Forge ich neoveruje,
nepotvrdzuje a neručí za ne, ani za splnenie zákaziek, ktoré uzol prijme. Kto s uzlom obchoduje, obchoduje
s ním, nie s Forge.

## 5. Zápis do registra

- Zápis je **bezplatný** a nezakladá žiadny poplatok — ani jednorazový, ani opakovaný.
- Uzol o zápis **požiada** (issue v repozitári platformy alebo e-mail); zapisuje **prevádzkovateľ siete**.
- Do registra ide **minimum**: identifikátor uzla, názov, odkaz na profil a stav. Všetko ostatné ostáva
  v profile uzla.
- Zápis nie je schvaľovanie kvality ani odporúčanie uzla — je to evidencia, že uzol je súčasťou siete.

## 6. Odchod a vyradenie

- Uzol môže **kedykoľvek odísť**: požiada o výmaz a jeho riadok sa z registra odstráni. Dôvod neuvádza.
- Výmaz sa týka registra; **história verejného repozitára ostáva** — zverejnené záznamy sa spätne nemažú.
- Prevádzkovateľ siete smie uzol z registra **vyradiť** pri porušení týchto pravidiel alebo pri trvalej
  nedostupnosti profilu — **vždy s uvedením dôvodu** v zázname o vyradení.
- Uzol mimo registra sa neoznačuje ako uzol siete Forge.

## 7. Žiadna záruka a žiadny vzťah

Účasť v sieti **nezakladá zastúpenie, partnerstvo, spoločný podnik ani pracovný vzťah** medzi uzlom a Forge
(ani medzi uzlami navzájom). Uzly sú samostatné subjekty a obchodujú vo vlastnom mene a na vlastnú
zodpovednosť. Forge poskytuje sieť a nástroje **tak, ako sú**, bez záruky dostupnosti a bez záruky výsledku.

## 8. Zmeny týchto pravidiel

Dokument sa **verzuje** ako každý iný dokument siete; zmeny sú v change logu nižšie a platia odo dňa zápisu.
Uzol, ktorý so zmenou nesúhlasí, môže odísť podľa §6. Podstatné zmeny sa oznamujú cez register.

**Slovenské a anglické znenie sa verzujú spolu:** každá zmena slovenského textu sa v tej istej zmene premietne
aj do `node-participation-terms.md`; anglická verzia nesmie ostať pozadu a obe nesú rovnaké číslo verzie.
Pri rozpore platí slovenské znenie.

## Change Log

| Dátum | Zmena |
|---|---|
| 2026-09-04 | Prvá verzia (v0.1) — krok (iv) rozhodnutia **D-2026-14**, podľa osnovy v handoffe SESSION-0052; pravidlo siete, nie zmluva; text pod CC BY 4.0 — WS-011, SESSION-0053 |
| 2026-09-04 | **Doplnené jazykové znenie** — záväzné je slovenské znenie, anglická verzia `node-participation-terms.md` v0.1 je preklad; §8 doplnená o pravidlo **„obe znenia sa verzujú spolu"**. Obsah pravidiel sa nemení, **verzia ostáva v0.1** — rozhodnutie riaditeľa 2026-09-04, WS-011, SESSION-0054 |
