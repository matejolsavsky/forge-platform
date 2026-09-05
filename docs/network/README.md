# Verejné dokumenty siete Forge

Tento priečinok obsahuje **pravidlá siete uzlov Forge** — nie dokumentáciu kódu platformy.
Sú tu preto, aby mali **verejnú adresu**: dá sa na ne odkázať, dajú sa citovať a otvorí ich ktokoľvek
aj bez prihlásenia.

| Súbor | Čo to je |
|---|---|
| `standard-profil-uzla.md` | **Štandard profilu uzla** — čo má obsahovať `PROFILE.md` uzla (povinné sekcie, prípustné hodnoty). Práve tento štandard kontroluje validátor platformy (`python -m forge_platform.profil`). |
| `podmienky-ucasti-uzla.md` | **Podmienky účasti uzla** — čo znamená byť v registri siete. **Pravidlo siete, nie zmluva**; **záväzné znenie**. |
| `node-participation-terms.md` | **Node Participation Terms** — anglický **preklad** podmienok účasti. Pri rozpore platí slovenské znenie. |

**Slovenské a anglické znenie podmienok sa verzujú spolu** — nesú rovnaké číslo verzie a menia sa
v tej istej zmene; anglická verzia nikdy neostáva pozadu.

## Toto sú nasadené kópie — needitujú sa tu

**Kanonický zdroj týchto dokumentov je repozitár `project-forge`** (`20-ecosystem/network/`).
Do `forge-platform` ich **kopíruje sync** (O-29a/O-30a, rozhodnutie **D-2026-15**) a kópie sú
**bitovo zhodné** s kanonickými súbormi. Zmena vykonaná priamo tu by sa pri najbližšom behu syncu
stratila — vrátane zmeny od agenta. **Programátor tento priečinok nemení**; nepatrí do rozsahu
žiadneho zadania o kóde.

**Ako navrhnúť zmenu:** založ **issue v tomto repozitári** — prevádzkovateľ siete ju posúdi a zmenu
vykoná v kanonickom zdroji, odkiaľ sa sem nasadí sama.

## Licencia

Texty sú pod **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)** — © 2026 Amunet s.r.o.
(platí licencia celého priečinka `docs/`, viď `../LICENSE-DOCS.md`). **Názov „Forge", sieť uzlov
a register uzlov nie sú predmetom licencie** (súbor `NOTICE` v koreni). Kód platformy je pod
Apache-2.0 (súbor `LICENSE`).

*Kanonický zdroj tohto súboru: `project-forge` →
`40-workstreams/WS-011-architektura-spoluprace/bootstrap/platform/docs/network/README.md`.
Do `forge-platform` ho nasadzuje sync (O-30a); tam sa needituje.*
