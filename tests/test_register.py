import json
import re
from pathlib import Path

from forge_platform.register import (
    ChybaRegistra,
    KodyRegistra,
    hlavna,
    nacitaj_register,
    validuj_register,
)

FIXTURES = Path(__file__).parent / "fixtures"
REGISTER = Path(__file__).parent.parent / "uzly" / "REGISTER.md"
DOCS_KODY_REGISTRA = Path(__file__).parent.parent / "docs" / "KODY-REGISTRA.md"


def test_nacitanie_realneho_registra():
    zaznamy = nacitaj_register(REGISTER)
    assert len(zaznamy) == 1
    zaznam = zaznamy[0]
    assert zaznam.id == "NODE-001"
    assert zaznam.cesta is None
    assert zaznam.url


def test_platny_profil_je_v_sulade():
    vysledky = validuj_register(FIXTURES / "register_platny.md")
    assert len(vysledky) == 1
    assert vysledky[0].nalezy == []
    assert vysledky[0].preskoceny is False
    assert hlavna([str(FIXTURES / "register_platny.md")]) == 0


def test_profil_s_nalezom():
    vysledky = validuj_register(FIXTURES / "register_s_nalezom.md")
    kody = [n.kod for n in vysledky[0].nalezy]
    assert kody == ["S001"]
    assert hlavna([str(FIXTURES / "register_s_nalezom.md")]) == 1


def test_uzol_bez_cesty_je_preskoceny():
    vysledky = validuj_register(FIXTURES / "register_bez_cesty.md")
    assert vysledky[0].preskoceny is True
    kody = [n.kod for n in vysledky[0].nalezy]
    assert kody == [KodyRegistra.R001]
    assert hlavna([str(FIXTURES / "register_bez_cesty.md")]) == 0


def test_neexistujuca_cesta_profilu():
    vysledky = validuj_register(FIXTURES / "register_neexistujuca_cesta.md")
    assert vysledky[0].preskoceny is False
    kody = [n.kod for n in vysledky[0].nalezy]
    assert kody == [KodyRegistra.R002]
    assert hlavna([str(FIXTURES / "register_neexistujuca_cesta.md")]) == 1


def test_relativna_cesta_je_vzhladom_na_priecinok_registra():
    vysledky = validuj_register(FIXTURES / "register" / "register_vzdialeny.md")
    assert vysledky[0].nalezy == []


def test_chybajuca_hlavicka_vracia_chybu_registra():
    try:
        nacitaj_register(FIXTURES / "register_chybna_hlavicka.md")
        assert False, "malo vyhodiť ChybaRegistra"
    except ChybaRegistra:
        pass
    assert hlavna([str(FIXTURES / "register_chybna_hlavicka.md")]) == 2


def test_duplicitne_id_vracia_chybu_registra():
    try:
        nacitaj_register(FIXTURES / "register_duplicitne_id.md")
        assert False, "malo vyhodiť ChybaRegistra"
    except ChybaRegistra:
        pass
    assert hlavna([str(FIXTURES / "register_duplicitne_id.md")]) == 2


def test_hlavna_neexistujuci_register_vracia_2(capsys):
    kod = hlavna([str(FIXTURES / "neexistuje.md")])
    assert kod == 2
    vystup = capsys.readouterr().err
    assert "sa nedá prečítať" in vystup


def test_hlavna_bez_argumentu_vracia_2():
    assert hlavna([]) == 2


def test_hlavna_s_viacerymi_argumentmi_vracia_2():
    assert hlavna(["a", "b"]) == 2


def test_hlavna_textovy_vystup_pre_platny_register(capsys):
    kod = hlavna([str(FIXTURES / "register_platny.md")])
    assert kod == 0
    vystup = capsys.readouterr().out
    assert "NODE-001 · beží · v súlade" in vystup
    assert "Spolu: 1 uzlov · 1 v súlade · 0 s nálezmi · 0 preskočených" in vystup


def test_hlavna_json_platny_register(capsys):
    kod = hlavna(["--json", str(FIXTURES / "register_platny.md")])
    assert kod == 0
    vystup = json.loads(capsys.readouterr().out)
    assert vystup["standard"] == "v0.1"
    assert vystup["v_sulade"] is True
    assert vystup["uzly"][0]["id"] == "NODE-001"
    assert vystup["uzly"][0]["nalezy"] == []


def test_hlavna_json_register_s_nalezom(capsys):
    kod = hlavna([str(FIXTURES / "register_s_nalezom.md"), "--json"])
    assert kod == 1
    vystup = json.loads(capsys.readouterr().out)
    assert vystup["v_sulade"] is False
    uzol = vystup["uzly"][0]
    assert uzol["preskoceny"] is False
    kody = [n["kod"] for n in uzol["nalezy"]]
    assert kody == ["S001"]


def test_hlavna_json_chybny_register(capsys):
    kod = hlavna(["--json", str(FIXTURES / "register_chybna_hlavicka.md")])
    assert kod == 2
    vystup = json.loads(capsys.readouterr().out)
    assert "chyba" in vystup
    assert vystup["register"] == str(FIXTURES / "register_chybna_hlavicka.md")


def test_kody_v_dokumentacii_zodpovedaju_kodu():
    text = DOCS_KODY_REGISTRA.read_text(encoding="utf-8")
    kody_v_docs = set(re.findall(r"^\| ([A-Z]\d{3}) \|", text, flags=re.MULTILINE))
    kody_v_kode = {
        hodnota
        for nazov, hodnota in vars(KodyRegistra).items()
        if not nazov.startswith("_") and isinstance(hodnota, str)
    }
    assert kody_v_docs == kody_v_kode
