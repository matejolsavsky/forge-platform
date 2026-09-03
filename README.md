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
  synchronizáciou odtiaľ a mení sa výhradne tam.

## Stav

Bootstrap; technológia zatiaľ nerozhodnutá (O-31).
