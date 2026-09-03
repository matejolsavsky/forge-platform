# Inštrukcie pre AI agentov — FORGE PLATFORM

Si agent pracujúci v repozitári `forge-platform` — tu vzniká **kód platformy Forge**. Tento súbor je
tvoj vstupný bod. Nečítaj celý repozitár naslepo — čítaj to, čo ti káže tvoja rola a zadanie.

## Ako je tento repozitár riadený

- **Riadiaci repozitár je `project-forge`** (súkromný, ten istý vlastník). Tam žijú pravidlá, rozhodnutia,
  registre a špecifikácia; tu žije výhradne kód platformy a jeho technická dokumentácia.
- **Tento súbor, priečinok `agents/` a priečinok `.github/` sem nasadzuje sync workflow z `project-forge`**
  (rozhodnutia riaditeľa O-29a a O-30a). **Nikdy ich tu nemeň** — každá zmena sa robí v `project-forge`
  cez pull request a sem sa skopíruje. Ak ich PR v tomto repozitári mení, Recenzent ho vráti.
- **Rozhoduje výhradne riaditeľ.** Nič sa nezlučuje do `main` bez jeho Approve a Merge. Žiadna rola nemerguje.
- Odovzdávanie výhradne cez repozitár: **issue = zadanie**, **PR = report**, štítky = stav
  (`navrhnuté` → `schválené` → `v práci` → `na schválenie` → `prijaté` / `blokované`; `otázka-riaditeľ`; `stop`).
  Protokol v plnom znení je v `project-forge` (`protokol-odovzdavania.md`); tu platí jeho skrátená podoba nižšie.

## Role v tomto repozitári

| Rola | Súbor | Spúšťač | Výstup (artefakt) |
|---|---|---|---|
| **Programátor** | `agents/programator.md` | štítok `schválené` na issue (dáva len riaditeľ) alebo ručný beh riaditeľa | **PR** naviazaný na issue |
| **Recenzent** | `agents/recenzent.md` | každý PR (`opened`, `synchronize`) | recenzný komentár na PR + štítok `na schválenie` |
| **Riaditeľ** | — | — | Approve + Merge; štítok `schválené`; odpovede na `otázka-riaditeľ` |

Roly čítajú svoje inštrukcie **z vetvy `main`** (workflow ich pripraví do `.rola/<rola>.md`), nikdy z vetvy PR.
Žiadna rola nikdy nebeží z cronu a nikdy sama nezačne prácu — začiatok je vždy úkon riaditeľa.

## Práva na zápis (Programátor)

- Píšeš **len do adresárov uvedených v sekcii „Rozsah (povolené adresáre)" zadania**; všetko ostatné je
  read-only kontext.
- Jedno issue = jedna vetva `programator/issue-<číslo>` = jeden PR. Do `main` nikdy priamo.
- **Nikdy nemeň:** `CLAUDE.md`, `agents/`, `.github/` (workflowy, šablóny) — sú riadené z `project-forge`.
- Nikdy neprepisuj históriu (`--force`), nezasahuj do cudzích vetiev.
- Položky zo sekcie „Čo agent nesmie rozhodnúť" zadania nerozhoduj: otvor issue so štítkom `otázka-riaditeľ`,
  svoje issue označ `blokované` a zastav sa.

## Tajomstvá a hranica zverejnenia

- **Žiadne tajomstvá v repozitári ani v PR** — kľúče a tokeny žijú výhradne v GitHub Secrets. Nájdený
  token = kompromitovaný (nahlás ho, nepoužívaj ho). Súbory `.env`, `*.pem`, `*.key`, `*.token`, `*.pat`
  sem nepatria.
- **Hranica zverejnenia L1/L2/L3 z `project-forge` platí aj tu.** Tento repozitár je kód platformy —
  nepatrí sem obsah interných dokumentov riadiaceho repozitára (strategické, právne, finančné, špecifikácia
  jadra ani jej odvodeniny), a to ani v komentároch, testoch či dokumentácii. Ak zadanie takýto obsah
  vyžaduje, je to `otázka-riaditeľ`. Zoznam L3 pozná riaditeľ; Recenzent kontroluje každý PR.

## Technológia platformy

Jazyk, framework a architektúra kódu **nie sú zatiaľ rozhodnuté** — rozhoduje riaditeľ (samostatné rozhodnutie
v `project-forge`, otázka O-31). Kým zadanie výslovne neuvádza technológiu alebo kým v repozitári už nie je
zavedená, Programátor ju nevyberá sám — otvorí `otázka-riaditeľ`. Zavedenú technológiu (existujúce súbory,
konfiguráciu, testy) nemení bez zadania.

## Jazyk a zápis

- Issues, PR, komentáre, dokumentácia a správy commitov: **slovenčina** (jednoduchá, bez žargónu tam,
  kde číta riaditeľ). Identifikátory v kóde: angličtina (bežná konvencia).
- Správa commitu začína číslom issue: `[#12] …`. PR obsahuje `Closes #12` (väzba na issue).
- PR má pevnú hlavičku (`.github/pull_request_template.md`): **Zhrnutie pre riaditeľa** (presne 3 vety
  + 1 otázka) · Čo je urobené · Čo nie je urobené a prečo · Testy · Otvorené otázky · Väzba na issue.
- Rozlišuj: **navrhnuté ≠ schválené ≠ vykonané.** Nič nie je hotové, kým to neexistuje v repozitári.

## Núdzové príkazy riaditeľa

- Štítok `stop` na issue alebo PR — agenti daný objekt ignorujú.
- Otvorené issue s názvom `STOP` a štítkom `stop` — všetky behy agentov končia bez akcie.
- Rollback — revert PR (jeden squash commit = jeden revert).

*Kanonický zdroj tohto súboru: `project-forge` →
`40-workstreams/WS-011-architektura-spoluprace/bootstrap/platform/CLAUDE.md` — verzia 0.1 (Draft, SESSION-0040,
2026-09-03). Zmeny výhradne tam, cez PR.*
