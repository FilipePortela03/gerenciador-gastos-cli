import json
import os

ARQUIVO = "gastos.json"


def carregar_gastos():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w") as f:
            json.dump([], f)
        return []

    with open(ARQUIVO, "r") as f:
        gastos = json.load(f)

        # Corrige dados antigos sem categoria
        for g in gastos:
            if "categoria" not in g:
                g["categoria"] = "Outros"

        return gastos


def salvar_gastos(gastos):
    with open(ARQUIVO, "w") as f:
        json.dump(gastos, f, indent=4)


def adicionar_gasto(gastos):
    nome = input("Nome do gasto: ")

    valor_input = input("Valor: ").replace(",", ".")

    try:
        valor = float(valor_input)
    except Exception:
        print("Valor inválido.")
        return

    categoria = input("Categoria: ").capitalize()

    gastos.append({
        "nome": nome,
        "valor": valor,
        "categoria": categoria
    })

    salvar_gastos(gastos)
    print("Gasto adicionado com sucesso!")


def listar_gastos(gastos):
    if not gastos:
        print("Nenhum gasto cadastrado.")
        return

    print("\nLista de gastos:")
    for i, g in enumerate(gastos, 1):
        print(f"{i}. {g['nome']} - R$ {g['valor']:.2f} ({g['categoria']})")


def total_gastos(gastos):
    total = sum(g["valor"] for g in gastos)
    print(f"\nTotal geral: R$ {total:.2f}")


def total_por_categoria(gastos):
    if not gastos:
        print("Nenhum gasto cadastrado.")
        return

    categorias = {}

    for g in gastos:
        cat = g["categoria"]
        categorias[cat] = categorias.get(cat, 0) + g["valor"]

    print("\nTotal por categoria:")
    for cat, valor in categorias.items():
        print(f"{cat}: R$ {valor:.2f}")


def filtrar_categoria(gastos):
    if not gastos:
        print("Nenhum gasto cadastrado.")
        return

    categorias = sorted(set(g["categoria"] for g in gastos))

    print("\nCategorias disponíveis:")
    for i, cat in enumerate(categorias, 1):
        print(f"{i}. {cat}")

    try:
        escolha = int(input("Escolha o número da categoria: ")) - 1
        categoria_escolhida = categorias[escolha]

        filtrados = [g for g in gastos if g["categoria"] == categoria_escolhida]

        print(f"\nGastos em '{categoria_escolhida}':")
        for i, g in enumerate(filtrados, 1):
            print(f"{i}. {g['nome']} - R$ {g['valor']:.2f}")

    except Exception:
        print("Opção inválida.")


def editar_gasto(gastos):
    listar_gastos(gastos)

    try:
        i = int(input("Número para editar: ")) - 1
        g = gastos[i]

        novo_nome = input(f"Novo nome ({g['nome']}): ") or g["nome"]

        novo_valor_input = input(f"Novo valor ({g['valor']}): ").replace(",", ".")
        novo_valor = float(novo_valor_input) if novo_valor_input else g["valor"]

        nova_categoria = input(f"Nova categoria ({g['categoria']}): ") or g["categoria"]

        g["nome"] = novo_nome
        g["valor"] = novo_valor
        g["categoria"] = nova_categoria.capitalize()

        salvar_gastos(gastos)
        print("Gasto atualizado com sucesso!")

    except Exception:
        print("Erro ao editar.")


def remover_gasto(gastos):
    listar_gastos(gastos)

    try:
        i = int(input("Número para remover: ")) - 1
        removido = gastos.pop(i)

        salvar_gastos(gastos)
        print(f"Removido: {removido['nome']}")

    except Exception:
        print("Erro ao remover.")


def main():
    gastos = carregar_gastos()

    while True:
        print("\n=== GERENCIADOR DE GASTOS ===")
        print("1. Adicionar gasto")
        print("2. Listar gastos")
        print("3. Mostrar total geral")
        print("4. Mostrar total por categoria")
        print("5. Filtrar por categoria")
        print("6. Editar gasto")
        print("7. Remover gasto")
        print("8. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_gasto(gastos)
        elif opcao == "2":
            listar_gastos(gastos)
        elif opcao == "3":
            total_gastos(gastos)
        elif opcao == "4":
            total_por_categoria(gastos)
        elif opcao == "5":
            filtrar_categoria(gastos)
        elif opcao == "6":
            editar_gasto(gastos)
        elif opcao == "7":
            remover_gasto(gastos)
        elif opcao == "8":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()