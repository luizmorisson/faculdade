def mostrar_mensagem_e_numero(mensagem, numero):
    print("Mensagem:", mensagem)
    print("Número:", numero)
def main():
    mensagem = input("Digite uma mensagem: ")
    numero = input("Digite um número: ")
    mostrar_mensagem_e_numero(mensagem, numero)
if __name__ == "__main__":
    main()