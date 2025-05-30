import os
import csv

PASTA_MEMORIA = "memoria_traducao"
os.makedirs(PASTA_MEMORIA, exist_ok=True)

def carregar_memoria():
    memoria = []
    for arquivo in os.listdir(PASTA_MEMORIA):
        if arquivo.endswith(".csv"):
            with open(os.path.join(PASTA_MEMORIA, arquivo), newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    memoria.append((row['original'], row['traducao_corrigida']))
    return memoria

def salvar_memoria(nome_arquivo, traducoes_corrigidas):
    caminho = os.path.join(PASTA_MEMORIA, nome_arquivo)
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["original", "traducao_automatica", "traducao_corrigida"])
        writer.writerows(traducoes_corrigidas)
