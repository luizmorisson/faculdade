def calcular_idade(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento
    return idade
def main():
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    ano_atual = int(input("Digite o ano atual: "))
    idade = calcular_idade(ano_nascimento, ano_atual)
    print("Sua idade é:", idade)
if __name__ == "__main__":
    main()