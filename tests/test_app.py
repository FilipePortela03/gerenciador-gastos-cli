import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

import app


def test_carregar_gastos_cria_arquivo_se_nao_existir(tmp_path):
    arquivo_teste = tmp_path / "gastos.json"
    app.ARQUIVO = str(arquivo_teste)

    gastos = app.carregar_gastos()

    assert gastos == []
    assert arquivo_teste.exists()


def test_salvar_e_carregar_gastos(tmp_path):
    arquivo_teste = tmp_path / "gastos.json"
    app.ARQUIVO = str(arquivo_teste)

    gastos_entrada = [
        {"nome": "Mercado", "valor": 100.0, "categoria": "Alimentacao"},
        {"nome": "Uber", "valor": 25.0, "categoria": "Transporte"},
    ]

    app.salvar_gastos(gastos_entrada)
    gastos_saida = app.carregar_gastos()

    assert gastos_saida == gastos_entrada


def test_carregar_gastos_corrige_categoria_ausente(tmp_path):
    arquivo_teste = tmp_path / "gastos.json"
    app.ARQUIVO = str(arquivo_teste)

    dados_antigos = [
        {"nome": "Padaria", "valor": 15.0}
    ]

    with open(arquivo_teste, "w", encoding="utf-8") as arquivo:
        json.dump(dados_antigos, arquivo)

    gastos = app.carregar_gastos()

    assert gastos[0]["categoria"] == "Outros"