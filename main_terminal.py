from data.persistencia import carregar_banco, salvar_banco
from services.menu import executar_menu


if __name__ == "__main__":
    carregar_banco()

    try:
        executar_menu()
    finally:
        salvar_banco()