"""Validátor profilu uzla proti Štandardu profilu uzla siete Forge v0.1."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

STANDARD_VERZIA = "v0.1"

POVINNE_SEKCIE: tuple[tuple[str, str], ...] = (
    ("3.1", "Identifikácia uzla"),
    ("3.2", "Kapacita"),
    ("3.3", "Materiály"),
    ("3.4", "Pracovný objem"),
    ("3.5", "Ponuka"),
    ("3.6", "Cenník — štruktúra"),
    ("3.7", "Lehoty"),
    ("3.8", "Kontakt"),
    ("3.9", "Stav dostupnosti"),
)

_SEKCIA_3_9 = "3.9"
_STAV_HODNOTY = ("prijíma zákazky", "obmedzene", "neprijíma")

_NADPIS_RE = re.compile(r"^#{1,6} (.*)$")
_DATUM_RE = re.compile(r"\d{4}-\d{2}-\d{2}")


@dataclass(frozen=True)
class Nalez:
    kod: str
    sprava: str
    riadok: int | None


def _ocisti(text: str, znaky: str) -> str:
    for znak in znaky:
        text = text.replace(znak, "")
    return text


def _zluc_medzery(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _normalizuj_nazov(text: str) -> str:
    text = text.lower()
    text = text.replace("—", "-").replace("–", "-")
    return _zluc_medzery(text)


def _najdi_nadpisy(riadky: list[str]) -> list[tuple[int, str]]:
    nadpisy = []
    for i, riadok in enumerate(riadky, start=1):
        zhoda = _NADPIS_RE.match(riadok)
        if zhoda:
            text = _zluc_medzery(_ocisti(zhoda.group(1), "*_"))
            nadpisy.append((i, text))
    return nadpisy


def _skontroluj_hlavicku(riadky: list[str]) -> list[Nalez]:
    for i, riadok in enumerate(riadky, start=1):
        ocisteny = _ocisti(riadok, "*_#")
        pozicia = ocisteny.lower().find("standard:")
        if pozicia == -1:
            continue
        zvysok = ocisteny[pozicia + len("standard:") :]
        tokeny = zvysok.split()
        token = tokeny[0] if tokeny else ""
        hodnota = token.strip("*_()").rstrip(",.")
        if hodnota != STANDARD_VERZIA:
            return [Nalez("H002", f"Verzia štandardu '{hodnota}' nezodpovedá {STANDARD_VERZIA}.", i)]
        return []
    return [Nalez("H001", "Hlavička so štandardom ('standard: v0.1') v profile chýba.", None)]


def _skontroluj_sekcie(nadpisy: list[tuple[int, str]]) -> tuple[list[Nalez], tuple[int, str] | None]:
    nalezy: list[Nalez] = []
    sekcia_3_9 = None
    for cislo, nazov in POVINNE_SEKCIE:
        vzor = re.compile(rf"^{re.escape(cislo)}(\s|$)")
        najdeny = None
        for riadok_c, text in nadpisy:
            if vzor.match(text):
                najdeny = (riadok_c, text)
                break
        if najdeny is None:
            nalezy.append(Nalez("S001", f"Povinná sekcia {cislo} {nazov} chýba.", None))
            continue
        riadok_c, text = najdeny
        if cislo == _SEKCIA_3_9:
            sekcia_3_9 = (riadok_c, text)
        ocakavany = f"{cislo} {nazov}"
        if _normalizuj_nazov(text) != _normalizuj_nazov(ocakavany):
            nalezy.append(Nalez("S002", f"Sekcia {cislo} má neočakávaný názov nadpisu.", riadok_c))
    return nalezy, sekcia_3_9


def _telo_sekcie(riadky: list[str], nadpisy: list[tuple[int, str]], riadok_nadpisu: int) -> str:
    dalsi_riadok = None
    for riadok_c, _ in nadpisy:
        if riadok_c > riadok_nadpisu:
            dalsi_riadok = riadok_c
            break
    koniec = (dalsi_riadok - 1) if dalsi_riadok is not None else len(riadky)
    return "\n".join(riadky[riadok_nadpisu:koniec])


def _skontroluj_stav_dostupnosti(riadky: list[str], nadpisy: list[tuple[int, str]], sekcia: tuple[int, str]) -> list[Nalez]:
    riadok_nadpisu, _ = sekcia
    telo = _telo_sekcie(riadky, nadpisy, riadok_nadpisu)
    ocisteny_telo = _ocisti(telo, "`*").lower()
    nalezy: list[Nalez] = []
    if not any(hodnota in ocisteny_telo for hodnota in _STAV_HODNOTY):
        nalezy.append(Nalez("P001", "V sekcii 3.9 chýba stav dostupnosti (prijíma zákazky / obmedzene / neprijíma).", None))
    if not _DATUM_RE.search(telo):
        nalezy.append(Nalez("P002", "V sekcii 3.9 chýba dátum v tvare RRRR-MM-DD.", None))
    return nalezy


def validuj(text: str) -> list[Nalez]:
    riadky = text.splitlines()
    nalezy: list[Nalez] = []
    nalezy.extend(_skontroluj_hlavicku(riadky))

    nadpisy = _najdi_nadpisy(riadky)
    nalezy_sekcie, sekcia_3_9 = _skontroluj_sekcie(nadpisy)
    nalezy.extend(nalezy_sekcie)

    if sekcia_3_9 is not None:
        nalezy.extend(_skontroluj_stav_dostupnosti(riadky, nadpisy, sekcia_3_9))

    nalezy.sort(key=lambda n: (n.riadok is not None, n.riadok or 0, n.kod))
    return nalezy


def nacitaj_a_validuj(cesta: str | Path) -> list[Nalez]:
    text = Path(cesta).read_text(encoding="utf-8")
    return validuj(text)


def hlavna(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    if len(argv) != 1:
        print("použitie: python -m forge_platform.profil <cesta k PROFILE.md>", file=sys.stderr)
        return 2

    cesta = argv[0]
    try:
        nalezy = nacitaj_a_validuj(cesta)
    except OSError:
        print(f"Súbor sa nedá prečítať: {cesta}", file=sys.stderr)
        return 2

    if not nalezy:
        print(f"Profil je v súlade so štandardom {STANDARD_VERZIA}.")
        return 0

    for nalez in nalezy:
        if nalez.riadok is None:
            print(f"{nalez.kod} · {nalez.sprava}")
        else:
            print(f"{nalez.kod} · riadok {nalez.riadok} · {nalez.sprava}")
    return 1
