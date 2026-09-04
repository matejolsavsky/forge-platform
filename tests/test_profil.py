from pathlib import Path

from forge_platform.profil import STANDARD_VERZIA, hlavna, nacitaj_a_validuj

FIXTURES = Path(__file__).parent / "fixtures"


def test_platny_profil_bez_nalezov():
    nalezy = nacitaj_a_validuj(FIXTURES / "profil_platny.md")
    assert nalezy == []


def test_chybajuca_hlavicka():
    nalezy = nacitaj_a_validuj(FIXTURES / "profil_bez_hlavicky.md")
    kody = [n.kod for n in nalezy]
    assert "H001" in kody
    nalez = next(n for n in nalezy if n.kod == "H001")
    assert nalez.riadok is None


def test_chybajuca_sekcia():
    nalezy = nacitaj_a_validuj(FIXTURES / "profil_bez_sekcie.md")
    assert len(nalezy) == 1
    assert nalezy[0].kod == "S001"
    assert nalezy[0].riadok is None
    assert "3.5" in nalezy[0].sprava


def test_zla_verzia_standardu():
    nalezy = nacitaj_a_validuj(FIXTURES / "profil_zla_verzia.md")
    kody = [n.kod for n in nalezy]
    assert kody == ["H002"]
    assert nalezy[0].riadok is not None


def test_standard_verzia_konstanta():
    assert STANDARD_VERZIA == "v0.1"


def test_hlavna_bez_nalezov_vracia_0(capsys):
    kod = hlavna([str(FIXTURES / "profil_platny.md")])
    assert kod == 0
    vystup = capsys.readouterr().out
    assert "v súlade so štandardom v0.1" in vystup


def test_hlavna_s_nalezmi_vracia_1(capsys):
    kod = hlavna([str(FIXTURES / "profil_bez_sekcie.md")])
    assert kod == 1
    vystup = capsys.readouterr().out
    assert "S001" in vystup


def test_hlavna_neexistujuci_subor_vracia_2(capsys):
    kod = hlavna([str(FIXTURES / "neexistuje.md")])
    assert kod == 2
    vystup = capsys.readouterr().err
    assert "Súbor sa nedá prečítať" in vystup


def test_hlavna_bez_argumentu_vracia_2(capsys):
    kod = hlavna([])
    assert kod == 2


def test_hlavna_s_viacerymi_argumentmi_vracia_2(capsys):
    kod = hlavna(["a", "b"])
    assert kod == 2
