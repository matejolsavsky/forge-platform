# Kódy nálezov validátora profilu uzla — FDS-003

**Dokument:** FDS-003 · **Projekt:** Project Forge · **Workstream:** WS-011 · **Repozitár:** `forge-platform` ·
**Verzia:** 0.1 (Draft) · **Väzba:** issue #7, D-2026-13

Táto tabuľka je verejný kontrakt validátora profilu uzla (`src/forge_platform/profil/validator.py`,
trieda `Kody`). Používajú ju ľudia aj strojové integrácie (napr. `--json`, budúci register uzlov
s hromadnou validáciou).

> **Pravidlo:** kódy nálezov sa **nemenia a nerušia**, len **pridávajú**. Zmena významu existujúceho
> kódu je rozhodnutie riaditeľa.

## Kódy

| Kód | Správa | Význam |
|---|---|---|
| H001 | Hlavička so štandardom ('standard: v0.1') v profile chýba. | V profile chýba riadok s hlavičkou `standard:`. |
| H002 | Verzia štandardu '\<hodnota>' nezodpovedá v0.1. | Hlavička `standard:` obsahuje inú verziu štandardu než `v0.1`. |
| S001 | Povinná sekcia \<číslo> \<názov> chýba. | V profile chýba niektorá z povinných sekcií 3.1–3.9. |
| S002 | Sekcia \<číslo> má neočakávaný názov nadpisu. | Povinná sekcia existuje, ale jej nadpis nezodpovedá očakávanému názvu. |
| P001 | V sekcii 3.9 chýba stav dostupnosti (prijíma zákazky / obmedzene / neprijíma). | Sekcia 3.9 (Stav dostupnosti) neobsahuje žiadnu z povolených hodnôt stavu. |
| P002 | V sekcii 3.9 chýba dátum v tvare RRRR-MM-DD. | Sekcia 3.9 (Stav dostupnosti) neobsahuje dátum v požadovanom tvare. |

## Change Log

| Verzia | Dátum | Zmena |
|---|---|---|
| 0.1 | 2026-09-04 | Prvá verzia — kódy nálezov vyňaté z `validator.py` do triedy `Kody` a zdokumentované ako verejný kontrakt (issue #7). |
