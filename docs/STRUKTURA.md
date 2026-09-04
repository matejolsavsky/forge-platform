# Štruktúra repozitára

- `agents/` — inštrukcie pre role agentov (Programátor, Recenzent); nasadzuje ich sync z `project-forge`.
- `docs/` — technická dokumentácia platformy Forge.
- `src/forge_platform/` — zdrojový kód platformy. Jazyk: Python 3.12+ (D-2026-12). Balíky:
  - `profil/` — validátor profilu uzla (`PROFILE.md`) proti Štandardu profilu uzla siete Forge v0.1.
- `tests/` — testy platformy (`pytest`), vrátane `tests/fixtures/` s testovacími profilmi uzla.
- `.github/` — konfigurácia repozitára (workflowy, šablóny); nasadzuje ju sync z `project-forge`.
