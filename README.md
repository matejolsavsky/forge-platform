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

Python; prvá funkcia — validátor profilu uzla podľa štandardu v0.1.

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
`R002`) sú popísané v [`docs/KODY-REGISTRA.md`](docs/KODY-REGISTRA.md).
