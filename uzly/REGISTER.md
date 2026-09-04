# Register uzlov siete Forge

Register je zoznam uzlov siete Forge a odkazov na ich profily — cesty alebo URL. Hromadná validácia
(`python -m forge_platform.register`) načíta túto tabuľku a pre každý uzol s vyplnenou lokálnou
cestou spustí nad jeho profilom validátor `forge_platform.profil`; beží výhradne nad lokálnymi
cestami. Cesty v stĺpci „Profil (cesta)" sú relatívne k priečinku tohto súboru. S prepínačom
`--stiahnut` si platforma profil uzla bez lokálnej cesty, ale s vyplnenou URL, stiahne priamo
z adresy v stĺpci „Profil (URL)" (`https://`, GitHub `blob` URL sa prevedie na `raw`) a zvaliduje
rovnako ako lokálny súbor. Profil zostáva vo vlastníctve uzla — do tohto repozitára sa neukladá,
sťahuje sa len na účely validácie.

| ID | Názov | Profil (cesta) | Profil (URL) | Stav |
|---|---|---|---|---|
| NODE-001 | Jawra |  | https://github.com/matejolsavsky/jawra-profile/blob/main/PROFILE.md | pripravuje sa |
