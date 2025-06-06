import csv
from pathlib import Path

from backend.glossario import carregar_glossario

def test_carregar_glossario(tmp_path: Path):
    caminho = tmp_path / "glossario.csv"
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["en", "pt"])
        writer.writeheader()
        writer.writerow({"en": "inverter", "pt": "inversor"})
        writer.writerow({"en": "battery", "pt": "bateria"})

    glossario = carregar_glossario(str(caminho))
    assert glossario == {"inverter": "inversor", "battery": "bateria"}