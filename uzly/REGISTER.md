# Register uzlov siete Forge

Register je zoznam uzlov siete Forge a odkazov na ich profily. Hromadná validácia
(`python -m forge_platform.register`) načíta túto tabuľku a pre každý uzol s vyplnenou lokálnou
cestou spustí nad jeho profilom validátor `forge_platform.profil`. Cesty v stĺpci
„Profil (cesta)" sú relatívne k priečinku tohto súboru. Stĺpec „Profil (URL)" sa iba eviduje —
sťahovanie profilu z URL táto verzia platformy nerobí.

| ID | Názov | Profil (cesta) | Profil (URL) | Stav |
|---|---|---|---|---|
| NODE-001 | Jawra |  | https://github.com/matejolsavsky/jawra-profile/blob/main/PROFILE.md | pripravuje sa |
