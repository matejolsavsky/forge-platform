"""Register uzlov a hromadná validácia profilov nad Štandardom profilu uzla siete Forge v0.1."""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from forge_platform.profil import Nalez, nacitaj_a_validuj, nalezy_ako_dict

STANDARD_VERZIA = "v0.1"

_HLAVICKA = "| ID | Názov | Profil (cesta) | Profil (URL) | Stav |"
_ID_RE = re.compile(r"^NODE-\d{3}$")


class KodyRegistra:
    """Stabilné kódy nálezov registra — verejný kontrakt (docs/KODY-REGISTRA.md).

    Kódy sa nemenia a nerušia, len pridávajú.
    """

    R001 = "R001"
    R002 = "R002"


class ChybaRegistra(Exception):
    """Register sa nedá spracovať (chybný formát tabuľky)."""


@dataclass(frozen=True)
class ZaznamUzla:
    id: str
    nazov: str
    cesta: str | None
    url: str | None
    stav: str


@dataclass(frozen=True)
class VysledokUzla:
    zaznam: ZaznamUzla
    nalezy: list[Nalez]
    preskoceny: bool


def _rozdel_riadok_tabulky(riadok: str) -> list[str]:
    riadok = riadok.strip().strip("|")
    return [bunka.strip() for bunka in riadok.split("|")]


def _je_riadok_oddelovaca(riadok: str) -> bool:
    obsah = riadok.strip()
    return bool(obsah) and set(obsah) <= set("|:- ")


def nacitaj_register(cesta: str | Path) -> list[ZaznamUzla]:
    text = Path(cesta).read_text(encoding="utf-8")
    riadky = text.splitlines()

    hlavicka_i = None
    for i, riadok in enumerate(riadky):
        if riadok.strip() == _HLAVICKA:
            hlavicka_i = i
            break
    if hlavicka_i is None:
        raise ChybaRegistra("Register neobsahuje tabuľku s očakávanou hlavičkou.")

    i = hlavicka_i + 1
    if i < len(riadky) and _je_riadok_oddelovaca(riadky[i]):
        i += 1

    zaznamy: list[ZaznamUzla] = []
    videne_id: set[str] = set()
    while i < len(riadky) and riadky[i].strip().startswith("|"):
        bunky = _rozdel_riadok_tabulky(riadky[i])
        if len(bunky) != 5:
            raise ChybaRegistra(f"Riadok {i + 1}: neočakávaný počet stĺpcov.")
        id_, nazov, cesta_bunka, url_bunka, stav = bunky
        if not _ID_RE.match(id_):
            raise ChybaRegistra(f"Riadok {i + 1}: ID '{id_}' nezodpovedá tvaru NODE-xxx.")
        if id_ in videne_id:
            raise ChybaRegistra(f"Riadok {i + 1}: duplicitné ID '{id_}'.")
        videne_id.add(id_)
        zaznamy.append(
            ZaznamUzla(
                id=id_,
                nazov=nazov,
                cesta=cesta_bunka or None,
                url=url_bunka or None,
                stav=stav,
            )
        )
        i += 1

    return zaznamy


def validuj_register(cesta: str | Path) -> list[VysledokUzla]:
    cesta = Path(cesta)
    zaznamy = nacitaj_register(cesta)

    vysledky: list[VysledokUzla] = []
    for zaznam in zaznamy:
        if zaznam.cesta is None:
            vysledky.append(
                VysledokUzla(
                    zaznam=zaznam,
                    nalezy=[Nalez(KodyRegistra.R001, "Uzol nemá v registri lokálnu cestu k profilu — preskočený.", None)],
                    preskoceny=True,
                )
            )
            continue

        try:
            nalezy = nacitaj_a_validuj(cesta.parent / zaznam.cesta)
        except OSError:
            vysledky.append(
                VysledokUzla(
                    zaznam=zaznam,
                    nalezy=[Nalez(KodyRegistra.R002, "Profil na uvedenej ceste sa nedá prečítať.", None)],
                    preskoceny=False,
                )
            )
            continue

        vysledky.append(VysledokUzla(zaznam=zaznam, nalezy=nalezy, preskoceny=False))

    return vysledky


def vysledky_ako_dict(vysledky: list[VysledokUzla]) -> list[dict]:
    return [
        {
            "id": v.zaznam.id,
            "nazov": v.zaznam.nazov,
            "stav": v.zaznam.stav,
            "cesta": v.zaznam.cesta,
            "url": v.zaznam.url,
            "preskoceny": v.preskoceny,
            "nalezy": nalezy_ako_dict(v.nalezy),
        }
        for v in vysledky
    ]


def _slovo_nalezy(pocet: int) -> str:
    if pocet == 1:
        return "nález"
    if 2 <= pocet <= 4:
        return "nálezy"
    return "nálezov"


def _riadok_uzla(vysledok: VysledokUzla) -> str:
    zaznam = vysledok.zaznam
    predpona = f"{zaznam.id} · {zaznam.stav} · "

    if vysledok.preskoceny:
        return predpona + f"preskočený ({vysledok.nalezy[0].kod})"
    if not vysledok.nalezy:
        return predpona + "v súlade"

    pocet = len(vysledok.nalezy)
    kody = ", ".join(nalez.kod for nalez in vysledok.nalezy)
    return predpona + f"{pocet} {_slovo_nalezy(pocet)} · {kody}"


def _riadok_suhrnu(vysledky: list[VysledokUzla]) -> str:
    preskocenych = sum(1 for v in vysledky if v.preskoceny)
    v_sulade = sum(1 for v in vysledky if not v.preskoceny and not v.nalezy)
    s_nalezmi = sum(1 for v in vysledky if not v.preskoceny and v.nalezy)
    return (
        f"Spolu: {len(vysledky)} uzlov · {v_sulade} v súlade · "
        f"{s_nalezmi} s nálezmi · {preskocenych} preskočených"
    )


def _urcit_kod(vysledky: list[VysledokUzla]) -> int:
    return 1 if any(v.nalezy for v in vysledky if not v.preskoceny) else 0


def hlavna(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    json_vystup = False
    cesty = []
    neznamy_prepinac = False
    for arg in argv:
        if arg == "--json":
            json_vystup = True
        elif arg.startswith("--"):
            neznamy_prepinac = True
        else:
            cesty.append(arg)

    if neznamy_prepinac or len(cesty) != 1:
        print("použitie: python -m forge_platform.register [--json] <cesta k registru>", file=sys.stderr)
        return 2

    cesta = cesty[0]
    try:
        vysledky = validuj_register(cesta)
    except OSError:
        if json_vystup:
            print(json.dumps({"register": cesta, "chyba": "Register sa nedá prečítať"}, ensure_ascii=False))
        print(f"Register sa nedá prečítať: {cesta}", file=sys.stderr)
        return 2
    except ChybaRegistra as chyba:
        if json_vystup:
            print(json.dumps({"register": cesta, "chyba": str(chyba)}, ensure_ascii=False))
        print(f"Register je chybný: {chyba}", file=sys.stderr)
        return 2

    kod = _urcit_kod(vysledky)

    if json_vystup:
        vystup = {
            "standard": STANDARD_VERZIA,
            "register": cesta,
            "v_sulade": kod == 0,
            "uzly": vysledky_ako_dict(vysledky),
        }
        print(json.dumps(vystup, ensure_ascii=False))
        return kod

    for vysledok in vysledky:
        print(_riadok_uzla(vysledok))
    print(_riadok_suhrnu(vysledky))
    return kod
