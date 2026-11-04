from data.persistencia import carregar_banco, salvar_banco
from gui.janela_principal import abrir_janela


if __name__ == "__main__":
    carregar_banco()

    try:
        abrir_janela()
    finally:
        salvar_banco()