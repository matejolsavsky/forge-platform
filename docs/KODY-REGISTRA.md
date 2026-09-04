# Kódy registra uzlov

**Projekt:** Project Forge · **Workstream:** WS-011 · **Repozitár:** `forge-platform` ·
**Verzia:** 0.1 (Draft) · **Väzba:** issue #9, D-2026-13

Táto tabuľka je verejný kontrakt hromadnej validácie registra uzlov
(`src/forge_platform/register/register.py`, trieda `KodyRegistra`). Kódy nálezov samotného
validátora profilu uzla (`H001`, `S001`, …) sú zdokumentované osobitne v
[`docs/KODY-NALEZOV.md`](KODY-NALEZOV.md) — register ich pri validácii jednotlivých profilov len
preberá.

> **Pravidlo:** kódy sa **nemenia a nerušia**, len **pridávajú**. Zmena významu existujúceho kódu
> je rozhodnutie riaditeľa.

## Kódy

| Kód | Správa | Význam |
|---|---|---|
| R001 | Uzol nemá v registri lokálnu cestu k profilu — preskočený. | Bunka „Profil (cesta)" je v registri prázdna; uzol sa nevaliduje a nemení návratový kód. |
| R002 | Profil na uvedenej ceste sa nedá prečítať. | Bunka „Profil (cesta)" je vyplnená, ale súbor na uvedenej ceste neexistuje alebo sa nedá otvoriť. |

## Change Log

| Verzia | Dátum | Zmena |
|---|---|---|
| 0.1 | 2026-09-04 | Prvá verzia — kódy registra uzlov v triede `KodyRegistra` a zdokumentované ako verejný kontrakt (issue #9). |
