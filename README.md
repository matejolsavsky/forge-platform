# forge-platform

Repozitár **forge-platform** je miesto, kde vzniká kód platformy **Project Forge**.

## Čo je Project Forge

Project Forge je bezplatná platforma. Jej uzly fungujú ako samostatné subjekty, nie ako pobočky
jednej centrály. Platforma vzniká postupne, krok za krokom, formou verejne overiteľných zmien.
Prvým prostredím, v ktorom sa Forge overuje, je 3D tlač v školách. Cieľom je, aby si uzly vedeli
zdieľať skúsenosti a nástroje bez zbytočnej byrokracie. Tento repozitár obsahuje výhradne technickú
časť platformy — kód a jeho dokumentáciu.

## Ako sa tu pracuje

Pravidlá spolupráce definuje súbor [`CLAUDE.md`](CLAUDE.md) — je to záväzný vstupný bod pre každého
agenta, ktorý v repozitári pracuje. V skratke:

- Prácu vykonáva rola **Programátor** (`agents/programator.md`) na základe issue so štítkom
  `schválené`; výstupom je vždy jeden pull request naviazaný na dané issue.
- Každý pull request nezávisle skontroluje rola **Recenzent** (`agents/recenzent.md`) a výsledok
  zapíše ako komentár na PR.
- O tom, čo sa zlúči do `main`, rozhoduje výhradne riaditeľ.
- Štítok `stop` zastavuje prácu na danom issue alebo PR. Štítok `otázka-riaditeľ` označuje vec,
  ktorú musí rozhodnúť riaditeľ.
- Tento repozitár je riadený z oddeleného repozitára `project-forge`, kde žijú pravidlá,
  rozhodnutia a špecifikácia. Súbory `CLAUDE.md`, `agents/` a `.github/` sem prichádzajú
  synchronizáciou odtiaľ a menia sa výhradne tam.

## Stav

Python. Validátor profilu uzla podľa štandardu v0.1, strojový výstup `--json` so stabilnými
kódmi nálezov, register uzlov s hromadnou validáciou a sťahovaním profilov z URL, denná
automatická kontrola registra.

## Použitie

Validátor profilu uzla skontroluje `PROFILE.md` proti Štandardu profilu uzla siete Forge v0.1
a vypíše nájdené odchýlky:

```
python -m forge_platform.profil <cesta k PROFILE.md>
```

Návratový kód:

- `0` — profil je v súlade so štandardom, žiadne odchýlky,
- `1` — profil má odchýlky (vypísané na `stdout`),
- `2` — súbor sa nedá prečítať alebo bol príkaz zavolaný nesprávne (hlásenie na `stderr`).

Prepínač `--json` (môže stáť pred cestou aj za ňou) vypíše výsledok strojovo čitateľne — jeden riadok
JSON na `stdout`:

```
python -m forge_platform.profil --json <cesta k PROFILE.md>
```

```
{"standard": "v0.1", "cesta": "<cesta>", "v_sulade": false, "nalezy": [{"kod": "S001", "sprava": "…", "riadok": null}]}
```

Kódy nálezov (`H001`, `S001`, …) sú popísané v [`docs/KODY-NALEZOV.md`](docs/KODY-NALEZOV.md) — sú
verejný kontrakt a od svojho zavedenia sa nemenia, len pridávajú.

Register uzlov (`uzly/REGISTER.md`) umožňuje zvalidovať profily viacerých uzlov naraz — hromadná
validácia beží výhradne nad lokálnymi cestami k profilom, URL sa v registri len eviduje:

```
python -m forge_platform.register <cesta k registru>
```

```
NODE-001 · pripravuje sa · preskočený (R001)
Spolu: 1 uzlov · 0 v súlade · 0 s nálezmi · 1 preskočených
```

Rovnako ako pri validátore profilu, prepínač `--json` (môže stáť pred cestou aj za ňou) vypíše
výsledok strojovo čitateľne — jeden riadok JSON na `stdout`. Návratový kód je `0`, ak je každý
validovaný uzol v súlade (preskočené uzly kód nemenia), `1`, ak má aspoň jeden uzol nález, a `2`,
ak sa register nedá spracovať alebo bol príkaz zavolaný nesprávne. Kódy nálezov registra (`R001`,
`R002`, `R003`) sú popísané v [`docs/KODY-REGISTRA.md`](docs/KODY-REGISTRA.md).

Prepínač `--stiahnut` (môže stáť pred cestou aj za ňou, rovnako ako `--json`) zapne sťahovanie:
uzol **bez** lokálnej cesty, ale s vyplnenou URL, sa stiahne (výhradne cez `urllib.request` zo
štandardnej knižnice, timeout 10 s, limit 256 KiB) a zvaliduje rovnakým validátorom ako lokálny
súbor. Uzol s vyplnenou lokálnou cestou sa vždy validuje zo súboru — aj keď má vyplnenú aj URL,
sťahovanie sa preň nevolá. Bez `--stiahnut` sa uzol bez cesty naďalej len preskočí (`R001`), presne
ako doteraz.

```
python -m forge_platform.register --stiahnut <cesta k registru>
```

V textovom výstupe má riadok uzla validovaného z URL za stavom značku `· z URL`. V `--json` výstupe
má každý uzol pole `"zdroj"` s hodnotou `"cesta"`, `"url"` alebo `null` (preskočený).

## Licencia

Kód tohto repozitára je pod **Apache License 2.0** — pozri [`LICENSE`](LICENSE); držiteľ
autorských práv je uvedený tam. Dokumentácia v [`docs/`](docs/) je pod **CC BY 4.0** — pozri
[`docs/LICENSE-DOCS.md`](docs/LICENSE-DOCS.md). Názov „Forge", sieť a register uzlov nie sú
predmetom licencie kódu — pozri [`NOTICE`](NOTICE).

Čo znamená byť uzlom v registri siete, popisujú [podmienky účasti uzla](https://github.com/matejolsavsky/forge-platform/blob/main/docs/network/podmienky-ucasti-uzla.md)
(v0.1, CC BY 4.0) — je to pravidlo siete, nie zmluva; záväzné je slovenské znenie, k dispozícii je
aj [anglický preklad](https://github.com/matejolsavsky/forge-platform/blob/main/docs/network/node-participation-terms.md).
Formálne požiadavky na profil uzla stanovuje [štandard profilu uzla](https://github.com/matejolsavsky/forge-platform/blob/main/docs/network/standard-profil-uzla.md).

## Príspevky zvonka

Repozitár je verejný; issues a pull requesty od kohokoľvek sú vítané, ale nie je záruka, že budú
prijaté — triedi ich riaditeľ projektu. Automatický recenzent nebeží na pull requestoch z forkov
(nemajú prístup k tajomstvám repozitára) — je to zámer, nie chyba; takéto PR posudzuje riaditeľ.
Prácu agenta v tomto repozitári spúšťa výhradne riaditeľ štítkom na issue; samotné otvorenie issue
ani PR nič nespúšťa. Pravidlá práce v repozitári sú v [`CLAUDE.md`](CLAUDE.md); pravidlá
a rozhodnutia projektu žijú v samostatnom repozitári `project-forge`.
