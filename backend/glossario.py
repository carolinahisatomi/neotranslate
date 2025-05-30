import csv

def carregar_glossario(caminho='glossario.csv'):
    glossario = {}
    try:
        with open(caminho, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                termo_en = row.get('en', '').strip()
                termo_pt = row.get('pt', '').strip()
                if termo_en and termo_pt:
                    glossario[termo_en.lower()] = termo_pt
    except FileNotFoundError:
        pass
    return glossario

def aplicar_glossario(texto, glossario):
    for termo_en, termo_pt in glossario.items():
        if termo_en in texto:
            texto = texto.replace(termo_en, termo_pt)
    return texto
