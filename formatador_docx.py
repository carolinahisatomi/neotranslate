
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt

def adicionar_secao_formatada(doc, titulo, estilo_base):
    doc.add_page_break()
    par = doc.add_paragraph()
    run = par.add_run(titulo.upper())
    run.bold = True
    run.font.size = Pt(estilo_base['tamanho'] + 2)
    run.font.name = estilo_base['fonte']
    par.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

def adicionar_secoes_padrao(doc, estilo_base, incluir_advertencias=True, incluir_especificacoes=True, incluir_orientacoes=True):
    if incluir_advertencias:
        adicionar_secao_formatada(doc, "ADVERTÊNCIAS", estilo_base)
    if incluir_especificacoes:
        adicionar_secao_formatada(doc, "ESPECIFICAÇÕES TÉCNICAS", estilo_base)
    if incluir_orientacoes:
        adicionar_secao_formatada(doc, "ORIENTAÇÕES", estilo_base)
